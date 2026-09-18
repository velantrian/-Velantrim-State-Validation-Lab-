# SEM-REV-E1 — Required Atoms (E0-compatible final cleanup)

**STATUS:** preregistration candidate · NOT FROZEN

Allowed assertion status values (E0): `current` | `not_current` | `retracted` | `superseded`.

Temporal explanations are reason/check atoms — **not** new status primitives.

---

## E1-A-01

```text
as:e1a-path-a.status=retracted
as:e1a-path-a.force=proposal
as:e1a-path-a.recoverable_by_identity=true
as:e1a-path-b.status=superseded
as:e1a-path-c.status=superseded
as:e1a-path-d.status=current
current_path=Path-D
dec:e1a-path-d.outcome=approved
```

---

## E1-B

### B-01

```text
as:e1b-0.status=current
as:e1b-1.status=not_current
reason/check: as:e1b-1 excluded because valid_from/effective_from > query_as_of
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
```

### B-02

```text
as:e1b-0.status=superseded
as:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

### B-03

```text
as:e1b-0.status=superseded
as:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
```

### B-04 (isolated valid_to)

```text
as:e1b-bound.status=not_current
reason/check: valid_to exclusive boundary caused temporal non-applicability
status=NO_QUALIFIED_RESULT
qualified_decision_ids does_not_contain dec:e1b-bound
```

---

## E1-C

```text
as:e1c-v1.status=superseded
as:e1c-v2.status=current
as:e1c-v1 must_not_outrank_by_recorded_at
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-v2
```

---

## E1-D

D-01/D-02: `NO_QUALIFIED_RESULT`; `excluded.dec:e1d-us contains scope_mismatch`

D-03:

```text
as:e1d-us.status=current
dec:e1d-us.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1d-us
```

---

## E1-E

E-01/E-02: NO_QUALIFIED_RESULT with scope_mismatch / authority_outcome_refused

E-03:

```text
as:e1e-old.status=superseded
as:e1e-new.status=current
dec:e1e-new.outcome=refused
status=NO_QUALIFIED_RESULT
```

---

## E1-F

### F-01

```text
missing_required_dependency_id=dec:e1f-auth
S4_stage=FAIL
S4 hash gate before oracle
FIXTURE_SEMANTIC_PASS iff exact fail-closed
```

### F-02

```text
as:e1f-opt.status=current
as:e1f-opt.uncertainty=UNKNOWN
as:e1f-opt.declared_loss=0
dec:e1f-opt.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1f-opt
```

---

## E1-G-04 / J-02

```text
as:e1g-prior-v1.status=superseded
as:e1g-succ.status=superseded
as:e1g-prior-v2.status=current
dec:e1g-prior-v2.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1g-prior-v2
```

---

## E1-H-01

```text
as:e1h-obs-a.recoverable_by_identity=true
as:e1h-obs-b.recoverable_by_identity=true
ev:e1h-1.recoverable=true
ev:e1h-2.recoverable=true
evidence_link ev:e1h-1→as:e1h-obs-a correct
evidence_link ev:e1h-2→as:e1h-obs-b correct
distinct_assertion_identities_preserved=true
```

---

## E1-I-01

```text
as:e1i-old.status=retracted
as:e1i-new.recoverable_by_identity=true
as:e1i-new != as:e1i-old
ev:e1i-new.recoverable=true
evidence_link ev:e1i-new→as:e1i-new correct
```

---

## E1-J-01

```text
as:e1j-pos-1.status=current
dec:e1j-pos-1.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
```
