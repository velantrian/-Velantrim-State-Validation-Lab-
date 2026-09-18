# SEM-REV-E1 — Forbidden Atoms (C2–C12)

**STATUS:** preregistration candidate · NOT FROZEN

---

## Cross-cutting

```text
assertion status not_yet_effective
assertion status not_temporally_applicable
TEMPORAL REASON promoted to new status primitive
observed_at on assertion rows
ASSERTION CURRENTNESS assigned as dec:*.status
revision target/replacement = dec:* (must be as:*)
asserted_at/valid_*/uncertainty/declared_loss on authority_decision rows
hidden assertion↔decision binding
scope_widening
proposal→decision force flip
observation→authorization
retracted→qualified_active
superseded→current without new superseding version identity
UNKNOWN→FALSE_or_fabricated_value on optional uncertainty
declared_loss=UNKNOWN  (unsupported encoding)
required_dependency_loss→valid_absence / ordinary NO_QUALIFIED_RESULT
EXPECTED_FAIL_CLOSED used to bypass S4 hash-before-oracle gate
recorded_at used as sole currentness authority
mutable is_current stored answer flag
oracle_atoms visible to SUT before evidence fixed
prose_parsed mandatory qualifier
majority_pass_override
same_id_resurrection
hidden_condition_flag_records
invented_authority_jurisdiction_or_rank
```

---

## E1-A-01

```text
A.status=superseded   (must remain retracted, not collapsed)
B.status=retracted
C.status=retracted
A.status=current
B.status=current
C.status=current
current_path=Path-A|Path-B|Path-C
D omitted while claiming currentness elsewhere
generic historical_recoverable_not_current as sole A/B/C status
```

---

## E1-B

```text
dec:e1b-1 qualified before effective_from
NO_QUALIFIED_RESULT while as:e1b-0 remains valid (B-01)
as:e1b-0.status other than superseded at/after supersession effective (B-02/B-03)
as:e1b-bound qualified at T==valid_to (B-04)
B-04 combined with supersession confound
assertion status not_yet_effective / not_temporally_applicable
```

---

## E1-C

```text
as:e1c-v1 current solely because recorded_at is later
as:e1c-v1 outranks as:e1c-v2 by recorded_at
dec:e1c-v*.status used as assertion-currentness atom
revision targeting dec:*
time_axes_conflated
prefer_by_semantic_force as explanation (forces are equal)
```

---

## E1-D

```text
dec:e1d-us qualified under production-eu
dec:e1d-us qualified under production-us-canary
lab-* silently widened to production-*
```

---

## E1-E

```text
scope_mismatch treated as jurisdiction proof
refused→approved flip
superseded authority decision treated current
invented_authority_hierarchy_winner
```

---

## E1-F

```text
F-01: silent ordinary NO_QUALIFIED_RESULT as success path for missing required dep
F-01: fail due to any omitted dependency other than dec:e1f-auth
F-02: NO_QUALIFIED_RESULT
F-02: uncertainty=FALSE or fabricated uncertainty value
F-02: decision omitted
declared_loss=UNKNOWN
```

---

## E1-G

```text
as:e1g-prior-v1.status=current
current_via_legitimate_reopen
same-ID revival
OR dual expected forms
generic rev:* used as condition flag (e.g. rev:e1g-k-removed)
compound condition evaluated without registered primitive
```

---

## E1-H

```text
silent_merge_or_delete_of_either_observation
authorization_inferred_from_observations_alone
claim_typed_conflict_relation_detected
prose_parsed_effect_code_as_mandatory_atom
evidence_conflict_preserved as typed detection claim
```

---

## E1-I

```text
as:e1i-old revived as same assertion identity
similarity-based silent un-retraction
as:e1i-new omitted / not recoverable
identity_collapse as:e1i-new → as:e1i-old
```

---

## E1-J

```text
NO_QUALIFIED_RESULT
outcome=refused
wrong scope
authority=UNKNOWN
decision omitted
trivial abstention
counting J-02 as independent physical evidence
```
