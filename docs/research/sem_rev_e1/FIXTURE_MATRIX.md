# SEM-REV-E1 — Fixture Matrix (E0-compatible final cleanup)

**STATUS:** preregistration candidate · **NOT FROZEN**

```text
E0 status vocabulary only: current | not_current | retracted | superseded
TEMPORAL REASON ≠ NEW STATUS PRIMITIVE
```

---

## Counts (recomputed)

| Metric | Count |
|--------|------:|
| **PHYSICAL_CORE_FIXTURES** | **18** |
| **CORE_ROLE_OR_CHECK_ENTRIES** | **20** (= 18 physical + C-02 + J-02) |
| TRUE_PAIRWISE_COUNTERFACTUAL_GROUPS | **2** (P-B-eff, P-D-scope) |
| CONTRAST_GROUPS | **3** (CG-E-out, CG-E-sup, CG-F-dep) |
| DUAL_CHECK_SAME_WORLD_GROUPS | **1** (C-02 ↔ C-01) |
| ROLE_ALIASES | **1** (J-02 → G-04) |
| POSITIVE_CONTROL_PHYSICAL_FIXTURES | **6** (B-02, B-03, D-03, F-02, G-04, J-01) |
| POSITIVE_CONTROL_ROLE_TAGS | **1** (J-02) |
| NX_CASES | **2** |

### Physical CORE inventory (18)

`E1-A-01`, `E1-B-01`, `E1-B-02`, `E1-B-03`, **`E1-B-04`**, `E1-C-01`, `E1-D-01`, `E1-D-02`, `E1-D-03`, `E1-E-01`, `E1-E-02`, `E1-E-03`, `E1-F-01`, `E1-F-02`, `E1-G-04`, `E1-H-01`, `E1-I-01`, `E1-J-01`

**Role/check only:** `E1-C-02`, `E1-J-02`

---

## Case map

| Case ID | Kind | Category | Primary H | Group | Notes |
|---------|------|----------|-----------|-------|-------|
| E1-A-01 | PHYSICAL | NEG | H1 | — | explicit as/dec; exact statuses |
| E1-B-01 | PHYSICAL | NEG | H2 | P-B-eff | e1b-0 current; e1b-1 not_current |
| E1-B-02 | PHYSICAL | POS | H2 | P-B-eff | e1b-0 superseded; e1b-1 current |
| E1-B-03 | PHYSICAL | POS | H2 | P-B-eff | same statuses post-boundary |
| E1-B-04 | PHYSICAL | NEG | H2 | — | isolated valid_to; no supersession |
| E1-C-01 | PHYSICAL | NEG | H6 | dual-C | late-arrival world |
| E1-C-02 | ROLE_OR_CHECK | BOUNDARY_CHECK | H6 | dual-C | v2 current check |
| E1-D-01 | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch EU |
| E1-D-02 | PHYSICAL | NEG | H3 | P-D-scope | scope_mismatch canary |
| E1-D-03 | PHYSICAL | POS | H3/H10 | P-D-scope | US qualifies |
| E1-E-01 | PHYSICAL | NEG | H4 | CG-E-scope | scope_mismatch |
| E1-E-02 | PHYSICAL | NEG | H4 | CG-E-out | refused |
| E1-E-03 | PHYSICAL | NEG | H4 | CG-E-sup | superseded; refused current |
| E1-E-NX | NX | NX | H4 | — | approved vs refused |
| E1-F-01 | PHYSICAL | EXPECTED_FAIL_CLOSED | H5 | CG-F-dep | missing only dec:e1f-auth |
| E1-F-02 | PHYSICAL | POS | H9 | CG-F-dep | single-valued QUALIFIED + UNKNOWN |
| E1-G-NX | NX | NX | H7 | — | compound condition |
| E1-G-04 | PHYSICAL | POS | H7/H10 | — | new-version path return |
| E1-H-01 | PHYSICAL | NEG | H8 | — | evidence owns observed_at |
| E1-I-01 | PHYSICAL | NEG | H8/H1 | — | evidence+link for new obs |
| E1-J-01 | PHYSICAL | POS | H10 | — | straightforward approve |
| E1-J-02 | ROLE_ALIAS | POS | H10 | → G-04 | not independent |

### TRUE_PAIRWISE

| Group | Cases | Δ |
|-------|-------|---|
| P-B-eff | B-01 / B-02 / B-03 | query_as_of only |
| P-D-scope | D-01 / D-02 / D-03 | query_scope only |

B-04 is **not** in P-B-eff (separate isolated world).
