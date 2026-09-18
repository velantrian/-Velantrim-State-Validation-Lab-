# E1-A — Deep Revision Chain

**Family:** E1-A  
**Hypothesis:** H1  
**CORE physical case:** E1-A-01  
**Role:** NEG

---

## Purpose

Test whether increased revision depth causes an older valid-looking state to
revive as current.

Required question: can D remain current while A remains **retracted** and
B/C remain **superseded** (recoverable by identity, not current)?

Do **not** collapse RETRACTED and SUPERSEDED into generic “historical”.

---

## E1-A-01

### Query

- `fixture_id`: `E1-A-01`
- `entity_id`: `ent:project:nova`
- `query`: `What is the current path decision for project Nova?`
- `query_scope`: `scope:project-nova`
- `query_as_of`: `2026-03-15T00:00:00Z`

### Records (chain A→B→C→D)

| ID | Force | Exact status at query | asserted_at | recorded_at | valid_from | valid_to | effective_from | notes |
|----|-------|------------------------|-------------|-------------|------------|----------|----------------|-------|
| `as:e1a-path-a` | proposal | **retracted** | 2026-01-01T00:00:00Z | 2026-01-01T01:00:00Z | 2026-01-01T00:00:00Z | NULL | — | Path-A |
| `rev:e1a-a-retract` | revision `retracts` | retracts A | 2026-01-02T00:00:00Z | 2026-01-02T01:00:00Z | — | — | 2026-01-02T00:00:00Z | reason `R_E1_A_CONSTRAINT` |
| `dec:e1a-path-b` / `as:e1a-path-b` | decision | **superseded** | 2026-01-05T00:00:00Z | 2026-01-05T01:00:00Z | 2026-01-05T00:00:00Z | NULL | — | Path-B; authority `principal:project-owner` |
| `dec:e1a-path-c` / `as:e1a-path-c` | decision | **superseded** | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | 2026-01-20T00:00:00Z | NULL | — | Path-C |
| `rev:e1a-b-to-c` | revision `supersedes` | B→C | 2026-01-20T00:00:00Z | 2026-01-20T01:00:00Z | — | — | 2026-01-20T00:00:00Z | reason `R_E1_B_SUPERSEDED` |
| `dec:e1a-path-d` / `as:e1a-path-d` | decision | **current** | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z | 2026-02-10T00:00:00Z | NULL | — | Path-D |
| `rev:e1a-c-to-d` | revision `supersedes` | C→D | 2026-02-10T00:00:00Z | 2026-02-10T01:00:00Z | — | — | 2026-02-10T00:00:00Z | reason `R_E1_C_SUPERSEDED` |

### Shared typed fields

- `scope_id`: `scope:project-nova` (all)
- `uncertainty`: NULL → projects as `UNKNOWN` where unspecified (optional)
- `declared_loss`: INTEGER `0` (no declared loss) unless a case explicitly sets `1`
- `observed_at`: not applicable on decision/proposal rows (no fabricated value)
- **required dependencies:** retraction of A; supersessions B→C and C→D; scope; temporal applicability of D

### Expected (exact)

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

### S3 candidate constraint (anti-trivial)

Must include at least Path-A/B/C/D identities so success cannot be “forget history”.
