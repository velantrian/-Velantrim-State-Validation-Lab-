# SEM-REV-E1 — Oracle Isolation (Design Boundary)

**STATUS:** preregistration candidate · NOT FROZEN  
**This task designs the boundary only. Do NOT implement.**

---

## Principle

```text
SYSTEM UNDER TEST ≠ ANSWER KEY
```

Inherited from E0 and remaining mandatory for any future E1 execution.

---

## SUT must not access

Before S5 output bytes are fixed and independently hashed:

- REQUIRED atoms;
- FORBIDDEN atoms;
- expected labels / gold outputs;
- hard-fail answer keys;
- equivalent answer-key structures (renamed columns, side channels, env dumps).

---

## Allowed SUT inputs

Only fixture **world-state** records and typed query parameters:

- entity / assertion / decision / revision / evidence records as written into the store;
- `query_scope`, `query_as_of`, and other typed request fields defined by the fixture;
- deterministic qualification rules that are part of the mechanism contract (not the per-fixture oracle).

---

## Scorer / oracle timing

Default (fixtures preregistered to emit S5):

```text
S0 → S1 → S2 → S3 → S4 → S5 → HASH(S5) verified → THEN oracle may run
```

If S5 hash verification fails on a fixture required to emit S5 → that
fixture cannot be classified as PASS; unexpected integrity failure is
`INCOMPLETE` / FAIL per `PASS_FAIL_INCOMPLETE_RULES.md`. Oracle must not
“help” repair.

### C1 exception: expected fail-closed (E1-F-01)

E1-F-01 is preregistered to stop at **S4 fail-closed**. It is not required
to emit S5. Oracle/adjudication for **that fixture** uses the recorded S4
fail-closed evidence (exit status + absence of a valid-absence
`NO_QUALIFIED_RESULT` path).

Remaining CORE fixtures continue independently and keep the default
S5-hash-then-oracle rule.

SUT still must not access oracle atoms before the applicable evidence for
that fixture is fixed.

---

## Design-time rule for this candidate

Oracle atoms in `REQUIRED_ATOMS.md` / `FORBIDDEN_ATOMS.md` are authored from the
**semantic contract**, not from observing an implementation run.

No executable scorer is created in this preregistration candidate.
