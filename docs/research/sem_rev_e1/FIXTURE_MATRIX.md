# SEM-REV-E1 — Fixture Matrix (C2–C12 corrected)

**STATUS:** preregistration candidate · NOT FROZEN  
**C1:** CLOSED (expected fail-closed)  
**Corrections:** C2–C12 applied

---

## Taxonomy (precise)

| Term | Meaning |
|------|---------|
| PHYSICAL_CORE | Independent world-state fixture counted as experimental evidence |
| ROLE_OR_CHECK | Additional required check/role on an existing physical fixture; **not** independent evidence |
| TRUE_PAIRWISE | Shared base world; exactly one material semantic Δ; both sides explicit |
| CONTRAST_GROUP | Related opposing cases; not necessarily single-Δ pairwise |
| DUAL_CHECK_SAME_WORLD | Same physical bytes; multiple required check emphases |
| CONDITION_LATTICE | Multi-flag reopen lattice — **NX** under current contract |
| ROLE_ALIAS | Alternate role tag on one physical fixture |
| NX | `NOT EXPRESSIBLE UNDER CURRENT CONTRACT` |

---

## Counts (recomputed)

| Metric | Count |
|--------|------:|
| PHYSICAL_CORE_FIXTURES | **19** |
| CORE_ROLE_OR_CHECK_ENTRIES | **21** (= 19 physical + B-04 dual-check + J-02 role alias) |
| TRUE_PAIRWISE_COUNTERFACTUAL_GROUPS | **3** (P-B-eff, P-D-scope, P-F-dep) |
| CONTRAST_GROUPS | **2** (CG-E-out, CG-E-sup) |
| DUAL_CHECK_SAME_WORLD_GROUPS | **2** (B-04↔B-02; C-01/C-02) |
| CONDITION_LATTICES | **0 CORE** (former G-01..G-03 → NX) |
| ROLE_ALIASES | **1** (J-02 → G-04) |
| POSITIVE_CONTROL_PHYSICAL_FIXTURES | **5** |
| POSITIVE_CONTROL_ROLE_TAGS | **1** (J-02) |
| NX_CASES | **2** (E1-E-NX, E1-G-NX) |

### Positive-control physical fixtures (exact)

1. `E1-B-02` (boundary qualify)  
2. `E1-B-03` (post-boundary qualify)  
3. `E1-D-03`  
4. `E1-G-04`  
5. `E1-J-01`  

→ **POSITIVE_CONTROL_PHYSICAL_FIXTURES = 5**  
→ **POSITIVE_CONTROL_ROLE_TAGS = 1** (`E1-J-02`)

### Physical CORE inventory (19)

A-01; B-01, B-02, B-03; C-01, C-02; D-01, D-02, D-03; E-01, E-02, E-03; F-01, F-02; G-04; H-01; I-01; J-01.

Note: C-01 and C-02 share one world but are listed as two dual-check physical entries for artifact packaging; taxonomy marks them `DUAL_CHECK_SAME_WORLD` (not TRUE_PAIRWISE). If a future freeze collapses them to one physical package, recount accordingly — this candidate keeps two named entries with shared-world note.

**Conservative physical-evidence count if C is collapsed:** 18.  
**This candidate’s declared PHYSICAL_CORE_FIXTURES = 19** (named entries above).

---

## Family × case map

| Case ID | Family | Kind | Category | Primary H | Group | Notes |
|---------|--------|------|----------|-----------|-------|-------|
| E1-A-01 | A | PHYSICAL | NEG | H1 | — | exact retracted/superseded/current |
| E1-B-01 | B | PHYSICAL | NEG | H2 | P-B-eff | premature activation; e1b-0 still current |
| E1-B-02 | B | PHYSICAL | POS | H2 | P-B-eff | at boundary; e1b-1 current |
| E1-B-03 | B | PHYSICAL | POS | H2 | P-B-eff | after; e1b-1 current |
| E1-B-04 | B | ROLE_OR_CHECK | BOUNDARY_CHECK | H2 | dual of B-02 | exclusive valid_to; **not** independent |
| E1-C-01 | C | PHYSICAL* | NEG | H6 | dual-C | late record must not outrank |
| E1-C-02 | C | PHYSICAL* | NEG/POS | H6 | dual-C | e1c-new remains current |
| E1-D-01 | D | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch EU |
| E1-D-02 | D | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch canary |
| E1-D-03 | D | PHYSICAL | POS | H3/H10 | P-D-scope | US qualifies |
| E1-E-01 | E | PHYSICAL | NEG | H4 | CG-E-scope | **scope_mismatch** (not jurisdiction) |
| E1-E-02 | E | PHYSICAL | NEG | H4 | CG-E-out | refused |
| E1-E-03 | E | PHYSICAL | NEG | H4 | CG-E-sup | superseded |
| E1-E-NX | E | NX | NX | H4 | — | precedence underdefined |
| E1-F-01 | F | PHYSICAL | EXPECTED_FAIL_CLOSED | H5 | P-F-dep | S4 fail-closed → fixture PASS |
| E1-F-02 | F | PHYSICAL | NEG/UNKNOWN | H9 | P-F-dep | optional uncertainty UNKNOWN |
| E1-G-NX | G | NX | NX | H7 | — | compound condition evaluation |
| E1-G-04 | G | PHYSICAL | POS | H7/H10 | — | new-version path return |
| E1-H-01 | H | PHYSICAL | NEG | H8 | — | preserve distinct observations |
| E1-I-01 | I | PHYSICAL | NEG | H8/H1 | — | no same-ID revival |
| E1-J-01 | J | PHYSICAL | POS | H10 | — | straightforward approve |
| E1-J-02 | J | ROLE_ALIAS | POS tag | H10 | → G-04 | not independent |

\*C-01/C-02: `DUAL_CHECK_SAME_WORLD`.

No `POS-ish/NEG` labels remain.
