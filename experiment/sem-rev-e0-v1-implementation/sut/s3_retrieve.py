#!/usr/bin/env python3
"""
S3 RETRIEVE - Recover candidate identities
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY

Fixture B candidates are assertions only (alpha + beta).
dec:ad-9 is a qualification dependency, NOT an S3 candidate.
Fixture C candidate is dec:pos-1.
Fixture A candidates are Path-A/B/C assertions.
"""

import json
import os
import sys

from runtime import connect, fail_exit, RuntimeGuardError


def retrieve_fixture_a_candidates(conn):
    cursor = conn.execute(
        """
        SELECT assertion_id, semantic_force, scope_id, content, reason,
               reopen_requires, valid_from, valid_to
        FROM assertion
        WHERE entity_id = 'ent:project:delta'
        ORDER BY assertion_id
        """
    )
    candidates = []
    for row in cursor.fetchall():
        candidates.append({
            'assertion_id': row['assertion_id'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'content': row['content'],
            'reason': row['reason'],
            'reopen_requires': row['reopen_requires'],
            'valid_from': row['valid_from'],
            'valid_to': row['valid_to'],
        })
    ids = [c['assertion_id'] for c in candidates]
    for required in ('as:path-a-v1', 'as:path-b-v1', 'as:path-c-v1'):
        if required not in ids:
            print(f'ERROR: Fixture A missing {required}')
            return None
    return candidates


def retrieve_fixture_b_candidates(conn):
    cursor = conn.execute(
        """
        SELECT assertion_id, semantic_force, scope_id, valid_from, valid_to,
               uncertainty, declared_loss, recorded_at
        FROM assertion
        WHERE entity_id = 'ent:service:atlas'
        ORDER BY assertion_id
        """
    )
    candidates = []
    for row in cursor.fetchall():
        candidates.append({
            'assertion_id': row['assertion_id'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'valid_from': row['valid_from'],
            'valid_to': row['valid_to'],
            'uncertainty': row['uncertainty'],
            'declared_loss': int(row['declared_loss']),
            'recorded_at': row['recorded_at'],
        })
    ids = [c['assertion_id'] for c in candidates]
    if 'as:alpha-v1' not in ids:
        print('ERROR: Fixture B missing as:alpha-v1')
        return None
    if 'as:beta-v1' not in ids:
        print('ERROR: Fixture B missing as:beta-v1')
        return None
    return candidates


def retrieve_fixture_c_candidates(conn):
    cursor = conn.execute(
        """
        SELECT decision_id, outcome, semantic_force, scope_id, effective_from,
               authority_id, reason, recorded_at
        FROM authority_decision
        WHERE decision_id = 'dec:pos-1'
        """
    )
    candidates = []
    for row in cursor.fetchall():
        candidates.append({
            'decision_id': row['decision_id'],
            'outcome': row['outcome'],
            'semantic_force': row['semantic_force'],
            'scope_id': row['scope_id'],
            'effective_from': row['effective_from'],
            'authority_id': row['authority_id'],
            'reason': row['reason'],
            'recorded_at': row['recorded_at'],
        })
    ids = [c['decision_id'] for c in candidates]
    if 'dec:pos-1' not in ids:
        print('ERROR: Fixture C missing dec:pos-1')
        return None
    return candidates


def run_s3(db_path, output_path='s3_output.json'):
    conn = connect(db_path, must_exist=True)
    try:
        fixture_a = retrieve_fixture_a_candidates(conn)
        fixture_b = retrieve_fixture_b_candidates(conn)
        fixture_c = retrieve_fixture_c_candidates(conn)
        if fixture_a is None or fixture_b is None or fixture_c is None:
            print('S3 RETRIEVE: FAIL')
            return None
        s3_result = {
            'fixture_a': fixture_a,
            'fixture_b': fixture_b,
            'fixture_c': fixture_c,
        }
        print('S3 RETRIEVE: Fixture A candidates:', [c['assertion_id'] for c in fixture_a])
        print('S3 RETRIEVE: Fixture B candidates:', [c['assertion_id'] for c in fixture_b])
        print('S3 RETRIEVE: Fixture C candidates:', [c['decision_id'] for c in fixture_c])
        print('S3 RETRIEVE: SUCCESS')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(s3_result, f, indent=2)
            f.write('\n')
        return s3_result
    finally:
        conn.close()


def main():
    print('S3 RETRIEVE: Starting...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        result = run_s3(db_path)
        if result is None:
            sys.exit(1)
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S3 RETRIEVE: ERROR - {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
