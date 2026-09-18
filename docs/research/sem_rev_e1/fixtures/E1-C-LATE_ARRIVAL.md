# E1-C — Late-Arriving Record (discriminating)

**Family:** E1-C  
**Hypothesis:** H6 (primary), H2  
**PHYSICAL_CORE:** `E1-C-01` (one world)  
**DUAL_CHECK_SAME_WORLD role:** `E1-C-02` (second required check on the same world)  
**Category:** NEG (adversarial temporal)

---

## Purpose

```text
recorded_at ≠ semantic currentness
```

Discriminate:

**A.** correct temporal / revision reasoning  

from  

**B.** simply preferring one `semantic_force` over another  

Therefore both competing records are **`authority_decision`** with the same
force and outcome. Only temporal axes + typed supersession differ.

No new primitive.

---

## Physical world `E1-C-01`

- `entity_id`: `ent:service:mira`
- `query`: `Is VX-C approved for Mira in production-us?`
- `query_scope`: `scope:production-us`
- `query_as_of`: `2026-02-20T00:00:00Z`

| ID | Force | outcome | authority | scope | asserted_at | recorded_at | effective_from | valid_from | valid_to | declared_loss |
|----|-------|---------|-----------|-------|-------------|-------------|----------------|------------|----------|---------------|
| `dec:e1c-v1` | authority_decision | approved | principal:release-board | scope:production-us | 2026-01-10T00:00:00Z | **2026-02-18T00:00:00Z** (late) | 2026-01-10T00:00:00Z | 2026-01-10T00:00:00Z | NULL | 0 |
| `dec:e1c-v2` | authority_decision | approved | principal:release-board | scope:production-us | 2026-02-01T00:00:00Z | **2026-02-02T00:00:00Z** | 2026-02-01T00:00:00Z | 2026-02-01T00:00:00Z | NULL | 0 |
| `rev:e1c-v1-to-v2` | revision `supersedes` | — | — | — | — | 2026-02-01T01:00:00Z | **2026-02-01T00:00:00Z** | — | — | — |

`rev:e1c-v1-to-v2`: target=`dec:e1c-v1` (or bound assertion identity if decisions are linked via assertion rows in loader); replacement=`dec:e1c-v2`; reason=`R_E1_C_SUPERSEDE_V1`.

Both decisions share force+outcome so a force-preference heuristic cannot decide.

### Check E1-C-01 (physical package primary)

```text
dec:e1c-v1.recorded_at later MUST NOT outrank dec:e1c-v2
dec:e1c-v1.status=superseded_not_current
```

### Check E1-C-02 (DUAL_CHECK_SAME_WORLD — not independent evidence)

```text
status=QUALIFIED_RESULT
qualified_decision_ids contains dec:e1c-v2
qualified_decision_ids does_not_contain dec:e1c-v1
dec:e1c-v2.status=current
```

FORBIDDEN:

```text
dec:e1c-v1 current solely because recorded_at is later
prefer_by_semantic_force (both forces equal — N/A path)
time_axes_conflated
```
