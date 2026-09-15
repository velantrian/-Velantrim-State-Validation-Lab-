#!/usr/bin/env python3
"""
SEM-REV-E0 v1 implementation scorer.
IMPLEMENTATION_TEST_ONLY — not a CORE experiment result.

Oracle material (REQUIRED / FORBIDDEN atoms) is loaded ONLY after the
S5 hash file exists and matches the exact on-disk projection bytes.

Enforces the COMPLETE frozen REQUIRED / FORBIDDEN atom sets for
Fixture A, Fixture B, and Fixture C.
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


def excluded_entry(fixture_b, key, value):
    for item in fixture_b.get('excluded', []):
        if item.get(key) == value:
            return item
    return None


def excluded_reasons(fixture_b, key, value):
    item = excluded_entry(fixture_b, key, value)
    return list(item.get('reasons') or []) if item else []


def score(projection):
    proj = projection['s5_projection']
    fa = proj['fixture_a']
    fb = proj['fixture_b']
    fc = proj['fixture_c']
    a = fa['assertions']
    required_ok = []
    required_missing = []
    forbidden_hits = []

    def req(name, ok):
        if ok:
            required_ok.append(name)
        else:
            required_missing.append(name)
            print(f'REQUIRED missing: {name}')

    def forbid(name, hit):
        if hit:
            forbidden_hits.append(name)
            print(f'FORBIDDEN present: {name}')

    # ----- Fixture A REQUIRED -----
    req('A.force=proposal', a['as:path-a-v1']['semantic_force'] == 'proposal')
    req('A.status=retracted', a['as:path-a-v1']['status'] == 'retracted')
    req('A.rejection_reason=R1_CONSTRAINT_FAILURE',
        a['as:path-a-v1'].get('rejection_reason') == 'R1_CONSTRAINT_FAILURE')
    req('B.force=decision', a['as:path-b-v1']['semantic_force'] == 'decision')
    req('B.status=superseded', a['as:path-b-v1']['status'] == 'superseded')
    req('B.decision_reason=R2_MEETS_K1',
        a['as:path-b-v1'].get('decision_reason') == 'R2_MEETS_K1')
    req('C.force=decision', a['as:path-c-v1']['semantic_force'] == 'decision')
    req('C.status=current', a['as:path-c-v1']['status'] == 'current')
    req('C.decision_reason=R3_NEW_REQUIREMENT_K2',
        a['as:path-c-v1'].get('decision_reason') == 'R3_NEW_REQUIREMENT_K2')
    req('current_path=Path-C', fa.get('current_path') == 'Path-C')
    req('reopen_B_requires=Y_K2_REMOVED_AND_OWNER_REAPPROVES_B',
        fa.get('reopen_B_requires') == 'Y_K2_REMOVED_AND_OWNER_REAPPROVES_B')
    req('scope=scope:project-delta', fa.get('scope') == 'scope:project-delta')
    req('absent properties remain UNKNOWN',
        a['as:path-a-v1'].get('uncertainty') == 'UNKNOWN'
        and a['as:path-a-v1'].get('reopen_requires') == 'UNKNOWN')

    # ----- Fixture A FORBIDDEN -----
    forbid('A.force=decision', a['as:path-a-v1']['semantic_force'] == 'decision')
    forbid('A.status=current', a['as:path-a-v1']['status'] == 'current')
    forbid('B.status=current', a['as:path-b-v1']['status'] == 'current')
    forbid('current_path=Path-A', fa.get('current_path') == 'Path-A')
    forbid('current_path=Path-B', fa.get('current_path') == 'Path-B')
    c_reason = a['as:path-c-v1'].get('decision_reason')
    forbid('C reason=R1 or R2', c_reason in (
        'R1_CONSTRAINT_FAILURE', 'R2_MEETS_K1', 'R1', 'R2'))
    forbid('B may reopen unconditionally',
           fa.get('reopen_B_requires') != 'Y_K2_REMOVED_AND_OWNER_REAPPROVES_B')
    forbid('scope widening', fa.get('scope') != 'scope:project-delta')
    forbid('invented reason/approval/evidence',
           c_reason != 'R3_NEW_REQUIREMENT_K2')

    # ----- Fixture B REQUIRED -----
    req('qualified_assertion_ids=[]', fb.get('qualified_assertion_ids') == [])
    req('qualified_decision_ids=[]', fb.get('qualified_decision_ids') == [])
    req('status=NO_QUALIFIED_RESULT', fb.get('status') == 'NO_QUALIFIED_RESULT')
    alpha_reasons = set(excluded_reasons(fb, 'assertion_id', 'as:alpha-v1'))
    beta_reasons = set(excluded_reasons(fb, 'assertion_id', 'as:beta-v1'))
    ad9_reasons = set(excluded_reasons(fb, 'decision_id', 'dec:ad-9'))
    req('excluded alpha contains scope_mismatch, retracted, force_not_allowed',
        {'scope_mismatch', 'retracted', 'force_not_allowed'} <= alpha_reasons)
    req('excluded beta contains scope_mismatch, no_approved_authority_decision',
        {'scope_mismatch', 'no_approved_authority_decision'} <= beta_reasons)
    req('excluded AD-9 contains authority_outcome_refused',
        'authority_outcome_refused' in ad9_reasons)

    alpha = excluded_entry(fb, 'assertion_id', 'as:alpha-v1') or {}
    beta = excluded_entry(fb, 'assertion_id', 'as:beta-v1') or {}
    ad9 = excluded_entry(fb, 'decision_id', 'dec:ad-9') or {}
    for label, item, keys in (
        ('alpha', alpha, ('scope_id', 'semantic_force', 'uncertainty', 'declared_loss',
                          'observed_at', 'recorded_at', 'valid_from')),
        ('beta', beta, ('scope_id', 'semantic_force', 'uncertainty', 'declared_loss',
                        'observed_at', 'recorded_at', 'valid_from')),
        ('AD-9', ad9, ('scope_id', 'semantic_force', 'effective_from', 'recorded_at')),
    ):
        for key in keys:
            req(f'preserve {label}.{key}', item.get(key) not in (None, ''))
    req('preserve alpha retraction', 'retracted' in alpha_reasons)
    req('preserve authority_decision dec:ad-9', bool(ad9.get('decision_id')))

    # ----- Fixture B FORBIDDEN -----
    qualified_text = json.dumps(fb.get('qualified', []))
    forbid('production_effect=40%', '40%' in qualified_text)
    forbid('production_effect=7.8%', '7.8%' in qualified_text)
    forbid('production_authorization=approved', fb.get('status') == 'QUALIFIED_RESULT')
    forbid('alpha current_qualified', any(
        q.get('assertion_id') == 'as:alpha-v1' for q in fb.get('qualified', [])))
    forbid('beta production_qualified', any(
        q.get('assertion_id') == 'as:beta-v1' for q in fb.get('qualified', [])))
    forbid('AD-9 approved', fb.get('dec_ad9_outcome') == 'approved')
    forbid('Lab-A silently widened',
           alpha.get('scope_id') not in ('lab-a', 'scope:lab-a')
           or beta.get('scope_id') not in ('lab-a', 'scope:lab-a'))
    forbid('retraction omitted', 'retracted' not in alpha_reasons)
    forbid('authority refusal omitted', 'authority_outcome_refused' not in ad9_reasons)
    forbid('declared_loss silently removed',
           int(alpha.get('declared_loss', 0)) != 1 or int(beta.get('declared_loss', 0)) != 1)

    # ----- Fixture C REQUIRED -----
    req('C.status=QUALIFIED_RESULT', fc.get('status') == 'QUALIFIED_RESULT')
    req('qualified_decision_ids contains dec:pos-1',
        'dec:pos-1' in fc.get('qualified_decision_ids', []))
    c_qual = None
    for item in fc.get('qualified', []):
        if item.get('decision_id') == 'dec:pos-1':
            c_qual = item
            break
    req('subject=ent:service:orion',
        bool(c_qual) and c_qual.get('subject') == 'ent:service:orion')
    req('scope=scope:production-eu',
        bool(c_qual) and c_qual.get('scope_id') == 'scope:production-eu')
    req('outcome=approved', bool(c_qual) and c_qual.get('outcome') == 'approved')
    req('semantic_force=authority_decision',
        bool(c_qual) and c_qual.get('semantic_force') == 'authority_decision')
    req('authority=principal:release-board',
        bool(c_qual) and c_qual.get('authority_id') == 'principal:release-board')

    # ----- Fixture C FORBIDDEN -----
    forbid('NO_QUALIFIED_RESULT', fc.get('status') == 'NO_QUALIFIED_RESULT')
    forbid('outcome=refused', bool(c_qual) and c_qual.get('outcome') == 'refused')
    forbid('wrong scope', bool(c_qual) and c_qual.get('scope_id') != 'scope:production-eu')
    forbid('authority=UNKNOWN', bool(c_qual) and c_qual.get('authority_id') in (
        None, '', 'UNKNOWN'))
    forbid('decision omitted', 'dec:pos-1' not in fc.get('qualified_decision_ids', []))
    forbid('trivial abstention', fc.get('status') in (
        'NO_QUALIFIED_RESULT', 'EMPTY', 'ABSTAIN', None))

    # S5 must not leak runtime paths into normative projection
    if 'database_path' in proj:
        forbidden_hits.append('database_path in S5 projection')
        print('FORBIDDEN present: database_path in S5 projection')

    result = {
        'required_ok': required_ok,
        'required_missing': required_missing,
        'forbidden_hits': forbidden_hits,
        'scorer_pass': (not required_missing) and (not forbidden_hits),
        'label': 'IMPLEMENTATION_TEST_ONLY',
        'core_result_produced': False,
        'oracle_atoms_complete': True,
    }
    print('REQUIRED satisfied:', len(required_ok))
    print('REQUIRED missing:', required_missing)
    print('FORBIDDEN hits:', forbidden_hits)
    print('Scoring Harness: Oracle accessed AFTER S5 hash fixed')
    print('Scoring Harness: COMPLETE frozen A/B/C atom sets')
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
