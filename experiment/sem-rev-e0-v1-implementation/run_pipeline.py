#!/usr/bin/env python3
"""
SEM-REV-E0 v1 Implementation Pipeline
FROZEN SPEC: SEM-REV-E0 v1

This script runs the complete S0-S5 pipeline for implementation testing.
It does NOT execute the scientific experiment.
"""

import subprocess
import os
import sys
import tempfile
import shutil


def run_stage(stage, db_path, impl_root, env=None):
    """Run a pipeline stage with correct path resolution"""
    script = os.path.join(impl_root, 'sut', f'{stage}.py')
    if not os.path.exists(script):
        print(f'ERROR: Script {script} not found')
        return False
    
    cmd = [sys.executable, script]
    
    if env is None:
        env = os.environ.copy()
    env['SEMREV_DB_PATH'] = db_path
    env['SEMREV_QUERY_AS_OF'] = '2026-02-01T00:00:00Z'
    
    # Set PYTHONPATH to include implementation root
    env['PYTHONPATH'] = impl_root
    
    result = subprocess.run(
        cmd,
        env=env,
        capture_output=True,
        text=True,
        cwd=os.path.dirname(db_path)  # Run in DB directory for file outputs
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
    
    # Implementation root is the directory containing this script
    impl_root = os.path.dirname(os.path.abspath(__file__))
    
    # Use a temporary directory for the database and outputs
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, 'semrev_e0.db')
    
    # Copy schema.sql to temp dir
    schema_src = os.path.join(impl_root, 'schema.sql')
    schema_dst = os.path.join(temp_dir, 'schema.sql')
    shutil.copy(schema_src, schema_dst)
    
    original_dir = os.getcwd()
    
    try:
        os.chdir(temp_dir)
        
        # Run S0
        print('\nRunning S0 WRITE...')
        if not run_stage('s0_write', db_path, impl_root):
            print('S0 FAILED')
            sys.exit(1)
        
        # Run S1
        print('\nRunning S1 CLOSE...')
        if not run_stage('s1_close', db_path, impl_root):
            print('S1 FAILED')
            sys.exit(1)
        
        # Run S2 (new process)
        print('\nRunning S2 REOPEN...')
        if not run_stage('s2_reopen', db_path, impl_root):
            print('S2 FAILED')
            sys.exit(1)
        
        # Run S3
        print('\nRunning S3 RETRIEVE...')
        if not run_stage('s3_retrieve', db_path, impl_root):
            print('S3 FAILED')
            sys.exit(1)
        
        # Run S4
        print('\nRunning S4 QUALIFY...')
        if not run_stage('s4_qualify', db_path, impl_root):
            print('S4 FAILED')
            sys.exit(1)
        
        # Run S5
        print('\nRunning S5 PROJECT...')
        if not run_stage('s5_project', db_path, impl_root):
            print('S5 FAILED')
            sys.exit(1)
        
        # Run scoring harness
        print('\nRunning Scoring Harness...')
        scorer_path = os.path.join(impl_root, 'harness', 'scorer.py')
        result = subprocess.run(
            [sys.executable, scorer_path],
            env=os.environ.copy(),
            capture_output=True,
            text=True,
            cwd=temp_dir
        )
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        
        print('\n' + '=' * 60)
        print('Pipeline Complete')
        print('IMPLEMENTATION_TEST_ONLY - NOT EXPERIMENTAL EVIDENCE')
        
    finally:
        os.chdir(original_dir)


if __name__ == '__main__':
    main()
