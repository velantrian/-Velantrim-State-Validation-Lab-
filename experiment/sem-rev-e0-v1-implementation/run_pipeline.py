#!/usr/bin/env python3
"""
SEM-REV-E0 v1 Implementation Pipeline
FROZEN SPEC: SEM-REV-E0 v1

This script runs the complete S0-S5 pipeline for implementation testing.
It does NOT execute the scientific experiment.
"""

import os
import shutil
import subprocess
import sys
import tempfile


def run_stage(stage, db_path, impl_root, env=None):
    """Run a pipeline stage with correct path resolution."""
    script = os.path.join(impl_root, 'sut', f'{stage}.py')
    if not os.path.exists(script):
        print(f'ERROR: Script {script} not found')
        return False

    cmd = [sys.executable, script]
    if env is None:
        env = os.environ.copy()
    env['SEMREV_DB_PATH'] = db_path
    env['SEMREV_QUERY_AS_OF'] = '2026-02-01T00:00:00Z'
    env['PYTHONPATH'] = os.path.join(impl_root, 'sut') + os.pathsep + impl_root

    result = subprocess.run(
        cmd,
        env=env,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(db_path),
    )
    print(f'=== {stage.upper()} OUTPUT ===')
    print(result.stdout)
    if result.stderr:
        print(f'=== {stage.upper()} ERROR ===')
        print(result.stderr)
    return result.returncode == 0


def main():
    print('SEM-REV-E0 v1 Implementation Pipeline')
    print('=' * 60)
    impl_root = os.path.dirname(os.path.abspath(__file__))
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, 'semrev_e0.db')
    shutil.copy(os.path.join(impl_root, 'schema.sql'), os.path.join(temp_dir, 'schema.sql'))
    original_dir = os.getcwd()
    try:
        os.chdir(temp_dir)
        for stage, label in (
            ('s0_write', 'S0 WRITE'),
            ('s1_close', 'S1 CLOSE'),
            ('s2_reopen', 'S2 REOPEN'),
            ('s3_retrieve', 'S3 RETRIEVE'),
            ('s4_qualify', 'S4 QUALIFY'),
            ('s5_project', 'S5 PROJECT'),
        ):
            print(f'\nRunning {label}...')
            if not run_stage(stage, db_path, impl_root):
                print(f'{label} FAILED')
                sys.exit(1)

        print('\nRunning Scoring Harness...')
        scorer_path = os.path.join(impl_root, 'harness', 'scorer.py')
        env = os.environ.copy()
        result = subprocess.run(
            [sys.executable, scorer_path],
            env=env,
            capture_output=True,
            text=True,
            cwd=temp_dir,
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        if result.returncode != 0:
            print('SCORER FAILED')
            sys.exit(1)
        print('\n' + '=' * 60)
        print('Pipeline Complete')
        print('IMPLEMENTATION_TEST_ONLY - NOT EXPERIMENTAL EVIDENCE')
    finally:
        os.chdir(original_dir)


if __name__ == '__main__':
    main()
