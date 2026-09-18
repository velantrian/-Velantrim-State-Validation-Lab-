# E1-A — Deep Revision Chain

**Family:** E1-A · **Hypothesis:** H1 · **PHYSICAL:** E1-A-01 · **Category:** NEG

```text
REVISIONS TARGET ASSERTIONS ONLY
ASSERTION CURRENTNESS ≠ AUTHORITY DECISION OUTCOME
```

---

## Query

- `fixture_id`: E1-A-01
- `entity_id`: ent:project:nova
- `query_scope`: scope:project-nova
- `query_as_of`: 2026-03-15T00:00:00Z
- query: `What is the current path decision for project Nova?`

---

## Assertions (explicit — no combined dec/as rows)

| ID | force | path | scope | asserted_at | recorded_at | valid_from | valid_to | uncertainty | declared_loss | reason |
|----|-------|------|-------|-------------|-------------|------------|----------|-------------|---------------|--------|
| `as:e1a-path-a` | proposal | Path-A | scope:project-nova | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z | 2026-01-01T00:00:00Z | NULL | NULL | 0 | — |
| `as:e1a-path-b` | decision | Path-B | scope:project-nova | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z | 2026-01-05T00:00:00Z | NULL | NULL | 0 | R_E1_A_PATH_B |
| `as:e1a-path-c` | decision | Path-C | scope:project-nova | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | 2026-01-20T00:00:00Z | NULL | NULL | 0 | R_E1_A_PATH_C |
| `as:e1a-path-d` | decision | Path-D | scope:project-nova | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z | 2026-02-10T00:00:00Z | NULL | NULL | 0 | R_E1_A_PATH_D |

A is proposal-only (no authority_decision required).

## Authority decisions (B/C/D)

| decision_id | assertion_id | authority | outcome | force | scope | reason | effective_from | recorded_at |
|-------------|--------------|-----------|---------|-------|-------|--------|----------------|-------------|
| `dec:e1a-path-b` | as:e1a-path-b | principal:project-owner | approved | authority_decision | scope:project-nova | R_E1_A_PATH_B | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z |
| `dec:e1a-path-c` | as:e1a-path-c | principal:project-owner | approved | authority_decision | scope:project-nova | R_E1_A_PATH_C | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z |
| `dec:e1a-path-d` | as:e1a-path-d | principal:project-owner | approved | authority_decision | scope:project-nova | R_E1_A_PATH_D | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z |

## Revisions (assertion targets only)

| revision_id | type | target_assertion_id | replacement_assertion_id | reason | effective_from | recorded_at |
|-------------|------|---------------------|--------------------------|--------|----------------|-------------|
| `rev:e1a-a-retract` | retracts | as:e1a-path-a | NULL | R_E1_A_CONSTRAINT | 2026-01-02T00:00:00Z | 2026-01-02T01:00:00Z |
| `rev:e1a-b-to-c` | supersedes | as:e1a-path-b | as:e1a-path-c | R_E1_B_SUPERSEDED | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z |
| `rev:e1a-c-to-d` | supersedes | as:e1a-path-c | as:e1a-path-d | R_E1_C_SUPERSEDED | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z |

## Expected (exact E0 statuses)

```text
as:e1a-path-a.status=retracted
as:e1a-path-a.force=proposal
as:e1a-path-a.recoverable_by_identity=true
as:e1a-path-b.status=superseded
as:e1a-path-b.force=decision
as:e1a-path-b.recoverable_by_identity=true
as:e1a-path-c.status=superseded
as:e1a-path-c.force=decision
as:e1a-path-c.recoverable_by_identity=true
as:e1a-path-d.status=current
as:e1a-path-d.force=decision
current_path=Path-D
dec:e1a-path-d.outcome=approved
scope=scope:project-nova
```

S3 must include Path-A/B/C/D assertion identities (anti-trivial omit-history).
