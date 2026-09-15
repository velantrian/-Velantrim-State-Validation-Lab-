# SEM-REV-E1 — PASS / FAIL / INCOMPLETE Rules

**STATUS:** preregistration candidate · NOT FROZEN

---

## Allowed CORE labels

```text
SEM_REV_E1_CORE_PASS
SEM_REV_E1_CORE_FAIL
SEM_REV_E1_CORE_INCOMPLETE
```

Do not invent other scientific CORE labels.

---

## Per-fixture vs CORE classification

CORE labels classify the **suite**. They are not identical to a stage exit code.

Each CORE fixture also has:

```text
FIXTURE_EXPECTATION = PASS | FAIL
```

### A. EXPECTED FIXTURE GUARD TRIGGER

E1-F-01 is a negative-control guard:

- required typed qualification dependency is **intentionally absent**;
- the exact preregistered outcome is **S4 fail-closed** (`S4 = FAIL`);
- this is **not** ordinary `NO_QUALIFIED_RESULT` as valid absence.

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ordinary NO_QUALIFIED_RESULT
```

`FIXTURE_EXPECTATION = PASS` **if and only if** the system produces that exact
fail-closed outcome (S4 FAIL; no silent conversion to a qualified or
`NO_QUALIFIED_RESULT` success path).

An expected fail-closed on E1-F-01:

- does **not** by itself make `SEM_REV_E1_CORE_FAIL`;
- does **not** prohibit `SEM_REV_E1_CORE_PASS`;
- does **not** make the suite `INCOMPLETE`;
- must **not** abort independent processing of remaining CORE fixtures.

E1-F-01 is **not** required to produce S5. S5 hash integrity applies only to
fixtures preregistered to emit S5.

### B. UNEXPECTED PIPELINE / EXECUTION FAILURE

The following remain FAIL or INCOMPLETE under the CORE rules:

- S4 FAIL / abort on a fixture whose preregistered expectation is S4 PASS and S5;
- crash, integrity-gate failure, oracle leakage, S5 hash mismatch on a fixture
  that must emit S5;
- suite abort that prevents independent processing of remaining CORE fixtures;
- missing artifacts preventing adjudication.

Do **not** treat unexpected execution failure as an expected guard trigger.

---

## SEM_REV_E1_CORE_PASS requires ALL of

1. All preregistered **CORE** E1 fixtures processed **independently** under the
   authorized execution protocol (future task), including fixtures whose
   preregistered expectation is fail-closed at S4;
2. All positive controls PASS;
3. `HARD_FAIL_COUNT = 0`;
4. No required atom missing (for E1-F-01: the required atoms are the fail-closed
   guard atoms, not a qualified projection);
5. No forbidden atom present;
6. Dependency integrity preserved (required-dep loss ≠ valid absence);
   E1-F-01 contributes PASS when fail-closed is exact, FAIL if loss is silently
   converted to a valid result / ordinary `NO_QUALIFIED_RESULT`;
7. Oracle isolation preserved;
8. S5 hash integrity holds for every CORE fixture preregistered to produce S5
   (E1-F-01 is excluded from this S5 requirement);
9. `FIXTURE_EXPECTATION = PASS` on every CORE fixture, including E1-F-01’s
   expected fail-closed.

**No majority-pass.** Example prohibited: “21/22 fixtures passed → PASS”.

If any CORE hard fail occurs → `CORE_PASS` prohibited.

Expected S4 fail-closed on E1-F-01 is **not** a CORE hard fail.

---

## SEM_REV_E1_CORE_FAIL

A preregistered semantic failure and/or hard fail occurs under sufficient
execution integrity to classify.

Includes positive-control failure and forbidden-atom hits.

---

## SEM_REV_E1_CORE_INCOMPLETE

Execution integrity is insufficient to classify:

- pre-run integrity gate fail;
- S5 hash mismatch;
- oracle accessible before S5 hash;
- missing artifacts preventing adjudication;
- stop conditions that abort before CORE suite completion.

Do **not** upgrade INCOMPLETE → PASS by interpretation.

---

## Non-CORE boundary cases

`NOT EXPRESSIBLE UNDER CURRENT CONTRACT` cases (e.g. E1-E-NX) are **not**
scored as CORE PASS/FAIL oracles. They document design boundaries. Their
presence/absence must not be used to manufacture CORE_PASS.
