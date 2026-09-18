# E1-I — Retraction + Late Similar Evidence

**Family:** E1-I · **H8/H1** · **PHYSICAL:** E1-I-01 · **NEG**

```text
observed_at on EVIDENCE only
```

---

## Query

entity `ent:service:mira` · `query_scope=scope:lab-us` · `query_as_of=2026-02-20T00:00:00Z`

## Source

| source_id | source_type |
|-----------|-------------|
| `src:e1i-new` | lab_log |

## Assertions

| ID | force | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss |
|----|-------|-------|-------------|-------------|------------|----------|-------------|---------------|
| `as:e1i-old` | claim | scope:lab-us | 2026-01-05T00:00:00Z | 2026-01-05T00:00:00Z | 2026-01-05T00:00:00Z | NULL | NULL | 0 |
| `as:e1i-new` | observation | scope:lab-us | 2026-02-10T00:00:00Z | 2026-02-15T00:00:00Z | 2026-02-10T00:00:00Z | NULL | NULL | 0 |

## Evidence for new observation

| evidence_id | source_id | observed_at | recorded_at | declared_loss |
|-------------|-----------|-------------|-------------|---------------|
| `ev:e1i-new` | src:e1i-new | **2026-02-10T00:00:00Z** | 2026-02-15T00:00:00Z | 0 |

## Link

`ev:e1i-new` ↔ `as:e1i-new`

## Revision

| revision_id | type | target_assertion_id | replacement | reason | effective_from | recorded_at |
|-------------|------|---------------------|-------------|--------|----------------|-------------|
| `rev:e1i-retract` | retracts | **as:e1i-old** | NULL | R_E1_I_INSUFFICIENT | 2026-01-08T00:00:00Z | 2026-01-08T00:00:00Z |

## REQUIRED

```text
as:e1i-old.status=retracted
as:e1i-old must_not_revive_as_same_assertion_identity
as:e1i-new.recoverable_by_identity=true
as:e1i-new != as:e1i-old
ev:e1i-new.recoverable=true
evidence_link ev:e1i-new→as:e1i-new correct
```

FORBIDDEN: revive old ID; drop new assertion/evidence; observed_at on as:e1i-new; identity collapse.
