#!/usr/bin/env python3
import subprocess
import os
import sys
import tempfile
import shutil

def run_stage(stage, env=None):
    script = f"sut/{stage}.py"
    if not os.path.exists(script):
        print(f"ERROR: Script {script} not found")
        return False
    cmd = [sys.executable, script]
    if env is None:
        env = os.environ.copy()
    result = subprocess.run(cmd, env=env, capture_output=True, text=True)
    print(f"=== {stage.upper()} OUTPUT ===")
    print(result.stdout)
    if result.stderr:
        print(f"=== {stage.upper()} ERROR ===")
        print(result.stderr)
    return result.returncode == 0

def main():
    print("SEM-REV-E0 v1 Implementation Pipeline")
    print("=" * 60)
    temp_dir = tempfile.mkdtemp()
    db_path = os.path.join(temp_dir, "semrev_e0.db")
    env = os.environ.copy()
    env["SEMREV_DB_PATH"] = db_path
    env["SEMREV_QUERY_AS_OF"] = "2026-02-01T00:00:00Z"
    original_dir = os.getcwd()
    try:
        os.chdir(temp_dir)
        shutil.copy("schema.sql", temp_dir)
        print("Running S0 WRITE...")
        if not run_stage("s0_write", env):
            print("S0 FAILED")
            sys.exit(1)
        print("Running S1 CLOSE...")
        if not run_stage("s1_close", env):
            print("S1 FAILED")
            sys.exit(1)
        print("Running S2 REOPEN...")
        if not run_stage("s2_reopen", env):
            print("S2 FAILED")
            sys.exit(1)
        print("Running S3 RETRIEVE...")
        if not run_stage("s3_retrieve", env):
            print("S3 FAILED")
            sys.exit(1)
        print("Running S4 QUALIFY...")
        if not run_stage("s4_qualify", env):
            print("S4 FAILED")
            sys.exit(1)
        print("Running S5 PROJECT...")
        if not run_stage("s5_project", env):
            print("S5 FAILED")
            sys.exit(1)
        print("Running Scoring Harness...")
        result = subprocess.run([sys.executable, "harness/scorer.py"], env=env, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        print("Pipeline Complete")
        print("IMPLEMENTATION_TEST_ONLY - NOT EXPERIMENTAL EVIDENCE")
    finally:
        os.chdir(original_dir)

if __name__ == "__main__":
    main()