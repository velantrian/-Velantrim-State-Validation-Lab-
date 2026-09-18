# E1-F — Required Dependency Loss vs Optional UNKNOWN

**Family:** E1-F  
**Hypotheses:** H5, H9  
**PHYSICAL_CORE:** E1-F-01, E1-F-02  
**Taxonomy:** `CONTRAST_GROUP` **CG-F-dep** (NOT TRUE_PAIRWISE — more than one material semantic Δ)

---

## Purpose

```text
UNKNOWN ≠ FALSE
DEPENDENCY LOSS ≠ VALID ABSENCE
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
```

`declared_loss`: INTEGER `0`/`1` only.  
UNKNOWN-discipline via optional `uncertainty` NULL → UNKNOWN.

---

## E1-F-01 — Required dependency missing (EXPECTED FAIL-CLOSED)

World: candidate `as:e1f-cand` requires typed dependency `dec:e1f-auth`; dependency
**absent**; candidate in S3 set; `declared_loss=0`.

### Immutable S4 hash gate (before oracle)

```text
S4 fail-closed status/output artifact fixed
→ exact bytes recorded
→ SHA-256 recorded
→ SHA-256 independently verified
→ THEN oracle/scorer may inspect expected outcome
```

If S4 evidence cannot be fixed and hashed → suite `SEM_REV_E1_CORE_INCOMPLETE`.

```text
FIXTURE_EXPECTED_FAIL_CLOSED
S4 = FAIL
S4_OUTPUT_SHA256 verified = YES required before oracle
FIXTURE_SEMANTIC_PASS iff exact fail-closed after hash gate
must_not_emit_silent_NO_QUALIFIED_RESULT_as_valid_absence
does_not_prohibit_CORE_PASS
S5_not_required
```

---

## E1-F-02 — Optional uncertainty absent → UNKNOWN (NEG)

`dec:e1f-opt` approved; production-us; `declared_loss=0`; `uncertainty` NULL → UNKNOWN.

```text
optional uncertainty=UNKNOWN
must_not_fabricate_FALSE_or_concrete_value
may QUALIFIED_RESULT if required gates pass
FIXTURE_SEMANTIC_PASS when atoms match
```

### Why not TRUE_PAIRWISE

F-01 varies required-dependency presence + expected stage outcome class
(fail-closed). F-02 varies optional uncertainty presence under an otherwise
qualifying decision. Multiple material deltas → **CONTRAST_GROUP**, not
TRUE_PAIRWISE.
