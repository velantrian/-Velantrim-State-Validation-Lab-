# SEM-REV-E1 — Oracle Isolation (Design Boundary)

**STATUS:** preregistration candidate · NOT FROZEN  
**Design only. Do NOT implement in this task.**

---

## Principle

```text
SYSTEM UNDER TEST ≠ ANSWER KEY
```

---

## SUT must not access (before fixture evidence is fixed)

- REQUIRED / FORBIDDEN atoms;
- expected labels / gold outputs;
- hard-fail answer keys;
- equivalent answer-key structures.

---

## Allowed SUT inputs

Only fixture **world-state** records and typed query parameters from registered
E0 families: entity, scope, assertion, evidence (+ links), revision
(`retracts`/`supersedes`/…), authority_decision, uncertainty ids, etc.

No hidden flag records, condition engines, jurisdiction maps, rank orders,
magic currentness fields, or per-fixture answer fields.

---

## Scorer / oracle timing

Default (fixtures that emit S5):

```text
S0 → S1 → S2 → S3 → S4 → S5 → HASH(S5) verified → THEN oracle may run
```

### C1 exception: E1-F-01

Preregistered to stop at **S4 fail-closed**. Not required to emit S5.
Adjudication uses recorded S4 fail-closed evidence.

Remaining CORE fixtures continue independently.

---

## Design-time rule

Oracle atoms authored from the **semantic contract**, not from implementation runs.
No executable scorer in this candidate phase.
