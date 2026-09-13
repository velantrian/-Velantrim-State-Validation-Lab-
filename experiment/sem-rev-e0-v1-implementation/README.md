# SEM-REV-E0 v1 Implementation

FROZEN SPEC: SEM-REV-E0 v1
IMPLEMENTATION ONLY: S0-S5 substrate
DATE: 2026-09-13

## Status

- REPO_ACCESS: YES
- FREEZE_INTEGRITY_PRECHECK: PASS
- SOURCE_FREEZE_COMMIT: 349243745ceadea691b9070e08c05e35d876c0ab
- IMPLEMENTATION_BRANCH: experiment/sem-rev-e0-v1-implementation

## Structure

Implementation directory structure:
- sut/ - System Under Test (S0-S5)
  - s0_write.py
  - s1_close.py
  - s2_reopen.py
  - s3_retrieve.py
  - s4_qualify.py
  - s5_project.py
- harness/ - Scoring harness
  - scorer.py
- tests/ - Implementation tests
  - test_implementation.py
- schema.sql
- run_pipeline.py
- README.md

## Implementation Summary

### S0 WRITE
- File-backed SQLite 3.53.4 with STRICT tables
- Explicit PKs, typed mandatory qualifiers
- Foreign keys ON on every connection
- No :memory:, no rowid semantic identity
- No free mutable is_current
- Does NOT persist oracle material

### S1 CLOSE
- Commits transaction, closes connections, terminates process
- No hidden state crosses S1 to S2

### S2 NEW-PROCESS REOPEN
- Runs in NEW OS PROCESS
- Reopens persisted DB only
- No access to oracle material

### S3 RETRIEVE
- Recovers Fixture B: as:alpha-v1, as:beta-v1
- Recovers Fixture C: dec:pos-1
- Dangerous alpha NOT silently dropped

### S4 DETERMINISTIC QUALIFICATION
- Typed lookups only, no LLM/prose parsing
- S3 membership != S4 dependency availability
- dec:ad-9 can bind without being S3 candidate
- Missing dependency -> S4 FAIL
- NOT RETRIEVED != ABSENT
- Currentness derived from typed data

### S5 STRUCTURED PROJECTION
- Writes exact output bytes
- Computes SHA-256
- Fixes output before oracle access
- No backward information flow

## Oracle Isolation

- sut/: S0-S5 implementation only
- harness/: Oracle loading and scoring only
- No imports from harness in sut
- No shared globals or environment variables
- Scoring harness runs AFTER S5 hash is fixed

## SQLite Environment

- Version: 3.53.4
- Source ID: 2026-07-24 19:02:57 bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc
- Guards: Version and source ID checked on every connection

## Running

Run pipeline: python run_pipeline.py
Run tests: python -m pytest tests/test_implementation.py -v

## Notes

- IMPLEMENTATION_TEST_ONLY: All execution is implementation testing, NOT experimental evidence
- NO CORE RESULT: Does NOT produce SEM_REV_E0_CORE_PASS/FAIL/INCOMPLETE
- NO EXPERIMENT EXECUTION: Frozen scientific experiment is NOT executed
- STOP CONDITIONS: Implementation stops if freeze integrity check fails

## Freeze Verification

- Freeze commit: 349243745ceadea691b9070e08c05e35d876c0ab
- Parent commit: b217db3776078d01d6d5411820cb352e9a1bd36b
- Freeze root: docs/research/sem_rev_e0/freeze/v1/
- MANIFEST.json SHA-256: d4974ee709edc9d83018b53733542588469bcbe9cfa5089c39cbb9799eaad49a