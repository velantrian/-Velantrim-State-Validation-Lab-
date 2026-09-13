#!/usr/bin/env python3
"""S2 NEW-PROCESS REOPEN - Reopen database in new OS process
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY
"""

import os
import sys

from runtime import connect, fail_exit, RuntimeGuardError


def run_s2(db_path):
    conn = connect(db_path, must_exist=True)
    try:
        tables = conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
        ).fetchall()
        if len(tables) == 0:
            print('ERROR: No tables found in database')
            conn.close()
            sys.exit(1)
        print(f'S2 REOPEN: Database reopened successfully at {db_path}')
        print(f'S2 REOPEN: Found {len(tables)} tables')
        print('S2 REOPEN: SUCCESS')
        return conn
    except Exception:
        conn.close()
        raise


def main():
    print('S2 REOPEN: Starting in new process...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        conn = run_s2(db_path)
        conn.close()
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S2 REOPEN: ERROR - {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
