# SEM-REV-E1 — Internal Consistency Audit (v0.1 candidate)

**DATE:** 2026-09-15  
**RESULT:** `PASS_WITH_BOUNDARIES`  
**C1:** expected fail-closed on E1-F-01 no longer prohibits CORE_PASS

## Checks

| Check | Result |
|-------|--------|
| Every CORE fixture maps to ≥1 hypothesis | PASS |
| Every hypothesis H1–H10 has ≥1 discriminating fixture | PASS |
| Positive/negative expectations present where appropriate | PASS |
| Oracle atoms semantic (not wording/style) | PASS |
| No fixture secretly requires unregistered new semantics for CORE | PASS |
| Authority precedence underdefined case isolated as NX | PASS (E1-E-NX) |
| Time axes remain distinct in fixtures | PASS |
| Scope explicit | PASS |
| Authority explicit where applicable | PASS |
| Required dependency vs UNKNOWN explicit (E1-F) | PASS |
| C1: EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE | PASS |
| C1: E1-F-01 fail-closed does not prohibit CORE_PASS | PASS |
| C1: F-01 not rewritten as ordinary NO_QUALIFIED_RESULT | PASS |
| Positive controls prevent exclude-all (E1-J, D-03, G-04) | PASS |
| No implementation-output-derived expected answers | PASS (contract-first) |
| E0 freeze/result not modified | PASS |
| New architectural primitive required for CORE suite | **NO** |
| NX case would need new primitive to *resolve* | YES — deliberately out of CORE |

## Counts

- Families: 10 (A–J)
- CORE physical cases: 22 (J-02 = role alias of G-04)
- Hypotheses: 1 continuity (H0-E1) + 10 failure classes (H1–H10)
- Positive controls: 3 (D-03, G-04/J-02, J-01)
- Negative adversarial CORE: 19
- Pairwise groupings: 8
- NX boundary: 1

## Stop-condition review

No stop triggered that blocks publishing this **candidate**.  
E1-E-NX is documented, not silently given a winner.
