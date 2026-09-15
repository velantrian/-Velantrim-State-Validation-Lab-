# E1-H — Contradictory Evidence

**Family:** E1-H  
**Hypothesis:** H8  
**CORE case:** E1-H-01

---

## Purpose

```text
EVIDENCE ≠ BELIEF
EVIDENCE ≠ AUTHORIZATION
```

Preserve conflict; do not auto-resolve to a single asserted truth or authorization.

---

## E1-H-01

- `entity_id`: `ent:service:mira`
- `query_scope`: `scope:lab-us`
- `query_as_of`: `2026-02-01T00:00:00Z`
- `query`: `What is observed about Mira latency under lab-us?`

### Evidence / observations

| ID | Force | Claim summary (typed effect field optional) | scope | observed_at | recorded_at |
|----|-------|-----------------------------------------------|-------|-------------|-------------|
| `ev:e1h-1` / `as:e1h-obs-hi` | observation | higher latency effect coded `effect_code=E_UP` | lab-us | 2026-01-10 | 2026-01-11 |
| `ev:e1h-2` / `as:e1h-obs-lo` | observation | lower latency effect coded `effect_code=E_DOWN` | lab-us | 2026-01-12 | 2026-01-13 |

No authority_decision approving production action is present.

### Expected

- both observations recoverable;
- conflict preserved;
- no single “true” production authorization inferred;
- no collapse to one belief atom as authorization

### Forbidden

- auto-resolved single truth;
- authorization inferred from evidence alone
