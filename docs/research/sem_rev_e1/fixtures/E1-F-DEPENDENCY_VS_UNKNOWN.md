# E1-F — Required Dependency Loss vs Optional UNKNOWN

**Family:** E1-F  
**Hypotheses:** H5, H9  
**CORE cases:** E1-F-01, E1-F-02  
**Pair:** P-F-dep

---

## Purpose

```text
UNKNOWN ≠ FALSE
DEPENDENCY LOSS ≠ VALID ABSENCE
NOT RETRIEVED ≠ ABSENT
```

---

## E1-F-01 — Required dependency missing (CORE NEG)

World intends:

- Candidate assertion `as:e1f-cand` (observation, scope=production-us) requires
  typed qualification dependency `dec:e1f-auth` (authority_decision) to evaluate
  authorization gate.
- Store is constructed such that **required dependency record is absent**
  (unrecoverable), while candidate is present in S3 set.

**Expected (C1):**

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ordinary NO_QUALIFIED_RESULT
```

- S4 = FAIL (fail-closed) is the **preregistered guard outcome**
- `FIXTURE_EXPECTATION = PASS` **iff** that exact fail-closed occurs
- Must **not** emit silent / ordinary `NO_QUALIFIED_RESULT` as if absence were valid evidence
- Expected fail-closed does **not** prohibit `SEM_REV_E1_CORE_PASS`
- Unexpected pipeline failure on other fixtures, or converting F-01 into a
  valid-absence `NO_QUALIFIED_RESULT`, remains FAIL / INCOMPLETE / hard-fail
  as specified
- Remaining CORE fixtures MUST still be processed independently
- This fixture is **not** required to emit S5

## E1-F-02 — Optional property absent → UNKNOWN (CORE NEG vs fabrication)

World:

- `dec:e1f-opt`: approved authority_decision; production-us; all required typed
  fields present;
- optional field (e.g. non-mandatory uncertainty detail) intentionally unspecified → `UNKNOWN`

**Expected:**

- optional property remains `UNKNOWN`
- must not fabricate FALSE / concrete value
- may still qualify if all **required** gates pass

### Material Δ

F-01 vs F-02: **required dependency missing** vs **optional unspecified**.
