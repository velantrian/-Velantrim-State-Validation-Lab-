# E1-A — Deep Revision Chain

**Family:** E1-A  
**Hypothesis:** H1  
**CORE case:** E1-A-01  
**Role:** NEG (adversarial depth)

---

## Purpose

Test whether increased revision depth causes an older valid-looking state to
revive as current.

Required question: can D remain current while A/B/C remain historically
recoverable but not current?

---

## E1-A-01

### Query

- `fixture_id`: `E1-A-01`
- `entity_id`: `ent:project:nova`
- `query`: `What is the current path decision for project Nova?`
- `query_scope`: `scope:project-nova`
- `query_as_of`: `2026-03-15T00:00:00Z`

### Records (chain A→B→C→D)

| ID | Force | Status intent | asserted_at | recorded_at | valid_from | valid_to | effective_from | notes |
|----|-------|---------------|-------------|-------------|------------|----------|----------------|-------|
| `as:e1a-path-a` | proposal | retracted | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z | 2026-01-01T00:00:00Z | NULL | — | Path-A |
| `rev:e1a-a-retract` | revision | retracts A | 2026-01-02T00:00:00Z | 2026-01-02T01:00:00Z | — | — | 2026-01-02T00:00:00Z | reason `R_E1_A_CONSTRAINT` |
| `dec:e1a-path-b` | decision | superseded | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z | 2026-01-05T00:00:00Z | NULL | — | Path-B; authority `principal:project-owner` |
| `dec:e1a-path-c` | decision | superseded | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | 2026-01-20T00:00:00Z | NULL | — | Path-C |
| `rev:e1a-b-to-c` | revision | supersedes B→C | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | — | — | 2026-01-20T00:00:00Z | reason `R_E1_B_SUPERSEDED` |
| `dec:e1a-path-d` | decision | **current** | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z | 2026-02-10T00:00:00Z | NULL | — | Path-D |
| `rev:e1a-c-to-d` | revision | supersedes C→D | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z | — | — | 2026-02-10T00:00:00Z | reason `R_E1_C_SUPERSEDED` |

### Shared typed fields

- `scope_id`: `scope:project-nova` (all)
- `uncertainty`: `UNKNOWN` where not specified
- `declared_loss`: `UNKNOWN` where not specified
- `observed_at`: `UNKNOWN` for decision records (not observations)
- `revision_relation`: as above
- **required dependencies for qualification:** retraction of A; supersessions B→C and C→D; scope; temporal applicability of D

### Expected (contract-first)

- current = Path-D / `dec:e1a-path-d`
- A/B/C recoverable, not current
- reopen not claimed unless separately preregistered (none here)

### S3 candidate constraint (anti-trivial)

Must include at least `as:e1a-path-a`, `dec:e1a-path-b`, `dec:e1a-path-c`, `dec:e1a-path-d` so success cannot be “forget history”.
