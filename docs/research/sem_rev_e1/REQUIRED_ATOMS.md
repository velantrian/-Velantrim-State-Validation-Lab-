# SEM-REV-E1 — Required Atoms (Candidate)

**STATUS:** preregistration candidate · NOT FROZEN  
**Rule:** atoms are semantic, not prose/style. Designed from contract, not from
implementation output.

Notation:
- `current_id=…` — sole current qualified subject of the query, when applicable
- `status=…` — projection status
- `excluded.<id> contains <reason_code…>` — typed exclusion reasons
- `UNKNOWN` — intentional unspecified optional property

---

## E1-A-01 — Deep revision chain

```text
A.status=historical_recoverable_not_current
B.status=historical_recoverable_not_current
C.status=historical_recoverable_not_current
D.status=current
current_path=Path-D
A/B/C recoverable by identity
scope=scope:project-nova
```

---

## E1-B — Temporal boundary

### E1-B-01 (before effective_from)

```text
dec:e1b-1.status=not_yet_effective
qualified_decision_ids=[]
status=NO_QUALIFIED_RESULT
reason includes not_effective_at_query_as_of
```

### E1-B-02 (exactly at effective_from)

```text
dec:e1b-1.status=current
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1b-1
temporal_applicability=boundary_inclusive_valid_from_or_effective_from_per_contract
```

### E1-B-03 (after effective_from; older overlap not current)

```text
dec:e1b-1.status=current
dec:e1b-0.status=not_current
qualified_decision_ids contains dec:e1b-1
```

### E1-B-04 (exclusive valid_to)

```text
at query_as_of == valid_to: record not temporally applicable
status=NO_QUALIFIED_RESULT OR not_current for that record
reason includes valid_to_exclusive_boundary
```

---

## E1-C — Late arrival

### E1-C-01 / E1-C-02

```text
current_decision=dec:e1c-new
late_recorded_observation=as:e1c-old does_not_outrank_by_recorded_at
axes_preserved: observed_at, asserted_at, recorded_at, effective_from distinct
```

---

## E1-D — Scopes

### E1-D-01 (query EU)

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1d-us contains scope_mismatch
no_scope_widening
```

### E1-D-02 (query US-canary)

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1d-us contains scope_mismatch
no_scope_widening
```

### E1-D-03 (query US) — positive

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1d-us
scope=scope:production-us
outcome=approved
```

---

## E1-E — Authority

### E1-E-01 (out of jurisdiction)

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-foreign contains jurisdiction_or_scope_mismatch
outcome_not_treated_as_approved_for_query_scope
```

### E1-E-02 (refused)

```text
status=NO_QUALIFIED_RESULT
excluded.dec:e1e-refused contains authority_outcome_refused
```

### E1-E-03 (superseded authority decision)

```text
dec:e1e-old.status=superseded_not_current
dec:e1e-new.status=current_if_query_matches
```

### E1-E-NX

```text
NOT EXPRESSIBLE UNDER CURRENT CONTRACT
no_required_atoms_for_CORE (boundary documentation only)
```

---

## E1-F — Dependency vs UNKNOWN

### E1-F-01 (required dependency missing)

```text
S4_stage=FAIL
CORE_PASS prohibited if this fixture is in CORE and dependency unrecovered
must_not_emit_silent_NO_QUALIFIED_RESULT_as_valid_absence
```

### E1-F-02 (optional absent)

```text
optional_property=UNKNOWN
must_not_fabricate_FALSE_or_concrete_value
qualification otherwise per contract
```

---

## E1-G — Conditional reopen

### E1-G-01

```text
prior.status=superseded_not_current
reopen_status=not_satisfied
current remains successor (or none per fixture)
```

### E1-G-02

```text
reopen_status=partial_not_sufficient
prior.status=superseded_not_current
```

### E1-G-03

```text
reopen_condition_flags=complete
authority_reapproval=absent
prior.status=superseded_not_current
```

### E1-G-04 / E1-J-02

```text
reopen_condition_flags=complete
authority_reapproval=present
prior.status=current_via_legitimate_reopen
OR successor superseded_by_reopened_prior per exact fixture rule
status=QUALIFIED_RESULT for reopened decision identity
```

---

## E1-H-01 — Contradictory evidence

```text
evidence_conflict_preserved=true
no_auto_resolved_single_truth
no_authorization_inferred_from_evidence_alone
EVIDENCE≠BELIEF
EVIDENCE≠AUTHORIZATION
```

---

## E1-I-01 — Retraction + late similar evidence

```text
as:e1i-old.status=retracted_not_qualified
as:e1i-old must_not_revive_as_same_assertion_identity
new_evidence_may_support_new_assertion_id_only_if_explicitly_represented
```

---

## E1-J-01 — Straightforward positive control

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1j-pos-1
subject=ent:service:kepler
scope=scope:production-apac
outcome=approved
semantic_force=authority_decision
authority=principal:release-board
```
