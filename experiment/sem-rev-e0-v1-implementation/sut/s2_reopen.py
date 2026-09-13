#!/usr/bin/env python3
"""
S2 NEW-PROCESS REOPEN - Reopen database in new OS process
FROZEN SPEC: SEM-REV-E0 v1
"""

import sqlite3
import os
import sys

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


def main():
    print('S2 REOPEN: Starting in new process...')

    if DB_PATH == ':memory:' or 'memory' in DB_PATH.lower():
        print('ERROR: :memory: database is forbidden')
        sys.exit(1)

    if not os.path.exists(DB_PATH):
        print(f'ERROR: Database file not found at {DB_PATH}')
        sys.exit(1)

    conn = get_connection(DB_PATH)

    try:
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        if len(tables) == 0:
            print('ERROR: No tables found in database')
            conn.close()
            sys.exit(1)

        print(f'S2 REOPEN: Database reopened successfully at {DB_PATH}')
        print(f'S2 REOPEN: Found {len(tables)} tables')
        print('S2 REOPEN: SUCCESS')

        conn.close()

    except Exception as e:
        print(f'S2 REOPEN: ERROR - {e}')
        conn.close()
        sys.exit(1)


if __name__ == '__main__':
    main()
