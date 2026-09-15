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

## SEM_REV_E1_CORE_PASS requires ALL of

1. All preregistered **CORE** E1 fixtures processed under authorized execution protocol (future task);
2. All positive controls PASS;
3. `HARD_FAIL_COUNT = 0`;
4. No required atom missing;
5. No forbidden atom present;
6. Dependency integrity preserved (required-dep loss ≠ valid absence);
7. Oracle isolation preserved;
8. S5 hash integrity holds where S5 is in scope of the future execution protocol.

**No majority-pass.** Example prohibited: “21/22 fixtures passed → PASS”.

If any CORE hard fail occurs → `CORE_PASS` prohibited.

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
