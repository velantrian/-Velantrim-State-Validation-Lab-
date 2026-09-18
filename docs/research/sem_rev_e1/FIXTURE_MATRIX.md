# SEM-REV-E1 — Fixture Matrix (final pre-freeze tightening)

**STATUS:** preregistration candidate · **NOT FROZEN**  
**C1:** CLOSED · **C2–C12:** applied · **Final tightening:** this revision

---

## Taxonomy

| Term | Meaning |
|------|---------|
| PHYSICAL_CORE | Independent world-state counted as experimental evidence |
| ROLE_OR_CHECK | Additional required check/role on an existing physical fixture; **not** independent evidence |
| TRUE_PAIRWISE | Shared base; **exactly one** material semantic Δ; both sides explicit |
| CONTRAST_GROUP | Related opposing cases; **not** single-Δ pairwise |
| DUAL_CHECK_SAME_WORLD | Same physical bytes; multiple required check emphases |
| ROLE_ALIAS | Alternate role tag on one physical fixture |
| NX | `NOT EXPRESSIBLE UNDER CURRENT CONTRACT` |

Every category is **single-valued**. Banned: `NEG/POS`, `NEG/UNKNOWN`, `POS-ish/NEG`.

---

## Corrected counts

| Metric | Count |
|--------|------:|
| **PHYSICAL_CORE_FIXTURES** | **17** |
| **CORE_ROLE_OR_CHECK_ENTRIES** | **20** (= 17 physical + B-04 + C-02 check + J-02 alias) |
| TRUE_PAIRWISE_COUNTERFACTUAL_GROUPS | **2** (P-B-eff, P-D-scope) |
| CONTRAST_GROUPS | **3** (CG-E-out, CG-E-sup, **CG-F-dep**) |
| DUAL_CHECK_SAME_WORLD_GROUPS | **2** (B-04↔B-02; C-02↔C-01) |
| ROLE_ALIASES | **1** (J-02 → G-04) |
| POSITIVE_CONTROL_PHYSICAL_FIXTURES | **5** (B-02, B-03, D-03, G-04, J-01) |
| POSITIVE_CONTROL_ROLE_TAGS | **1** (J-02) |
| NX_CASES | **2** (E1-E-NX, E1-G-NX) |

### Physical CORE inventory (17) — exact

`E1-A-01`, `E1-B-01`, `E1-B-02`, `E1-B-03`, `E1-C-01`, `E1-D-01`, `E1-D-02`, `E1-D-03`, `E1-E-01`, `E1-E-02`, `E1-E-03`, `E1-F-01`, `E1-F-02`, `E1-G-04`, `E1-H-01`, `E1-I-01`, `E1-J-01`

**Not physical (role/check only):** `E1-B-04`, `E1-C-02`, `E1-J-02`

**C-01/C-02:** one physical world (`E1-C-01`); `E1-C-02` is dual-check only.

---

## Case map

| Case ID | Kind | Category | Primary H | Group | Notes |
|---------|------|----------|-----------|-------|-------|
| E1-A-01 | PHYSICAL | NEG | H1 | — | exact retracted/superseded/current |
| E1-B-01 | PHYSICAL | NEG | H2 | P-B-eff | e1b-0 still current |
| E1-B-02 | PHYSICAL | POS | H2 | P-B-eff | boundary; e1b-1 current |
| E1-B-03 | PHYSICAL | POS | H2 | P-B-eff | after; e1b-1 current |
| E1-B-04 | ROLE_OR_CHECK | BOUNDARY_CHECK | H2 | dual B-02 | exclusive valid_to |
| E1-C-01 | PHYSICAL | NEG | H6 | dual-C | late-arrival world (same-force decisions) |
| E1-C-02 | ROLE_OR_CHECK | BOUNDARY_CHECK | H6 | dual-C | v2 current check |
| E1-D-01 | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch EU |
| E1-D-02 | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch canary |
| E1-D-03 | PHYSICAL | POS | H3/H10 | P-D-scope | US qualifies |
| E1-E-01 | PHYSICAL | NEG | H4 | CG-E-scope | scope_mismatch |
| E1-E-02 | PHYSICAL | NEG | H4 | CG-E-out | refused |
| E1-E-03 | PHYSICAL | NEG | H4 | CG-E-sup | superseded; exact oracle |
| E1-E-NX | NX | NX | H4 | — | approved vs refused; no precedence |
| E1-F-01 | PHYSICAL | EXPECTED_FAIL_CLOSED | H5 | CG-F-dep | S4 fail-closed + hash gate |
| E1-F-02 | PHYSICAL | NEG | H9 | CG-F-dep | optional uncertainty UNKNOWN |
| E1-G-NX | NX | NX | H7 | — | compound condition |
| E1-G-04 | PHYSICAL | POS | H7/H10 | — | new-version path return; fully specified |
| E1-H-01 | PHYSICAL | NEG | H8 | — | preserve distinct observations |
| E1-I-01 | PHYSICAL | NEG | H8/H1 | — | no revival; new ID recoverable |
| E1-J-01 | PHYSICAL | POS | H10 | — | straightforward approve |
| E1-J-02 | ROLE_ALIAS | POS | H10 | → G-04 | not independent |

### TRUE_PAIRWISE (exactly one Δ)

| Group | Cases | Material Δ |
|-------|-------|------------|
| P-B-eff | B-01 / B-02 / B-03 | `query_as_of` only |
| P-D-scope | D-01 / D-02 / D-03 | `query_scope` only |

### CONTRAST_GROUPS (not single-Δ)

| Group | Cases | Why not pairwise |
|-------|-------|------------------|
| CG-E-out | E-02 | outcome contrast vs approved baseline |
| CG-E-sup | E-03 | supersession present |
| **CG-F-dep** | F-01 / F-02 | fail-closed dep loss vs optional UNKNOWN — **multiple** material deltas |
