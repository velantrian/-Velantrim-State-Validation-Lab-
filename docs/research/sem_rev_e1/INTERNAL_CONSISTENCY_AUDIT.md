# SEM-REV-E1 — Internal Consistency Audit (C2–C12)

**DATE:** 2026-09-15 (correction pass continued)  
**RESULT:** `PASS_WITH_BOUNDARIES`  
**C1:** CLOSED  
**C12 CROSS_DOC_CONSISTENCY:** PASS (after C2–C11)

## Checks

| Check | Result |
|-------|--------|
| Every CORE fixture maps to ≥1 hypothesis | PASS |
| Every CORE hypothesis claim has ≥1 discriminating fixture | PASS |
| B-01 oracle single-valued (e1b-0 current) | PASS (C2) |
| B-04 single-valued + dual-check of B-02 | PASS (C3) |
| G reopen: no same-ID; new version; compound → NX | PASS (C4) |
| E-01 scope_mismatch not jurisdiction | PASS (C5) |
| H narrowed to typed observation preservation | PASS (C6) |
| A exact retracted/superseded/current | PASS (C7) |
| Counts/taxonomy recomputed; no POS-ish/NEG | PASS (C8) |
| declared_loss INTEGER 0/1 only | PASS (C9) |
| No hidden condition flags / jurisdiction maps | PASS (C10) |
| Fixture vs CORE classification vocabulary | PASS (C11) |
| C1 expected fail-closed preserved | PASS |
| Alias not counted as independent evidence | PASS |
| NX explicit (E1-E-NX, E1-G-NX) | PASS |
| New architectural primitive required for CORE | **NO** |

## Declared_loss

| Item | Value |
|------|-------|
| Encoding | INTEGER NOT NULL; `0` = no loss; `1` = loss |
| Source | E0 `schema.sql` assertion/evidence/projection |
| `declared_loss=UNKNOWN` | **forbidden / removed** |
| DECLARED_LOSS_ENCODING_CHANGED | **NO** |

## Remaining NX / unresolved boundaries

1. `E1-E-NX` — two same-scope conflicting approvals without typed precedence  
2. `E1-G-NX` — compound reopen-condition evaluation (`K_CONSTRAINT_REMOVED ∧ reapproval`)  

## Counts snapshot

See `FIXTURE_MATRIX.md` (PHYSICAL=19, ROLE/CHECK entries=21, TRUE_PAIRWISE=3,
CONTRAST=2, DUAL_CHECK=2, ROLE_ALIASES=1, POS physical=5, NX=2).
