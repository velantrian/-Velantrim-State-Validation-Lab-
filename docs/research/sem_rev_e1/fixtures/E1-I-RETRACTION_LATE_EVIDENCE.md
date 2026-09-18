# E1-I — Retraction + Late Similar Evidence

**Family:** E1-I  
**Hypotheses:** H8 (narrowed), H1  
**Physical CORE:** E1-I-01

---

## Purpose

A claim is retracted. Later evidence arrives that **resembles** the original
claim. Similarity must **not** restore the historical assertion identity.
New evidence may support a **new** assertion only if explicitly represented.

---

## E1-I-01

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:lab-us`
- `query_as_of`: `2026-02-20T00:00:00Z`

| ID | Force | Status | scope | asserted/observed | recorded | declared_loss | notes |
|----|-------|--------|-------|-------------------|----------|---------------|-------|
| `as:e1i-old` | claim | **retracted** | lab-us | 2026-01-05 | 2026-01-05 | 0 | original |
| `rev:e1i-retract` | `retracts` | — | — | — | 2026-01-08 | — | effective 2026-01-08; `R_E1_I_INSUFFICIENT` |
| `as:e1i-new` | observation | active candidate | lab-us | observed 2026-02-10 | recorded 2026-02-15 | 0 | **new identity** |

### Expected

```text
as:e1i-old.status=retracted
as:e1i-old must_not_revive_as_same_assertion_identity
as:e1i-new may exist as separate assertion
```
