# E1-F — Required Dependency Loss vs Optional UNKNOWN

**Family:** E1-F  
**Hypotheses:** H5, H9  
**Physical CORE:** E1-F-01, E1-F-02  
**TRUE_PAIRWISE:** P-F-dep — Δ = required dependency missing vs optional field absent

---

## Purpose

```text
UNKNOWN ≠ FALSE
DEPENDENCY LOSS ≠ VALID ABSENCE
NOT RETRIEVED ≠ ABSENT
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
```

UNKNOWN-discipline uses an **existing optional** property: `uncertainty` NULL →
projects as `UNKNOWN`. Do **not** use `declared_loss=UNKNOWN` (unsupported).

`declared_loss` encoding (E0 schema): INTEGER NOT NULL, `0` = no loss, `1` = loss.

---

## E1-F-01 — Required dependency missing (EXPECTED FAIL-CLOSED)

World:

- Candidate `as:e1f-cand` (observation, scope=production-us, `declared_loss=0`) requires
  typed qualification dependency `dec:e1f-auth` (authority_decision).
- Required dependency **absent** (unrecoverable); candidate present in S3 set.

**Fixture classification (C1/C11):**

```text
FIXTURE_EXPECTED_FAIL_CLOSED
S4 = FAIL
FIXTURE_SEMANTIC_PASS iff exact fail-closed
must_not_emit_silent_NO_QUALIFIED_RESULT_as_valid_absence
does_not_prohibit_CORE_PASS
S5_not_required
```

Unexpected crash / missing artifacts → `EXECUTION_INTEGRITY_FAILURE` → suite INCOMPLETE/FAIL per rules — not a semantic PASS.

---

## E1-F-02 — Optional uncertainty absent → UNKNOWN

World:

- `dec:e1f-opt`: approved authority_decision; production-us; required typed fields present;
  `declared_loss=0`
- `uncertainty` intentionally NULL / unspecified → **UNKNOWN** (existing optional encoding)

**Expected:**

```text
optional uncertainty = UNKNOWN
must_not_fabricate_FALSE_or_concrete_value
may QUALIFIED_RESULT if required gates pass
FIXTURE_SEMANTIC_PASS when atoms match
```
