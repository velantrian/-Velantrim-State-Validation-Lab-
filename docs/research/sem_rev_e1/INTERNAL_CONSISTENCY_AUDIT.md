# SEM-REV-E1 — Internal Consistency Audit (final pre-freeze tightening)

**RESULT:** `PASS_WITH_BOUNDARIES`  
**C12 / final tightening CROSS_DOC_CONSISTENCY:** **PASS**  
**E1_FROZEN:** NO

## Checks

| Check | Result |
|-------|--------|
| PHYSICAL_CORE = 17 (C counted once) | PASS |
| ROLE/CHECK entries = 20 | PASS |
| TRUE_PAIRWISE = 2 only (P-B-eff, P-D-scope) | PASS |
| CG-F-dep not called TRUE_PAIRWISE | PASS |
| No NEG/POS or NEG/UNKNOWN labels | PASS |
| F-01 S4 hash-before-oracle gate | PASS |
| G-04 fully specified (no “as needed”) | PASS |
| C same-force late-arrival discrimination | PASS |
| E-03 exact oracle | PASS |
| I-01 new identity recoverable required | PASS |
| E-NX approved vs refused conflict | PASS |
| No hidden primitives | PASS |
| declared_loss INTEGER 0/1 | PASS |
| Implementation / experiment / freeze / merge | NO |

## Counts snapshot

PHYSICAL_CORE_FIXTURES = 17  
CORE_ROLE_OR_CHECK_ENTRIES = 20  
TRUE_PAIRWISE = 2  
CONTRAST = 3  
DUAL_CHECK = 2  
ROLE_ALIASES = 1  
POS physical = 5  
NX = 2  

## Remaining NX

1. `E1-E-NX` — approved vs refused; same scope; no typed precedence  
2. `E1-G-NX` — compound reopen-condition evaluation  
