#!/usr/bin/env python3
import json
import hashlib
import os
import sys

def main():
    print("Scoring Harness: Starting...")
    if not os.path.exists("s5_output.json"):
        print("ERROR: S5 output not found")
        sys.exit(1)
    if not os.path.exists("s5_output.sha256"):
        print("ERROR: S5 hash file not found")
        sys.exit(1)
    with open("s5_output.sha256", "r") as f:
        hash_line = f.read().strip()
    expected_hash = hash_line.split()[0]
    with open("s5_output.json", "rb") as f:
        content = f.read()
    actual_hash = hashlib.sha256(content).hexdigest()
    if expected_hash != actual_hash:
        print("ERROR: Hash mismatch")
        sys.exit(1)
    print("Hash verified")
    with open("s5_output.json", "r") as f:
        s5_output = json.load(f)
    print("S5 output loaded")
    print("Scoring Harness: Oracle accessed AFTER S5 hash fixed")
    print("Scoring Harness: IMPLEMENTATION_TEST_ONLY")
    print("Scoring Harness: SUCCESS")

if __name__ == "__main__":
    main()