# SEM-REV-E1 — PASS / FAIL / INCOMPLETE Rules (C1+C11)

**STATUS:** preregistration candidate · NOT FROZEN

---

## Final CORE labels (only)

```text
SEM_REV_E1_CORE_PASS
SEM_REV_E1_CORE_FAIL
SEM_REV_E1_CORE_INCOMPLETE
```

Do not invent other scientific CORE labels.

---

## Fixture-level vocabulary (C11)

| Term | Meaning |
|------|---------|
| `FIXTURE_SEMANTIC_PASS` | Preregistered semantic expectation met |
| `FIXTURE_SEMANTIC_FAIL` | Preregistered semantic expectation missed / forbidden atom hit |
| `FIXTURE_EXPECTED_FAIL_CLOSED` | Fixture intentionally expects S4 fail-closed (E1-F-01) |
| `EXECUTION_INTEGRITY_FAILURE` | Crash, missing artifacts, oracle leak, hash mismatch, suite abort |

Alias retained from C1: `FIXTURE_EXPECTATION = PASS` ≡ `FIXTURE_SEMANTIC_PASS`.

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ordinary NO_QUALIFIED_RESULT
```

### E1-F-01

- exact S4 fail-closed → `FIXTURE_SEMANTIC_PASS`
- silent ordinary `NO_QUALIFIED_RESULT` / valid-absence path → `FIXTURE_SEMANTIC_FAIL` (+ HF-06)
- unrelated crash / missing evidence → `EXECUTION_INTEGRITY_FAILURE`

Expected fail-closed does **not** prohibit `SEM_REV_E1_CORE_PASS` and must not
abort independent processing of remaining CORE fixtures. F-01 is not required
to emit S5.

---

## SEM_REV_E1_CORE_PASS requires ALL of

1. All **physical CORE** fixtures (+ required role/check entries) processed
   independently under the authorized future execution protocol;
2. All positive-control physical fixtures + required positive role tags PASS;
3. `HARD_FAIL_COUNT = 0`;
4. No required atom missing;
5. No forbidden atom present;
6. Dependency integrity preserved (F-01 contributes PASS only on exact fail-closed);
7. Oracle isolation preserved;
8. S5 hash integrity for every CORE fixture preregistered to emit S5
   (F-01 excluded);
9. `FIXTURE_SEMANTIC_PASS` on every physical CORE fixture and required
   role/check entry.

**No majority-pass.**

NX cases are **not** CORE oracles and must not be used to manufacture PASS.

---

## SEM_REV_E1_CORE_FAIL

A preregistered semantic failure and/or hard fail occurs under sufficient
execution integrity to classify (including positive-control failure and
forbidden-atom hits; including F-01 converted to ordinary valid absence).

---

## SEM_REV_E1_CORE_INCOMPLETE

`EXECUTION_INTEGRITY_FAILURE` prevents valid classification:

- pre-run integrity gate fail;
- S5 hash mismatch on a fixture required to emit S5;
- oracle accessible before evidence fixed;
- missing artifacts;
- stop conditions that abort before CORE suite completion.

Do **not** upgrade INCOMPLETE → PASS by interpretation.

---

## Non-CORE boundary cases

`NOT EXPRESSIBLE UNDER CURRENT CONTRACT` cases (`E1-E-NX`, `E1-G-NX`) are not
scored as CORE PASS/FAIL oracles.
