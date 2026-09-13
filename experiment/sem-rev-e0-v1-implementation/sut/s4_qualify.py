#!/usr/bin/env python3
"""
S4 DETERMINISTIC QUALIFICATION
FROZEN SPEC: SEM-REV-E0 v1
"""

import sqlite3
import os
import sys
import json
from datetime import datetime, timezone

DB_PATH = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
QUERY_AS_OF = os.environ.get('SEMREV_QUERY_AS_OF', '2026-02-01T00:00:00Z')


def get_connection(db_path=DB_PATH):
    conn = sqlite3.connect(db_path)
    conn.execute('PRAGMA foreign_keys = ON')
    conn.execute('PRAGMA journal_mode = WAL')

    version = conn.execute('SELECT sqlite_version()').fetchone()[0]
    if version != '3.53.4':
        print(f'ERROR: SQLite version mismatch. Expected 3.53.4, got {version}')
        conn.close()
        sys.exit(1)

    source_id = conn.execute('SELECT sqlite_source_id()').fetchone()[0]
    expected_source_id = '2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc'
    if source_id != expected_source_id:
        print('ERROR: SQLite source ID mismatch')
        conn.close()
        sys.exit(1)

    return conn


def is_current(conn, assertion_id, query_as_of):
    cursor = conn.execute("""
        SELECT valid_from, valid_to FROM assertion WHERE assertion_id = ?
    """, (assertion_id,))
    row = cursor.fetchone()

    if row is None:
        return False

    valid_from = row[0]
    valid_to = row[1]

    if valid_from and valid_from > query_as_of:
        return False

    if valid_to and valid_to <= query_as_of:
        return False

    cursor = conn.execute("""
        SELECT revision_type, effective_from
        FROM revision
        WHERE target_assertion_id = ?
        AND effective_from <= ?
    """, (assertion_id, query_as_of))

    for rev_row in cursor.fetchall():
        rev_type = rev_row[0]
        effective_from = rev_row[1]
        if effective_from <= query_as_of:
            return False

    return True


def get_authority_outcome(conn, scope_id, query_as_of):
    cursor = conn.execute("""
        SELECT decision_id, outcome, effective_from
        FROM authority_decision
        WHERE scope_id = ?
        AND effective_from <= ?
        ORDER BY effective_from DESC
        LIMIT 1
    """, (scope_id, query_as_of))

    row = cursor.fetchone()
    if row:
        return {
            'decision_id': row[0],
            'outcome': row[1],
            'effective_from': row[2]
        }
    return None


def qualify_fixture_b(conn, s3_candidates, query_as_of):
    query_scope = 'scope:production-us'
    allowed_forces = ['observation', 'authority_decision']
    required_outcome = 'approved'

    qualified = []
    excluded = []

    for candidate in s3_candidates:
        assertion_id = candidate['assertion_id']

        cursor = conn.execute("""
            SELECT entity_id, semantic_force, scope_id, valid_from, valid_to,
                   uncertainty, declared_loss
            FROM assertion
            WHERE assertion_id = ?
        """, (assertion_id,))
        row = cursor.fetchone()

        if row is None:
            print(f'ERROR: Assertion {assertion_id} not found')
            return None

        semantic_force = row[1]
        scope_id = row[2]
        uncertainty = row[5]
        declared_loss = row[6]

        if scope_id != query_scope:
            excluded.append({'assertion_id': assertion_id, 'reason': 'scope_mismatch'})
            continue

        if semantic_force not in allowed_forces:
            excluded.append({'assertion_id': assertion_id, 'reason': 'force_not_allowed'})
            continue

        if not is_current(conn, assertion_id, query_as_of):
            excluded.append({'assertion_id': assertion_id, 'reason': 'not_current'})
            continue

        auth_outcome = get_authority_outcome(conn, query_scope, query_as_of)
        if auth_outcome is None:
            excluded.append({'assertion_id': assertion_id, 'reason': 'no_authority_decision'})
            continue

        if auth_outcome['outcome'] != required_outcome:
            excluded.append({'assertion_id': assertion_id, 'reason': f'authority_outcome_{auth_outcome["outcome"]}'})
            continue

        qualified.append({
            'assertion_id': assertion_id,
            'semantic_force': semantic_force,
            'scope_id': scope_id,
            'currentness': True,
            'authority_status': auth_outcome['outcome'],
            'uncertainty': uncertainty,
            'declared_loss': declared_loss
        })

    cursor = conn.execute("""
        SELECT decision_id, outcome, effective_from
        FROM authority_decision
        WHERE decision_id = 'dec:ad-9'
    """)
    dec_ad9 = cursor.fetchone()

    if dec_ad9 is None:
        print('ERROR: dec:ad-9 cannot be recovered - S4 FAIL')
        return None

    return {
        'qualified': qualified,
        'excluded': excluded,
        'dec_ad9_recovered': True,
        'dec_ad9_outcome': dec_ad9[1]
    }


def qualify_fixture_c(conn, s3_candidates, query_as_of):
    query_scope = 'scope:production-eu'
    required_outcome = 'approved'

    qualified = []
    excluded = []

    for candidate in s3_candidates:
        decision_id = candidate['decision_id']

        cursor = conn.execute("""
            SELECT outcome, semantic_force, scope_id, effective_from
            FROM authority_decision
            WHERE decision_id = ?
        """, (decision_id,))
        row = cursor.fetchone()

        if row is None:
            print(f'ERROR: Decision {decision_id} not found')
            return None

        outcome = row[0]
        semantic_force = row[1]
        scope_id = row[2]
        effective_from = row[3]

        if scope_id != query_scope:
            excluded.append({'decision_id': decision_id, 'reason': 'scope_mismatch'})
            continue

        if outcome != required_outcome:
            excluded.append({'decision_id': decision_id, 'reason': f'outcome_{outcome}'})
            continue

        if effective_from > query_as_of:
            excluded.append({'decision_id': decision_id, 'reason': 'not_yet_effective'})
            continue

        qualified.append({
            'decision_id': decision_id,
            'outcome': outcome,
            'semantic_force': semantic_force,
            'scope_id': scope_id,
            'currentness': True
        })

    return {'qualified': qualified, 'excluded': excluded}


def main():
    print('S4 QUALIFY: Starting...')

    if DB_PATH == ':memory:' or 'memory' in DB_PATH.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    if not os.path.exists(DB_PATH):
        print(f'ERROR: Database file not found at {DB_PATH}')
        sys.exit(1)

    conn = get_connection(DB_PATH)

    try:
        with open('s3_output.json', 'r') as f:
            s3_result = json.load(f)

        fixture_b_result = qualify_fixture_b(conn, s3_result['fixture_b'], QUERY_AS_OF)
        fixture_c_result = qualify_fixture_c(conn, s3_result['fixture_c'], QUERY_AS_OF)

        if fixture_b_result is None or fixture_c_result is None:
            print('S4 QUALIFY: FAIL - Missing required dependencies')
            sys.exit(1)

        s4_result = {
            'fixture_b': fixture_b_result,
            'fixture_c': fixture_c_result
        }

        print('S4 QUALIFY: Fixture B qualified:', [q['assertion_id'] for q in fixture_b_result['qualified']])
        print('S4 QUALIFY: Fixture B excluded:', [e['assertion_id'] for e in fixture_b_result['excluded']])
        print('S4 QUALIFY: Fixture C qualified:', [q['decision_id'] for q in fixture_c_result['qualified']])
        print('S4 QUALIFY: Fixture C excluded:', [e['decision_id'] for e in fixture_c_result['excluded']])
        print('S4 QUALIFY: dec:ad-9 recovered:', fixture_b_result['dec_ad9_recovered'])
        print('S4 QUALIFY: SUCCESS')

        with open('s4_output.json', 'w') as f:
            json.dump(s4_result, f, indent=2)

        conn.close()

    except Exception as e:
        print(f'S4 QUALIFY: ERROR - {e}')
        import traceback
        traceback.print_exc()
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
