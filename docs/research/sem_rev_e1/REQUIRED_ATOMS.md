# SEM-REV-E1 — Required Atoms (record-family aligned)

**STATUS:** preregistration candidate · NOT FROZEN  

```text
ASSERTION CURRENTNESS ≠ AUTHORITY DECISION OUTCOME
REVISIONS TARGET ASSERTIONS ONLY
```

`declared_loss` / `uncertainty` / `valid_*` / `asserted_at` live on **assertions**.  
`outcome` / `authority_id` / `effective_from` live on **authority_decisions**.  
Qualification may list `qualified_decision_ids` containing `dec:*` bound to current assertions.

---

## E1-A-01

```text
A.status=retracted
A.force=proposal
A.recoverable_by_identity=true
B.status=superseded
B.force=decision
B.recoverable_by_identity=true
C.status=superseded
C.force=decision
C.recoverable_by_identity=true
D.status=current
D.force=decision
current_path=Path-D
scope=scope:project-nova
```

---

## E1-B

### B-01

```text
as:e1b-0.status=current
as:e1b-1.status=not_yet_effective
dec:e1b-0.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
```

### B-02 / B-04

```text
as:e1b-0.status=not_temporally_applicable
as:e1b-1.status=current
dec:e1b-1.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

B-04 emphasizes exclusive `valid_to` on **as:e1b-0**.

### B-03

```text
as:e1b-1.status=current
as:e1b-0.status=not_current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
```

---

## E1-C

```text
as:e1c-v1.status=superseded
as:e1c-v2.status=current
as:e1c-v1 must_not_outrank_by_recorded_at
dec:e1c-v2.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-v2
qualified_decision_ids does_not_contain dec:e1c-v1
```

---

## E1-D

### D-01 / D-02

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1d-us contains scope_mismatch
no_scope_widening
```

### D-03

```text
as:e1d-us.status=current
dec:e1d-us.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1d-us
scope=scope:production-us
as:e1d-us.declared_loss=0
```

---

## E1-E

### E-01

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-foreign contains scope_mismatch
```

### E-02

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-refused contains authority_outcome_refused
```

### E-03

```text
as:e1e-old.status=superseded
as:e1e-new.status=current
dec:e1e-new.outcome=refused
status=NO_QUALIFIED_RESULT
qualified_approved_decision_ids does_not_contain dec:e1e-old
qualified_approved_decision_ids does_not_contain dec:e1e-new
```

### E-NX

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
approved_vs_refused_same_scope_no_precedence
no_required_CORE_atoms
```

---

## E1-F

### F-01

```text
FIXTURE_EXPECTED_FAIL_CLOSED
S4_stage=FAIL
S4_OUTPUT_BYTES fixed
S4_OUTPUT_SHA256 recorded + independently verified before oracle
FIXTURE_SEMANTIC_PASS iff exact fail-closed after hash gate
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
does_not_prohibit_CORE_PASS
S5_not_required_for_this_fixture
```

### F-02

```text
as:e1f-opt.uncertainty=UNKNOWN
as:e1f-opt.declared_loss=0
dec:e1f-opt.outcome=approved
must_not_fabricate_FALSE_or_concrete_value
```

---

## E1-G

### G-NX

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
```

### G-04 / J-02

```text
as:e1g-prior-v1.status=superseded
as:e1g-succ.status=superseded
as:e1g-prior-v2.status=current
dec:e1g-prior-v2.outcome=approved
current_path=Path-Prior
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1g-prior-v2
qualified_decision_ids does_not_contain dec:e1g-prior-v1
qualified_decision_ids does_not_contain dec:e1g-succ
same_id_resurrection=false
```

---

## E1-H-01

```text
as:e1h-obs-a recoverable=true
as:e1h-obs-b recoverable=true
distinct_identities_preserved=true
no_authority_decision_fabricated=true
no_production_authorization_inferred=true
```

---

## E1-I-01

```text
as:e1i-old.status=retracted
as:e1i-old must_not_revive_as_same_assertion_identity
as:e1i-new.recoverable_by_identity=true
as:e1i-new != as:e1i-old
```

---

## E1-J-01

```text
as:e1j-pos-1.status=current
as:e1j-pos-1.declared_loss=0
dec:e1j-pos-1.outcome=approved
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
subject=ent:service:kepler
scope=scope:production-apac
authority=principal:release-board
```
