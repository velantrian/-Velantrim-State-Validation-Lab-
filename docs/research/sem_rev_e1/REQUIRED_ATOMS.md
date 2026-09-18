# SEM-REV-E1 — Required Atoms (final pre-freeze tightening)

**STATUS:** preregistration candidate · NOT FROZEN  
`declared_loss` atoms: INTEGER `0`/`1` only.

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

### E1-B-01

```text
dec:e1b-0.status=current
dec:e1b-1.status=not_yet_effective
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-0
qualified_decision_ids does_not_contain dec:e1b-1
```

### E1-B-02 / E1-B-04 (B-04 = dual-check)

```text
dec:e1b-0.status=not_temporally_applicable
dec:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
qualified_decision_ids does_not_contain dec:e1b-0
```

B-04 also requires `valid_to_exclusive_boundary` reason emphasis for e1b-0.

### E1-B-03

```text
dec:e1b-1.status=current
dec:e1b-0.status=not_current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
```

---

## E1-C (physical C-01; dual-check C-02)

```text
dec:e1c-v1.status=superseded_not_current
dec:e1c-v1 must_not_outrank_by_recorded_at
dec:e1c-v2.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-v2
qualified_decision_ids does_not_contain dec:e1c-v1
same_semantic_force=authority_decision_both
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
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1d-us
scope=scope:production-us
outcome=approved
declared_loss=0
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
dec:e1e-old.status=superseded
dec:e1e-new.status=current
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
S4_OUTPUT_SHA256 recorded
S4_OUTPUT_SHA256 independently verified before oracle
FIXTURE_SEMANTIC_PASS iff exact fail-closed after hash gate
must_not_emit_silent_NO_QUALIFIED_RESULT_as_valid_absence
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS
does_not_prohibit_CORE_PASS
S5_not_required_for_this_fixture
```

If S4 evidence cannot be fixed/hashed → CORE `INCOMPLETE` (not F-01 semantic PASS).

### F-02

```text
optional uncertainty=UNKNOWN
declared_loss=0
must_not_fabricate_FALSE_or_concrete_value
qualification otherwise per contract
```

---

## E1-G

### G-NX

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
no_required_CORE_atoms
```

### G-04 / J-02

```text
as:e1g-prior-v1.status=superseded
as:e1g-succ.status=superseded
as:e1g-prior-v2.status=current
dec:e1g-prior-v2.status=current
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
no_single_authorized_truth_fabricated_from_observations_alone=true
```

---

## E1-I-01

```text
as:e1i-old.status=retracted
as:e1i-old must_not_revive_as_same_assertion_identity
as:e1i-new.recoverable_by_identity=true
as:e1i-new remains a distinct identity
as:e1i-new != as:e1i-old
```

---

## E1-J-01

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
subject=ent:service:kepler
scope=scope:production-apac
outcome=approved
semantic_force=authority_decision
authority=principal:release-board
declared_loss=0
```
