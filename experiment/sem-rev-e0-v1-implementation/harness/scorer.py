#!/usr/bin/env python3
"""
SEM-REV-E0 v1 implementation scorer.
IMPLEMENTATION_TEST_ONLY — not a CORE experiment result.

Oracle material (REQUIRED / FORBIDDEN atoms) is loaded ONLY after the
S5 hash file exists and matches the exact on-disk projection bytes.
"""

import hashlib
import json
import os
import sys


def freeze_root():
    here = os.path.dirname(os.path.abspath(__file__))
    impl = os.path.dirname(here)
    repo = os.path.dirname(os.path.dirname(impl))
    return os.path.join(repo, 'docs', 'research', 'sem_rev_e0', 'freeze', 'v1')


def verify_s5_hash(output_path='s5_output.json', hash_path='s5_output.sha256'):
    if not os.path.exists(output_path):
        print('ERROR: S5 output not found — oracle unavailable before S5 hash')
        return None
    if not os.path.exists(hash_path):
        print('ERROR: S5 hash file not found — oracle unavailable before S5 hash')
        return None
    with open(hash_path, 'r', encoding='utf-8') as f:
        hash_line = f.read()
    if not hash_line.endswith('\n'):
        print('ERROR: hash file missing terminating newline')
        return None
    expected_hash = hash_line.strip().split()[0]
    with open(output_path, 'rb') as f:
        content = f.read()
    actual_hash = hashlib.sha256(content).hexdigest()
    if expected_hash != actual_hash:
        print('ERROR: Hash mismatch')
        return None
    print('Hash verified')
    return json.loads(content.decode('utf-8'))


def excluded_reasons(fixture_b, key, value):
    for item in fixture_b.get('excluded', []):
        if item.get(key) == value:
            return list(item.get('reasons') or [])
    return []


def score(projection):
    proj = projection['s5_projection']
    fa = proj['fixture_a']
    fb = proj['fixture_b']
    fc = proj['fixture_c']
    a = fa['assertions']
    required_ok = []
    forbidden_hits = []

    checks = [
        ('A.force=proposal', a['as:path-a-v1']['semantic_force'] == 'proposal'),
        ('A.status=retracted', a['as:path-a-v1']['status'] == 'retracted'),
        ('A.rejection_reason=R1_CONSTRAINT_FAILURE',
         a['as:path-a-v1'].get('rejection_reason') == 'R1_CONSTRAINT_FAILURE'),
        ('B.force=decision', a['as:path-b-v1']['semantic_force'] == 'decision'),
        ('B.status=superseded', a['as:path-b-v1']['status'] == 'superseded'),
        ('B.decision_reason=R2_MEETS_K1',
         a['as:path-b-v1'].get('decision_reason') == 'R2_MEETS_K1'),
        ('C.force=decision', a['as:path-c-v1']['semantic_force'] == 'decision'),
        ('C.status=current', a['as:path-c-v1']['status'] == 'current'),
        ('C.decision_reason=R3_NEW_REQUIREMENT_K2',
         a['as:path-c-v1'].get('decision_reason') == 'R3_NEW_REQUIREMENT_K2'),
        ('current_path=Path-C', fa.get('current_path') == 'Path-C'),
        ('reopen_B_requires=Y_K2_REMOVED_AND_OWNER_REAPPROVES_B',
         fa.get('reopen_B_requires') == 'Y_K2_REMOVED_AND_OWNER_REAPPROVES_B'),
        ('scope=scope:project-delta', fa.get('scope') == 'scope:project-delta'),
        ('B.qualified empty', fb.get('qualified_assertion_ids') == []),
        ('B.qualified decisions empty', fb.get('qualified_decision_ids') == []),
        ('B.status=NO_QUALIFIED_RESULT', fb.get('status') == 'NO_QUALIFIED_RESULT'),
        ('C.status=QUALIFIED_RESULT', fc.get('status') == 'QUALIFIED_RESULT'),
        ('C.contains dec:pos-1', 'dec:pos-1' in fc.get('qualified_decision_ids', [])),
    ]
    for name, ok in checks:
        if ok:
            required_ok.append(name)
        else:
            print(f'REQUIRED missing: {name}')

    alpha_reasons = set(excluded_reasons(fb, 'assertion_id', 'as:alpha-v1'))
    beta_reasons = set(excluded_reasons(fb, 'assertion_id', 'as:beta-v1'))
    ad9_reasons = set(excluded_reasons(fb, 'decision_id', 'dec:ad-9'))
    multi = [
        ('alpha scope_mismatch', 'scope_mismatch' in alpha_reasons),
        ('alpha retracted', 'retracted' in alpha_reasons),
        ('alpha force_not_allowed', 'force_not_allowed' in alpha_reasons),
        ('beta scope_mismatch', 'scope_mismatch' in beta_reasons),
        ('beta no_approved_authority_decision',
         'no_approved_authority_decision' in beta_reasons),
        ('AD-9 authority_outcome_refused',
         'authority_outcome_refused' in ad9_reasons),
    ]
    for name, ok in multi:
        if ok:
            required_ok.append(name)
        else:
            print(f'REQUIRED missing: {name}')

    forbidden = [
        ('A.force=decision', a['as:path-a-v1']['semantic_force'] == 'decision'),
        ('A.status=current', a['as:path-a-v1']['status'] == 'current'),
        ('B.status=current', a['as:path-b-v1']['status'] == 'current'),
        ('current_path=Path-A', fa.get('current_path') == 'Path-A'),
        ('current_path=Path-B', fa.get('current_path') == 'Path-B'),
        ('C.status=NO_QUALIFIED_RESULT', fc.get('status') == 'NO_QUALIFIED_RESULT'),
        ('AD-9 approved', fb.get('dec_ad9_outcome') == 'approved'),
        ('B production approved', fb.get('status') == 'QUALIFIED_RESULT'),
    ]
    for name, hit in forbidden:
        if hit:
            forbidden_hits.append(name)
            print(f'FORBIDDEN present: {name}')

    for item in fb.get('excluded', []):
        if item.get('assertion_id') in ('as:alpha-v1', 'as:beta-v1'):
            if int(item.get('declared_loss', 0)) != 1:
                forbidden_hits.append(f"declared_loss removed for {item.get('assertion_id')}")

    result = {
        'required_ok': required_ok,
        'required_missing': [n for n, ok in checks + multi if not ok],
        'forbidden_hits': forbidden_hits,
        'scorer_pass': (not [n for n, ok in checks + multi if not ok]) and (not forbidden_hits),
        'label': 'IMPLEMENTATION_TEST_ONLY',
        'core_result_produced': False,
    }
    print('REQUIRED satisfied:', len(required_ok))
    print('REQUIRED missing:', result['required_missing'])
    print('FORBIDDEN hits:', forbidden_hits)
    print('Scoring Harness: Oracle accessed AFTER S5 hash fixed')
    print('Scoring Harness: IMPLEMENTATION_TEST_ONLY')
    if result['scorer_pass']:
        print('Scoring Harness: SUCCESS')
    else:
        print('Scoring Harness: FAIL')
    return result


def main():
    print('Scoring Harness: Starting...')
    projection = verify_s5_hash()
    if projection is None:
        sys.exit(1)
    print('S5 output loaded')
    result = score(projection)
    with open('scorer_output.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    if not result['scorer_pass']:
        sys.exit(1)


if __name__ == '__main__':
    main()
