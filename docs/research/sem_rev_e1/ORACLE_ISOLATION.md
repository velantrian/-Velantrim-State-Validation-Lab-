# SEM-REV-E1 — Oracle Isolation (final tightening)

**STATUS:** preregistration candidate · NOT FROZEN  
**Design only. Do NOT implement in this task.**

---

## Principle

```text
SYSTEM UNDER TEST ≠ ANSWER KEY
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
```

---

## SUT must not access (before fixture evidence is fixed)

REQUIRED / FORBIDDEN atoms; expected labels; hard-fail keys; answer-key side channels.

---

## Allowed SUT inputs

Registered E0 world-state families only. No hidden flags, jurisdiction maps,
rank orders, magic currentness fields, or per-fixture answer fields.

---

## Scorer / oracle timing

### Default (fixtures that emit S5)

```text
S0 → S1 → S2 → S3 → S4 → S5 → HASH(S5) verified → THEN oracle may run
```

### E1-F-01 expected fail-closed (immutable S4 hash gate)

```text
S0 → S1 → S2 → S3 → S4 FAIL (fail-closed)
→ exact S4 status/output artifact bytes fixed
→ SHA-256 recorded
→ SHA-256 independently verified
→ THEN oracle/scorer may inspect expected fail-closed outcome
```

If S4 evidence cannot be fixed and hashed:

```text
SEM_REV_E1_CORE_INCOMPLETE
```

Oracle must not run on unfixed/unhashed F-01 evidence.  
F-01 is not required to emit S5. Remaining CORE fixtures continue independently.

---

## Design-time rule

Oracle atoms from semantic contract, not implementation runs. No executable scorer here.
