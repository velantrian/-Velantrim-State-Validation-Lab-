# E1-I — Retraction + Late Contradictory Evidence

**Family:** E1-I  
**Hypotheses:** H8, H1  
**CORE case:** E1-I-01

---

## Purpose

A claim is retracted. Later evidence arrives that **resembles** the original
claim. Similarity / new evidence must **not** magically restore the historical
assertion identity. New evidence may support a **new** assertion only if
explicitly represented.

---

## E1-I-01

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:lab-us`
- `query_as_of`: `2026-02-20T00:00:00Z`

| ID | Force | Status | scope | asserted/observed | recorded | notes |
|----|-------|--------|-------|-------------------|----------|-------|
| `as:e1i-old` | claim | **retracted** | lab-us | 2026-01-05 | 2026-01-05 | original claim |
| `rev:e1i-retract` | revision | retracts old | — | — | 2026-01-08 | effective 2026-01-08; reason `R_E1_I_INSUFFICIENT` |
| `as:e1i-new` | observation | active candidate | lab-us | observed 2026-02-10 | recorded 2026-02-15 | **new identity**; similar content codes allowed |

### Expected

- `as:e1i-old` remains retracted; not qualified active
- must **not** revive `as:e1i-old` identity
- `as:e1i-new` may exist as separate assertion; does not un-retract old

### Forbidden

- silent un-retraction;
- similarity-based identity merge restoring old ID
