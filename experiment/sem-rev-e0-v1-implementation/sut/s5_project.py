#!/usr/bin/env python3
"""
S5 STRUCTURED PROJECTION
FROZEN SPEC: SEM-REV-E0 v1
"""

import sqlite3
import os
import sys
import json
import hashlib
from datetime import datetime, timezone

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


def compute_sha256(data):
    if isinstance(data, dict) or isinstance(data, list):
        data = json.dumps(data, sort_keys=True, indent=2)
    return hashlib.sha256(data.encode('utf-8')).hexdigest()


def main():
    print('S5 PROJECT: Starting...')

    if DB_PATH == ':memory:' or 'memory' in DB_PATH.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    if not os.path.exists(DB_PATH):
        print(f'ERROR: Database file not found at {DB_PATH}')
        sys.exit(1)

    conn = get_connection(DB_PATH)

    try:
        with open('s4_output.json', 'r') as f:
            s4_result = json.load(f)

        projection = {
            's5_projection': {
                'fixture_b': s4_result['fixture_b'],
                'fixture_c': s4_result['fixture_c'],
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'database_path': DB_PATH
            }
        }

        output_bytes = json.dumps(projection, sort_keys=True, indent=2).encode('utf-8')
        output_path = 's5_output.json'
        with open(output_path, 'wb') as f:
            f.write(output_bytes)

        sha256_hash = compute_sha256(output_bytes)

        hash_path = 's5_output.sha256'
        with open(hash_path, 'w') as f:
            f.write(f'{sha256_hash}  {output_path}\n')

        print(f'S5 PROJECT: Output written to {output_path}')
        print(f'S5 PROJECT: SHA-256: {sha256_hash}')
        print('S5 PROJECT: SUCCESS')
        print('S5 PROJECT: Scoring harness may now access oracle')

        conn.close()

    except Exception as e:
        print(f'S5 PROJECT: ERROR - {e}')
        import traceback
        traceback.print_exc()
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
