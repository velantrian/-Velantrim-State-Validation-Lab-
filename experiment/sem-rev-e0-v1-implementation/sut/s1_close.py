#!/usr/bin/env python3
"""
S1 CLOSE - Commit, close connections, terminate process
FROZEN SPEC: SEM-REV-E0 v1
"""

import sqlite3
import os
import sys

DB_PATH = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')


def main():
    print('S1 CLOSE: Starting...')

    if DB_PATH == ':memory:' or 'memory' in DB_PATH.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    conn = sqlite3.connect(DB_PATH)
    conn.execute('PRAGMA foreign_keys = ON')

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

    try:
        conn.commit()
        conn.close()

        print('S1 CLOSE: Database committed and connections closed')
        print('S1 CLOSE: SUCCESS')

    except Exception as e:
        print(f'S1 CLOSE: ERROR - {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
