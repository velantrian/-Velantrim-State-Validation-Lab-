#!/usr/bin/env python3
"""S1 CLOSE - Commit, close connections, terminate process
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY
"""

import os
import sys

from runtime import connect, fail_exit, RuntimeGuardError


def run_s1(db_path):
    conn = connect(db_path, must_exist=True)
    try:
        conn.commit()
        conn.close()
        print('S1 CLOSE: Database committed and connections closed')
        print('S1 CLOSE: SUCCESS')
    except Exception:
        try:
            conn.close()
        except Exception:
            pass
        raise


def main():
    print('S1 CLOSE: Starting...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        run_s1(db_path)
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S1 CLOSE: ERROR - {e}')
        sys.exit(1)


if __name__ == '__main__':
    main()
