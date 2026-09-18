# SEM-REV-E1 — PASS / FAIL / INCOMPLETE (final tightening)

**STATUS:** preregistration candidate · NOT FROZEN

---

## Final CORE labels (only)

```text
SEM_REV_E1_CORE_PASS
SEM_REV_E1_CORE_FAIL
SEM_REV_E1_CORE_INCOMPLETE
```

---

## Fixture-level vocabulary

| Term | Meaning |
|------|---------|
| `FIXTURE_SEMANTIC_PASS` | Preregistered semantic expectation met |
| `FIXTURE_SEMANTIC_FAIL` | Expectation missed / forbidden atom hit |
| `FIXTURE_EXPECTED_FAIL_CLOSED` | Intentionally expects S4 fail-closed (E1-F-01) |
| `EXECUTION_INTEGRITY_FAILURE` | Crash, missing artifacts, oracle leak, hash mismatch, suite abort |

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ordinary NO_QUALIFIED_RESULT
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
```

### E1-F-01 hash gate

1. S4 fail-closed artifact bytes fixed  
2. SHA-256 recorded  
3. SHA-256 independently verified  
4. **Then** oracle may score  

- exact fail-closed after gate → `FIXTURE_SEMANTIC_PASS`  
- ordinary `NO_QUALIFIED_RESULT` / valid-absence path → `FIXTURE_SEMANTIC_FAIL`  
- S4 evidence not fixable/hashable → **CORE `INCOMPLETE`**  
- unrelated crash → `EXECUTION_INTEGRITY_FAILURE`

Expected fail-closed does not prohibit `CORE_PASS` and must not abort independent fixture processing. F-01 does not require S5.

---

## SEM_REV_E1_CORE_PASS requires ALL of

1. All **17 physical CORE** fixtures + required role/check entries processed independently;
2. All positive-control physical fixtures + required positive role tags PASS;
3. `HARD_FAIL_COUNT = 0`;
4. No required atom missing;
5. No forbidden atom present;
6. Dependency integrity preserved (F-01 PASS only on exact fail-closed after hash gate);
7. Oracle isolation preserved (including F-01 S4 hash-before-oracle);
8. S5 hash integrity for every CORE fixture preregistered to emit S5 (F-01 excluded);
9. `FIXTURE_SEMANTIC_PASS` on every physical CORE fixture and required role/check entry.

**No majority-pass.** NX cases are not CORE oracles.

---

## SEM_REV_E1_CORE_FAIL

Preregistered semantic failure and/or hard fail under sufficient integrity
(including F-01 converted to ordinary valid absence; positive-control failure).

---

## SEM_REV_E1_CORE_INCOMPLETE

`EXECUTION_INTEGRITY_FAILURE`, including:

- pre-run integrity gate fail;
- S5 hash mismatch on fixtures required to emit S5;
- **F-01 S4 evidence not fixed/hashed before oracle;**
- oracle accessible before evidence fixed;
- missing artifacts;
- suite abort before CORE completion.

Do not upgrade INCOMPLETE → PASS by interpretation.
