# E1-H — Opposing Observations (typed boundary)

**Family:** E1-H · **Hypothesis:** H8 (narrowed) · **PHYSICAL:** E1-H-01 · **NEG**

```text
observed_at belongs to EVIDENCE, not ASSERTION
PRESERVING DISTINCT OPPOSING OBSERVATIONS ≠ DERIVING A TYPED CONFLICT RELATION
```

---

## Query

entity `ent:service:mira` · `query_scope=scope:lab-us` · `query_as_of=2026-02-01T00:00:00Z`  
query: `What observations exist for Mira under lab-us?`

## Sources

| source_id | source_type | description |
|-----------|-------------|-------------|
| `src:e1h-a` | lab_log | E1-H observation A source |
| `src:e1h-b` | lab_log | E1-H observation B source |

## Assertions (no observed_at)

| ID | force | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss |
|----|-------|-------|-------------|-------------|------------|----------|-------------|---------------|
| `as:e1h-obs-a` | observation | scope:lab-us | 2026-01-10T00:00:00Z | 2026-01-11T00:00:00Z | 2026-01-10T00:00:00Z | NULL | NULL | 0 |
| `as:e1h-obs-b` | observation | scope:lab-us | 2026-01-12T00:00:00Z | 2026-01-13T00:00:00Z | 2026-01-12T00:00:00Z | NULL | NULL | 0 |

## Evidence (owns observed_at)

| evidence_id | source_id | observed_at | recorded_at | declared_loss | description |
|-------------|-----------|-------------|-------------|---------------|-------------|
| `ev:e1h-1` | src:e1h-a | 2026-01-10T00:00:00Z | 2026-01-11T00:00:00Z | 0 | obs A evidence |
| `ev:e1h-2` | src:e1h-b | 2026-01-12T00:00:00Z | 2026-01-13T00:00:00Z | 0 | obs B evidence |

## Links

| evidence_id | assertion_id |
|-------------|--------------|
| ev:e1h-1 | as:e1h-obs-a |
| ev:e1h-2 | as:e1h-obs-b |

No authority_decision present.

## REQUIRED

```text
as:e1h-obs-a.recoverable_by_identity=true
as:e1h-obs-b.recoverable_by_identity=true
ev:e1h-1.recoverable=true
ev:e1h-2.recoverable=true
evidence_link ev:e1h-1→as:e1h-obs-a correct
evidence_link ev:e1h-2→as:e1h-obs-b correct
distinct_assertion_identities_preserved=true
no_authority_decision_fabricated=true
no_production_authorization_inferred=true
no_single_authorized_truth_fabricated_from_observations_alone=true
```

FORBIDDEN: observed_at on as:*; silent merge/delete; typed conflict-detection claim; prose effect_code atoms.
