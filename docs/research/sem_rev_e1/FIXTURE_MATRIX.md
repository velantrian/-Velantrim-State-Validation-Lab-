# SEM-REV-E1 — Fixture Matrix

**STATUS:** preregistration candidate · NOT FROZEN  
**CORE suite:** 10 families · 22 cases  
**Design rule:** prefer pairwise counterfactuals (Δ = one material property)

Legend:
- **POS** = positive control / should qualify
- **NEG** = adversarial negative / must not wrongly qualify or must preserve distinctions
- **PAIR** = member of a counterfactual pair
- **NX** = `NOT EXPRESSIBLE UNDER CURRENT CONTRACT` (documented boundary; not a CORE hard-fail oracle)

---

## Summary counts

| Metric | Count |
|--------|------:|
| Fixture families | 10 |
| CORE cases | 22 |
| Positive controls | 3 |
| Negative / adversarial CORE cases | 19 |
| Pairwise counterfactual groupings | 8 |
| NX boundary cases (documented, non-CORE) | 1 |

---

## Family × hypothesis map

| Case ID | Family | Role | Primary H | Pair group | Notes |
|---------|--------|------|-----------|------------|-------|
| E1-A-01 | A Deep revision | NEG | H1 | — | A→B→C→D; D current |
| E1-B-01 | B Temporal | NEG | H2 | P-B-eff | query **before** effective_from |
| E1-B-02 | B Temporal | POS-ish/NEG | H2 | P-B-eff | query **at** effective_from |
| E1-B-03 | B Temporal | NEG | H2 | P-B-eff | query after; overlapping older interval still not current |
| E1-B-04 | B Temporal | NEG | H2 | P-B-bound | `valid_to` exclusive boundary (`T < valid_to`) |
| E1-C-01 | C Late arrival | NEG | H6 | P-C-rec | late-recorded older obs must not outrank |
| E1-C-02 | C Late arrival | NEG | H6 | P-C-rec | earlier-recorded newer decision remains current |
| E1-D-01 | D Scopes | NEG | H3 | P-D-scope | approve US; query EU → no widen |
| E1-D-02 | D Scopes | NEG | H3 | P-D-scope | approve US; query US-canary → no widen |
| E1-D-03 | D Scopes | POS | H3/H10 | P-D-scope | approve US; query US → qualify |
| E1-E-01 | E Authority | NEG | H4 | P-E-jur | out-of-jurisdiction “approve” must not qualify |
| E1-E-02 | E Authority | NEG | H4 | P-E-out | refused outcome must not flip to approved |
| E1-E-03 | E Authority | NEG | H4 | P-E-sup | superseded authority decision not current |
| E1-E-NX | E Authority | NX | H4 | — | two in-jurisdiction conflicting approvals, no typed precedence |
| E1-F-01 | F Dependency | NEG | H5 | P-F-dep | required dependency missing → stage FAIL path |
| E1-F-02 | F Dependency | NEG | H9 | P-F-dep | optional property absent → UNKNOWN (not FALSE) |
| E1-G-01 | G Reopen | NEG | H7 | P-G-re | condition unsatisfied |
| E1-G-02 | G Reopen | NEG | H7 | P-G-re | half of compound condition |
| E1-G-03 | G Reopen | NEG | H7 | P-G-re | full condition, **no** authority reapproval |
| E1-G-04 | G Reopen | POS | H7/H10 | P-G-re | full frozen reopen condition satisfied |
| E1-H-01 | H Evidence | NEG | H8 | — | conflicting evidence preserved; no auto-truth |
| E1-I-01 | I Retract+late | NEG | H8/H1 | — | new similar evidence ≠ revive retracted ID |
| E1-J-01 | J Positive | POS | H10 | — | straightforward current approved decision |
| E1-J-02 | J Positive | POS | H10 | — | legitimate reopen (alias of E1-G-04 expectations) |

Note: E1-J-02 shares semantic expectation with E1-G-04 but is listed as a
distinct positive-control **role** in the CORE suite (same fixture content
may be referenced once physically; see `fixtures/E1-J-POSITIVE_CONTROLS.md`).

**Physical CORE fixture specs counted as 22 rows above excluding NX;**  
E1-E-NX is boundary documentation only and is **not** required for CORE_PASS.

Adjusted CORE physical cases in `fixtures/`: **22** (A1, B1–B4, C1–C2, D1–D3,
E1–E3, F1–F2, G1–G4, H1, I1, J1) with J2 = cross-ref to G4.

---

## Pairwise deltas (exact material Δ)

| Pair | Cases | Material Δ only |
|------|-------|-----------------|
| P-B-eff | B-01 / B-02 / B-03 | `query_as_of` relative to same `effective_from` |
| P-B-bound | B-03 / B-04 | `query_as_of` vs exclusive `valid_to` |
| P-C-rec | C-01 / C-02 | which record is late-recorded vs current decision |
| P-D-scope | D-01 / D-02 / D-03 | `query_scope` only (`eu` / `us-canary` / `us`) |
| P-E-jur | E-01 vs expressible baseline | authority jurisdiction match |
| P-E-out | E-02 | `outcome=refused` vs would-be approved |
| P-E-sup | E-03 | supersession present vs absent |
| P-F-dep | F-01 / F-02 | required dep missing vs optional field UNKNOWN |
| P-G-re | G-01…G-04 | reopen-condition completeness / reapproval |

---

## Generalization (anti-memorization)

E1 entities / reasons differ from E0 (`ent:service:atlas`, `orion`, Path-A/B/C,
`VX-17`, etc.):

Examples: `ent:service:mira`, `ent:service:kepler`, `ent:project:nova`,
`scope:production-apac`, reason codes `R_E1_*`.

Chain lengths, temporal arrangements, and force combinations differ while
the **same** E0 semantic obligations remain.
