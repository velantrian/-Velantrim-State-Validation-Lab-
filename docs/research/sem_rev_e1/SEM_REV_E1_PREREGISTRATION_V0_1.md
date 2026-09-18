# SEM-REV-E1 — Adversarial Robustness / Generalization
## Preregistration Candidate v0.1 (C1–C12)

**STATUS:** `PREREGISTRATION_CANDIDATE` — **NOT FROZEN**  
**DATE BASELINE:** 2026-09-15  
**MODE:** research design · falsification-first · docs-only · anti-drift  
**CORRECTIONS:** C1 CLOSED · C2–C12 applied · **final pre-freeze tightening** on `research/sem-rev-e1-prereg-v0.1`

---

## 0. Relation to E0

### Verified E0 baseline (live)

| Pin | Value |
|-----|-------|
| Freeze commit | `349243745ceadea691b9070e08c05e35d876c0ab` |
| Implementation commit | `6e523aae297cd0cbd1d3f777c672404248780f6e` |
| Result commit | `070513004b4e71a8bd788c532c95a0952613444f` |
| Run ID | `e0-v1-20260915T065633Z-dd69520c` |
| Classification | `SEM_REV_E0_CORE_PASS` |
| Prereg SHA-256 | `d4974ee709edc9d83018b53733542588469bcbe9cfa5089c39cbb9799eaad49a` |
| SQLite | `3.53.4` |

### What E0 established (bounded)

The frozen deterministic S0–S5 implementation preserved the tested semantic
distinctions on frozen Fixtures A/B/C under the specified SQLite 3.53.4
environment.

### What this document is

A falsification-first research design + preregistration **candidate** for
SEM-REV-E1. It does **not** authorize experiment execution, implementation,
freeze, S6/S7/Graph Kernel/Continuum/Crystal, architecture/canon promotion,
or merge.

---

## 1. Primary research question

Does the **same** bounded semantic-preservation principle remain valid when
input histories become adversarially more complex, **without** adding new
architectural machinery merely to rescue failing cases?

---

## 2. Central hypothesis

### H0-E1

Continuity under adversarial histories that are **expressible under the
current E0 contract**.

### Failure classes H1–H10

See `HYPOTHESES_AND_FAILURE_MODES.md` (H4/H7/H8 **narrowed** after C4–C6).

---

## 3. Fixed E0 distinctions (still in force)

```text
RETRIEVED ≠ QUALIFIED
QUALIFIED ≠ TRUE
PROPOSAL ≠ DECISION
OBSERVATION ≠ AUTHORIZATION
HISTORICAL ≠ CURRENT
SUPERSEDED ≠ FALSE
RETRACTED ≠ NEVER EXISTED
RETRACTED ≠ SUPERSEDED
NOT RETRIEVED ≠ ABSENT
UNKNOWN ≠ FALSE
CAPABILITY ≠ AUTHORITY
MODEL OUTPUT ≠ CANON
SCOPE ≠ JURISDICTION
HISTORICAL IDENTITY ≠ NEW CURRENT VERSION
REOPEN PATH ≠ REVIVE OLD ASSERTION/DECISION IDENTITY
PRESERVING DISTINCT OPPOSING OBSERVATIONS ≠ DERIVING A TYPED CONFLICT RELATION
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
```

---

## 4. Architectural reuse policy

```text
NO NEW ORGAN / ENGINE / DATABASE / LLM / GRAPH / AUTHORITY MODEL
```

If a case needs an unregistered primitive → `NOT EXPRESSIBLE UNDER CURRENT CONTRACT`.

Post-prereg audit (separate) may decide A/B/C about implementation support.
This candidate authorizes **none** of that work.

---

## 5. Fixture suite overview (final tightened counts)

| Metric | Count |
|--------|------:|
| PHYSICAL_CORE_FIXTURES | **17** |
| CORE_ROLE_OR_CHECK_ENTRIES | **20** |
| TRUE_PAIRWISE groups | **2** (P-B-eff, P-D-scope) |
| CONTRAST groups | **3** (CG-E-out, CG-E-sup, CG-F-dep) |
| DUAL_CHECK_SAME_WORLD groups | **2** |
| ROLE_ALIASES | 1 (J-02→G-04) |
| POSITIVE_CONTROL_PHYSICAL | 5 |
| NX_CASES | 2 (E1-E-NX, E1-G-NX) |

F-01/F-02 are **CONTRAST_GROUP** (not TRUE_PAIRWISE).  
C-01 is one physical late-arrival world; C-02 is dual-check only.  
Full matrix: `FIXTURE_MATRIX.md`.

---

## 6. Time axes

| Axis | Role |
|------|------|
| `observed_at` | when observed |
| `asserted_at` | when asserted |
| `recorded_at` | when entered store |
| `valid_from` / `valid_to` | applicability (`T < valid_to` when set) |
| `effective_from` | revision effect time |
| `query_as_of` | evaluation time `T` |

Currentness = derived projection, not stored answer flag.

---

## 7. Scope / authority / UNKNOWN / declared_loss

- Scope identity is **exact**. Similarity must not widen scope.
- `SCOPE ≠ JURISDICTION`. Principal names are not jurisdiction atoms.
- Authority outcomes/supersession are typed; refused must not flip to approved.
- No new authority hierarchy.
- Optional unspecified **uncertainty** → `UNKNOWN`.
- **`declared_loss`**: INTEGER `0` (no loss) / `1` (loss). **Not** `UNKNOWN`.
  Encoding unchanged from E0 schema (`DECLARED_LOSS_ENCODING_CHANGED = NO`).
- Missing **required** typed qualification dependency → preregistered
  **S4 fail-closed** (`EXPECTED_FAIL_CLOSED`). Exact fail-closed ⇒ fixture
  semantic PASS; does not by itself prohibit CORE_PASS; must not abort the suite.
- F-01: S4 fail-closed artifact must be fixed + SHA-256 verified **before**
  oracle (`EXPECTED_FAIL_CLOSED ≠ ORACLE_ISOLATION_BYPASS`). Unhashable S4 ⇒ INCOMPLETE.

---

## 8. Oracle isolation

```text
SYSTEM UNDER TEST ≠ ANSWER KEY
```

See `ORACLE_ISOLATION.md`. Not implemented here.

---

## 9. Result labels

```text
SEM_REV_E1_CORE_PASS
SEM_REV_E1_CORE_FAIL
SEM_REV_E1_CORE_INCOMPLETE
```

Fixture-level: `FIXTURE_SEMANTIC_PASS` / `FIXTURE_SEMANTIC_FAIL` /
`FIXTURE_EXPECTED_FAIL_CLOSED` / `EXECUTION_INTEGRITY_FAILURE`.

No majority-pass. See `PASS_FAIL_INCOMPLETE_RULES.md`.

---

## 10. Strongest allowed claim if PASS

See `CLAIM_BOUNDARY.md` (expressible-suite wording; excludes NX capabilities).

---

## 11. Companion documents

1. `HYPOTHESES_AND_FAILURE_MODES.md`
2. `FIXTURE_MATRIX.md`
3. `REQUIRED_ATOMS.md`
4. `FORBIDDEN_ATOMS.md`
5. `HARD_FAILS.md`
6. `ORACLE_ISOLATION.md`
7. `PASS_FAIL_INCOMPLETE_RULES.md`
8. `CLAIM_BOUNDARY.md`
9. `INTERNAL_CONSISTENCY_AUDIT.md`
10. `fixtures/E1-A` … `E1-J`

---

## 12. Explicit non-goals / NX boundaries

- Do not change frozen E0 evidence or the E0 scientific result.
- Do not invent hidden precedence / jurisdiction / condition flags.
- Do not design oracle atoms from implementation outputs.
- Do not execute SQLite / S0–S5 / scorer in this candidate phase.
- **NX:** `E1-E-NX` (authority precedence); `E1-G-NX` (compound reopen-condition evaluation).
