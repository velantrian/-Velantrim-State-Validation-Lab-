#!/usr/bin/env python3
"""
S3 RETRIEVE - Recover candidate identities
FROZEN SPEC: SEM-REV-E0 v1
"""

import sqlite3
import os
import sys
import json

DB_PATH = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')


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


def retrieve_fixture_b_candidates(conn):
    cursor = conn.execute("""
        SELECT assertion_id, semantic_force, scope_id, valid_from, valid_to
        FROM assertion
        WHERE entity_id = 'ent:service:atlas'
        ORDER BY assertion_id
    """)

    candidates = []
    for row in cursor.fetchall():
        candidates.append({
            'assertion_id': row[0],
            'semantic_force': row[1],
            'scope_id': row[2],
            'valid_from': row[3],
            'valid_to': row[4]
        })

    candidate_ids = [c['assertion_id'] for c in candidates]

    if 'as:alpha-v1' not in candidate_ids:
        print('ERROR: Fixture B missing as:alpha-v1')
        return None

    if 'as:beta-v1' not in candidate_ids:
        print('ERROR: Fixture B missing as:beta-v1')
        return None

    return candidates


def retrieve_fixture_c_candidates(conn):
    cursor = conn.execute("""
        SELECT decision_id, outcome, semantic_force, scope_id, effective_from
        FROM authority_decision
        WHERE decision_id = 'dec:pos-1'
    """)

    candidates = []
    for row in cursor.fetchall():
        candidates.append({
            'decision_id': row[0],
            'outcome': row[1],
            'semantic_force': row[2],
            'scope_id': row[3],
            'effective_from': row[4]
        })

    decision_ids = [c['decision_id'] for c in candidates]

    if 'dec:pos-1' not in decision_ids:
        print('ERROR: Fixture C missing dec:pos-1')
        return None

    return candidates


def main():
    print('S3 RETRIEVE: Starting...')

    if DB_PATH == ':memory:' or 'memory' in DB_PATH.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    if not os.path.exists(DB_PATH):
        print(f'ERROR: Database file not found at {DB_PATH}')
        sys.exit(1)

    conn = get_connection(DB_PATH)

    try:
        fixture_b_candidates = retrieve_fixture_b_candidates(conn)
        fixture_c_candidates = retrieve_fixture_c_candidates(conn)

        if fixture_b_candidates is None or fixture_c_candidates is None:
            print('S3 RETRIEVE: FAIL')
            sys.exit(1)

        s3_result = {
            'fixture_b': fixture_b_candidates,
            'fixture_c': fixture_c_candidates
        }

        print('S3 RETRIEVE: Fixture B candidates:', [c['assertion_id'] for c in fixture_b_candidates])
        print('S3 RETRIEVE: Fixture C candidates:', [c['decision_id'] for c in fixture_c_candidates])
        print('S3 RETRIEVE: SUCCESS')

        with open('s3_output.json', 'w') as f:
            json.dump(s3_result, f, indent=2)

        conn.close()

    except Exception as e:
        print(f'S3 RETRIEVE: ERROR - {e}')
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
