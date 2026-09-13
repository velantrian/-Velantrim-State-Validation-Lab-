#!/usr/bin/env python3
"""
S4 DETERMINISTIC QUALIFICATION
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY

Typed column/relation lookups only.
S3 membership != dependency availability.
Missing required dependency => S4 FAIL (not a normal exclusion).
Currentness is derived; no stored is_current flag is read or written.
"""

import json
import os
import sys

from runtime import QUERY_AS_OF_DEFAULT, connect, fail_exit, RuntimeGuardError


ALLOWED_FORCES_B = frozenset(['observation', 'authority_decision'])
QUERY_SCOPE_A = 'scope:project-delta'
QUERY_SCOPE_B = 'scope:production-us'
QUERY_SCOPE_C = 'scope:production-eu'
REQUIRED_OUTCOME_B = 'approved'
REQUIRED_OUTCOME_C = 'approved'
UNKNOWN = 'UNKNOWN'


def load_s3(path='s3_output.json'):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def interval_applies(valid_from, valid_to, query_as_of):
    if valid_from and valid_from > query_as_of:
        return False
    if valid_to and valid_to <= query_as_of:
        return False
    return True


def revisions_for(conn, assertion_id, query_as_of):
    cursor = conn.execute(
        """
        SELECT revision_id, revision_type, reason, effective_from,
               replacement_assertion_id
        FROM revision
        WHERE target_assertion_id = ?
          AND effective_from <= ?
        ORDER BY effective_from ASC
        """,
        (assertion_id, query_as_of),
    )
    return [dict(row) for row in cursor.fetchall()]


def require_row(conn, sql, params, label):
    row = conn.execute(sql, params).fetchone()
    if row is None:
        print(f'ERROR: required dependency missing: {label}')
        return None
    return row


def derived_status(conn, assertion_id, query_as_of):
    row = conn.execute(
        "SELECT valid_from, valid_to FROM assertion WHERE assertion_id = ?",
        (assertion_id,),
    ).fetchone()
    if row is None:
        return UNKNOWN, []
    revs = revisions_for(conn, assertion_id, query_as_of)
    if not interval_applies(row['valid_from'], row['valid_to'], query_as_of):
        if any(r['revision_type'] == 'retracts' for r in revs):
            return 'retracted', revs
        if any(r['revision_type'] == 'supersedes' for r in revs):
            return 'superseded', revs
        return 'not_current', revs
    if any(r['revision_type'] in ('retracts', 'invalidates') for r in revs):
        return 'retracted', revs
    if any(r['revision_type'] == 'supersedes' for r in revs):
        return 'superseded', revs
    return 'current', revs


def is_current(conn, assertion_id, query_as_of):
    status, _ = derived_status(conn, assertion_id, query_as_of)
    return status == 'current'


def latest_authority_for_scope(conn, scope_id, query_as_of):
    row = conn.execute(
        """
        SELECT decision_id, outcome, effective_from, reason, authority_id,
               semantic_force, scope_id, recorded_at
        FROM authority_decision
        WHERE scope_id = ?
          AND effective_from <= ?
        ORDER BY effective_from DESC
        LIMIT 1
        """,
        (scope_id, query_as_of),
    ).fetchone()
    return dict(row) if row else None


def qualify_fixture_a(conn, s3_candidates, query_as_of):
    for rev_id in ('rev:A-reject', 'rev:B-to-C'):
        row = require_row(
            conn,
            'SELECT revision_id FROM revision WHERE revision_id = ?',
            (rev_id,),
            rev_id,
        )
        if row is None:
            return None

    by_id = {}
    for candidate in s3_candidates:
        assertion_id = candidate['assertion_id']
        row = require_row(
            conn,
            """
            SELECT assertion_id, entity_id, semantic_force, scope_id, content,
                   reason, reopen_requires, valid_from, valid_to, uncertainty,
                   declared_loss, recorded_at, asserted_at
            FROM assertion WHERE assertion_id = ?
            """,
            (assertion_id,),
            assertion_id,
        )
        if row is None:
            return None
        status, revs = derived_status(conn, assertion_id, query_as_of)
        record = {
            'assertion_id': assertion_id,
            'entity_id': row['entity_id'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'content': row['content'],
            'status': status,
            'currentness': status == 'current',
            'reason': row['reason'] if row['reason'] else UNKNOWN,
            'reopen_requires': row['reopen_requires'] if row['reopen_requires'] else UNKNOWN,
            'uncertainty': row['uncertainty'] if row['uncertainty'] else UNKNOWN,
            'declared_loss': int(row['declared_loss']),
            'valid_from': row['valid_from'],
            'recorded_at': row['recorded_at'],
            'asserted_at': row['asserted_at'],
            'revisions': [
                {
                    'revision_id': r['revision_id'],
                    'revision_type': r['revision_type'],
                    'reason': r['reason'],
                    'effective_from': r['effective_from'],
                }
                for r in revs
            ],
        }
        if assertion_id == 'as:path-a-v1':
            r1 = next((r['reason'] for r in revs if r['revision_id'] == 'rev:A-reject'), UNKNOWN)
            record['rejection_reason'] = r1
            record['path'] = 'Path-A'
        elif assertion_id == 'as:path-b-v1':
            record['decision_reason'] = row['reason'] if row['reason'] else UNKNOWN
            record['path'] = 'Path-B'
        elif assertion_id == 'as:path-c-v1':
            record['decision_reason'] = row['reason'] if row['reason'] else UNKNOWN
            record['path'] = 'Path-C'
        by_id[assertion_id] = record

    for required in ('as:path-a-v1', 'as:path-b-v1', 'as:path-c-v1'):
        if required not in by_id:
            print(f'ERROR: required Fixture A assertion missing after lookup: {required}')
            return None

    current_paths = [
        rec['path'] for rec in by_id.values()
        if rec['status'] == 'current' and rec['semantic_force'] == 'decision'
    ]
    current_path = current_paths[0] if len(current_paths) == 1 else UNKNOWN

    return {
        'assertions': by_id,
        'current_path': current_path,
        'reopen_B_requires': by_id['as:path-b-v1']['reopen_requires'],
        'scope': QUERY_SCOPE_A,
    }


def qualify_fixture_b(conn, s3_candidates, query_as_of):
    alpha_rev = require_row(
        conn,
        """
        SELECT revision_id, revision_type, reason, effective_from
        FROM revision WHERE revision_id = 'rev:alpha-retract'
        """,
        (),
        'rev:alpha-retract',
    )
    if alpha_rev is None:
        print('ERROR: alpha missing revision -> S4 FAIL')
        return None

    dec_ad9 = require_row(
        conn,
        """
        SELECT decision_id, outcome, semantic_force, scope_id, reason,
               effective_from, authority_id, recorded_at
        FROM authority_decision WHERE decision_id = 'dec:ad-9'
        """,
        (),
        'dec:ad-9',
    )
    if dec_ad9 is None:
        print('ERROR: dec:ad-9 cannot be recovered - S4 FAIL')
        return None

    qualified = []
    excluded = []

    for candidate in s3_candidates:
        assertion_id = candidate['assertion_id']
        row = require_row(
            conn,
            """
            SELECT assertion_id, entity_id, semantic_force, scope_id, content,
                   valid_from, valid_to, uncertainty, declared_loss,
                   recorded_at, asserted_at
            FROM assertion WHERE assertion_id = ?
            """,
            (assertion_id,),
            assertion_id,
        )
        if row is None:
            return None

        ev = conn.execute(
            """
            SELECT e.evidence_id, e.observed_at, e.recorded_at, e.declared_loss
            FROM evidence e
            JOIN evidence_assertion_link l ON l.evidence_id = e.evidence_id
            WHERE l.assertion_id = ?
            """,
            (assertion_id,),
        ).fetchone()

        reasons = []
        status, revs = derived_status(conn, assertion_id, query_as_of)

        if row['scope_id'] != QUERY_SCOPE_B:
            reasons.append('scope_mismatch')
        if row['semantic_force'] not in ALLOWED_FORCES_B:
            reasons.append('force_not_allowed')
        if status == 'retracted' or any(r['revision_type'] == 'retracts' for r in revs):
            reasons.append('retracted')
        if not is_current(conn, assertion_id, query_as_of) and 'retracted' not in reasons:
            reasons.append('not_current')

        auth = latest_authority_for_scope(conn, QUERY_SCOPE_B, query_as_of)
        if auth is None:
            reasons.append('no_authority_decision')
        elif auth['outcome'] != REQUIRED_OUTCOME_B:
            reasons.append('no_approved_authority_decision')

        payload = {
            'assertion_id': assertion_id,
            'entity_id': row['entity_id'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'status': status,
            'currentness': status == 'current',
            'uncertainty': row['uncertainty'] if row['uncertainty'] else UNKNOWN,
            'declared_loss': int(row['declared_loss']),
            'valid_from': row['valid_from'],
            'recorded_at': row['recorded_at'],
            'asserted_at': row['asserted_at'],
            'observed_at': ev['observed_at'] if ev else UNKNOWN,
            'authority_status': auth['outcome'] if auth else UNKNOWN,
            'reasons': reasons,
        }
        if ev:
            payload['evidence_declared_loss'] = int(ev['declared_loss'])

        if reasons:
            excluded.append(payload)
        else:
            qualified.append(payload)

    ad9_reasons = []
    if dec_ad9['outcome'] != REQUIRED_OUTCOME_B:
        ad9_reasons.append('authority_outcome_refused')
    if dec_ad9['scope_id'] != QUERY_SCOPE_B:
        ad9_reasons.append('scope_mismatch')
    excluded.append({
        'decision_id': dec_ad9['decision_id'],
        'assertion_id': None,
        'semantic_force': dec_ad9['semantic_force'],
        'scope_id': dec_ad9['scope_id'],
        'authority_id': dec_ad9['authority_id'],
        'authority_status': dec_ad9['outcome'],
        'reason': dec_ad9['reason'],
        'effective_from': dec_ad9['effective_from'],
        'recorded_at': dec_ad9['recorded_at'],
        'declared_loss': 0,
        'reasons': ad9_reasons,
    })

    status_label = 'QUALIFIED_RESULT' if qualified else 'NO_QUALIFIED_RESULT'
    return {
        'qualified': qualified,
        'excluded': excluded,
        'qualified_assertion_ids': [q['assertion_id'] for q in qualified],
        'qualified_decision_ids': [],
        'status': status_label,
        'dec_ad9_recovered': True,
        'dec_ad9_outcome': dec_ad9['outcome'],
        'alpha_revision_recovered': True,
        'alpha_revision_reason': alpha_rev['reason'],
    }


def qualify_fixture_c(conn, s3_candidates, query_as_of):
    qualified = []
    excluded = []

    pos = require_row(
        conn,
        """
        SELECT decision_id, outcome, semantic_force, scope_id, effective_from,
               authority_id, reason, recorded_at
        FROM authority_decision WHERE decision_id = 'dec:pos-1'
        """,
        (),
        'dec:pos-1',
    )
    if pos is None:
        return None

    for candidate in s3_candidates:
        decision_id = candidate['decision_id']
        row = require_row(
            conn,
            """
            SELECT decision_id, outcome, semantic_force, scope_id, effective_from,
                   authority_id, reason, recorded_at
            FROM authority_decision WHERE decision_id = ?
            """,
            (decision_id,),
            decision_id,
        )
        if row is None:
            return None

        reasons = []
        if row['scope_id'] != QUERY_SCOPE_C:
            reasons.append('scope_mismatch')
        if row['outcome'] != REQUIRED_OUTCOME_C:
            reasons.append(f"outcome_{row['outcome']}")
        if row['effective_from'] > query_as_of:
            reasons.append('not_yet_effective')

        payload = {
            'decision_id': row['decision_id'],
            'outcome': row['outcome'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'authority_id': row['authority_id'],
            'reason': row['reason'] if row['reason'] else UNKNOWN,
            'effective_from': row['effective_from'],
            'recorded_at': row['recorded_at'],
            'subject': 'ent:service:orion',
            'currentness': True,
            'reasons': reasons,
        }
        if reasons:
            excluded.append(payload)
        else:
            qualified.append(payload)

    status_label = 'QUALIFIED_RESULT' if qualified else 'NO_QUALIFIED_RESULT'
    return {
        'qualified': qualified,
        'excluded': excluded,
        'qualified_decision_ids': [q['decision_id'] for q in qualified],
        'status': status_label,
    }


def run_s4(db_path, s3_path='s3_output.json', output_path='s4_output.json',
           query_as_of=None):
    if query_as_of is None:
        query_as_of = os.environ.get('SEMREV_QUERY_AS_OF', QUERY_AS_OF_DEFAULT)
    conn = connect(db_path, must_exist=True)
    try:
        s3_result = load_s3(s3_path)
        fixture_a = qualify_fixture_a(conn, s3_result['fixture_a'], query_as_of)
        fixture_b = qualify_fixture_b(conn, s3_result['fixture_b'], query_as_of)
        fixture_c = qualify_fixture_c(conn, s3_result['fixture_c'], query_as_of)
        if fixture_a is None or fixture_b is None or fixture_c is None:
            print('S4 QUALIFY: FAIL - Missing required dependencies')
            return None
        s4_result = {
            'fixture_a': fixture_a,
            'fixture_b': fixture_b,
            'fixture_c': fixture_c,
            'query_as_of': query_as_of,
        }
        print('S4 QUALIFY: Fixture A current_path:', fixture_a['current_path'])
        print('S4 QUALIFY: Fixture B status:', fixture_b['status'])
        print(
            'S4 QUALIFY: Fixture B excluded:',
            [e.get('assertion_id') or e.get('decision_id') for e in fixture_b['excluded']],
        )
        print('S4 QUALIFY: Fixture C qualified:', fixture_c['qualified_decision_ids'])
        print('S4 QUALIFY: dec:ad-9 recovered:', fixture_b['dec_ad9_recovered'])
        print('S4 QUALIFY: SUCCESS')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(s4_result, f, indent=2)
            f.write('\n')
        return s4_result
    finally:
        conn.close()


def main():
    print('S4 QUALIFY: Starting...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        result = run_s4(db_path)
        if result is None:
            sys.exit(1)
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S4 QUALIFY: ERROR - {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
