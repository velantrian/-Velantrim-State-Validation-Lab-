# E1-H — Opposing Observations (Typed Boundary)

**Family:** E1-H  
**Hypothesis:** H8 (**narrowed**)  
**Physical CORE:** E1-H-01  

---

## Capability under test (honest)

```text
PRESERVING DISTINCT OPPOSING OBSERVATIONS
≠
DERIVING A TYPED CONFLICT RELATION
```

Unless a typed conflict primitive already exists in the E0 contract (it does
**not**), E1 must **not** claim “the SUT detected a contradiction”.

No `effect_code` field is added. No prose parsing for mandatory semantics.

---

## E1-H-01

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:lab-us`
- `query_as_of`: `2026-02-01T00:00:00Z`
- `query`: `What observations exist for Mira under lab-us?`

| ID | Force | scope | observed_at | recorded_at | declared_loss | content (non-oracle prose) |
|----|-------|-------|-------------|-------------|---------------|----------------------------|
| `as:e1h-obs-a` | observation | lab-us | 2026-01-10 | 2026-01-11 | 0 | distinct observation A |
| `as:e1h-obs-b` | observation | lab-us | 2026-01-12 | 2026-01-13 | 0 | distinct observation B |
| `ev:e1h-1` ↔ `as:e1h-obs-a` | evidence link | — | — | — | 0 | typed link only |
| `ev:e1h-2` ↔ `as:e1h-obs-b` | evidence link | — | — | — | 0 | typed link only |

No `authority_decision` approving production action is present.

### REQUIRED

```text
as:e1h-obs-a recoverable=true
as:e1h-obs-b recoverable=true
distinct_identities_preserved=true
no_authority_decision_fabricated=true
no_production_authorization_inferred=true
no_single_authorized_truth_fabricated_from_observations_alone=true
```

### FORBIDDEN

```text
silent_merge_or_delete_of_either_observation
authorization_inferred_from_observations_alone
claim_typed_conflict_relation_detected
prose_parsed_effect_code_as_mandatory_atom
```

### Explicit non-claim

Oracle does **not** require `evidence_conflict_preserved=true` as a typed
conflict-detection atom.
