#!/usr/bin/env python3
"""
S5 STRUCTURED PROJECTION
FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION_TEST_ONLY

Writes exact output bytes, then hashes those exact written bytes.
Oracle / scorer MUST NOT run before the hash file exists.
"""

import hashlib
import json
import os
import sys

from runtime import connect, fail_exit, RuntimeGuardError


def write_exact(path, payload):
    text = json.dumps(payload, sort_keys=True, indent=2) + '\n'
    data = text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(data)
    return data


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def run_s5(db_path, s4_path='s4_output.json', output_path='s5_output.json',
           hash_path='s5_output.sha256'):
    conn = connect(db_path, must_exist=True)
    try:
        with open(s4_path, 'r', encoding='utf-8') as f:
            s4_result = json.load(f)

        # Normative projection is path-independent (no temp/runtime paths).
        projection = {
            's5_projection': {
                'fixture_a': s4_result.get('fixture_a', {}),
                'fixture_b': s4_result.get('fixture_b', {}),
                'fixture_c': s4_result.get('fixture_c', {}),
                'query_as_of': s4_result.get('query_as_of'),
            }
        }

        output_bytes = write_exact(output_path, projection)
        with open(output_path, 'rb') as f:
            on_disk = f.read()
        if on_disk != output_bytes:
            print('ERROR: S5 written bytes differ from in-memory payload')
            return None
        digest = sha256_bytes(on_disk)
        with open(hash_path, 'w', encoding='utf-8', newline='\n') as f:
            f.write(f'{digest}  {os.path.basename(output_path)}\n')

        print(f'S5 PROJECT: Output written to {output_path}')
        print(f'S5 PROJECT: SHA-256: {digest}')
        print('S5 PROJECT: SUCCESS')
        print('S5 PROJECT: Scoring harness may now access oracle')
        return {
            'projection': projection,
            'sha256': digest,
            'output_path': output_path,
            'hash_path': hash_path,
            'byte_count': len(on_disk),
        }
    finally:
        conn.close()


def main():
    print('S5 PROJECT: Starting...')
    db_path = os.environ.get('SEMREV_DB_PATH', 'semrev_e0.db')
    try:
        result = run_s5(db_path)
        if result is None:
            sys.exit(1)
    except RuntimeGuardError as e:
        fail_exit(e)
    except Exception as e:
        print(f'S5 PROJECT: ERROR - {e}')
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
