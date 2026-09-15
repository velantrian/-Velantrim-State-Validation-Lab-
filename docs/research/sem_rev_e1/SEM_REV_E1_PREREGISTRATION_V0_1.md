# SEM-REV-E1 — Adversarial Robustness / Generalization
## Preregistration Candidate v0.1

**STATUS:** `PREREGISTRATION_CANDIDATE` — **NOT FROZEN**  
**DATE BASELINE:** 2026-09-15  
**MODE:** research design · falsification-first · docs-only · anti-drift  
**CORRECTION:** C1 applied 2026-09-15 against reviewed HEAD `1d572982cac9aaf068c3c2c16f5de3383e6c3b38`

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

### What E0 did **not** establish

- general semantic-memory correctness;
- robustness under deeper / adversarial histories;
- production suitability;
- graph-kernel unnecessary;
- general architecture validity.

### What this document is

A **falsification-first** research design + preregistration **candidate** for
SEM-REV-E1. It does **not** authorize:

- experiment execution;
- implementation change;
- freeze execution;
- S6 / S7 / Graph Kernel / Continuum / Crystal;
- architecture or canon promotion;
- merge.

---

## 1. Primary research question

Does the **same** bounded semantic-preservation principle remain valid when
input histories become adversarially more complex, **without** adding new
architectural machinery merely to rescue failing cases?

---

## 2. Central hypothesis

### H0-E1 (null / continuity)

The bounded deterministic semantic-preservation mechanism continues to
preserve required distinctions under adversarial variations of:

revision depth · temporal order · temporal overlap · scope similarity ·
authority conflict · evidence conflict · dependency loss · late-arriving
records · conditional reopen · UNKNOWN · positive controls.

### Explicit alternatives (failure classes)

| ID | Failure class |
|----|----------------|
| H1 | REVISION DEPTH FAILURE |
| H2 | TEMPORAL ORDERING FAILURE |
| H3 | SCOPE DISAMBIGUATION FAILURE |
| H4 | AUTHORITY CONFLICT FAILURE |
| H5 | DEPENDENCY INTEGRITY FAILURE |
| H6 | LATE-ARRIVAL FAILURE |
| H7 | REOPEN-CONDITION FAILURE |
| H8 | CONTRADICTORY-EVIDENCE FAILURE |
| H9 | UNKNOWN DISCIPLINE FAILURE |
| H10 | OVER-ABSTENTION / POSITIVE-CONTROL FAILURE |

Details: `HYPOTHESES_AND_FAILURE_MODES.md`.

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
NOT RETRIEVED ≠ ABSENT
UNKNOWN ≠ FALSE
CAPABILITY ≠ AUTHORITY
MODEL OUTPUT ≠ CANON
```

No new distinction is introduced merely because it sounds useful.

---

## 4. Architectural reuse policy

**Default assumption for E1 design:**

```text
NO NEW ORGAN
NO NEW ENGINE
NO NEW DATABASE
NO NEW LLM
NO GRAPH
NO NEW AUTHORITY MODEL
```

Reuse the verified E0 mechanism vocabulary.

If a proposed case requires an unregistered primitive → mark
`OUT_OF_CURRENT_E1_SCOPE` or `NOT EXPRESSIBLE UNDER CURRENT CONTRACT`.

Do **not** silently redesign E0.

Post-prereg audit (separate task) must decide:

- **A.** E0 implementation already supports E1 as-is;
- **B.** bounded fixture-loader / harness extensions only;
- **C.** a semantic capability is genuinely missing → scientific finding / boundary.

This candidate authorizes **none** of A/B/C implementation work.

---

## 5. Fixture suite overview

Approximately **10 families** (E1-A … E1-J), **22 CORE cases**, with pairwise
counterfactuals where one material property changes.

| Family | Focus | Hypotheses |
|--------|-------|------------|
| E1-A | Deep revision chain | H1 |
| E1-B | Temporal overlap / boundary | H2 |
| E1-C | Late-arriving record | H6, H2 |
| E1-D | Nearby / colliding scopes | H3 |
| E1-E | Conflicting authority decisions | H4 |
| E1-F | Required dependency loss vs optional UNKNOWN | H5, H9 |
| E1-G | Conditional reopen | H7 |
| E1-H | Contradictory evidence | H8 |
| E1-I | Retraction + late contradictory evidence | H8, H1 |
| E1-J | Positive controls | H10 |

Full matrix: `FIXTURE_MATRIX.md`  
Per-family specs: `fixtures/`

Entity / reason IDs are **new** (not E0 renames). Same contract, new histories.

---

## 6. Time axes (must remain distinct)

| Axis | Role |
|------|------|
| `observed_at` | when the phenomenon was observed |
| `asserted_at` | when the claim/decision was asserted |
| `recorded_at` | when the record entered the store |
| `valid_from` / `valid_to` | interval of temporal applicability |
| `effective_from` | when a revision relation takes effect |
| `query_as_of` | evaluation time `T` |

Currentness remains a **derived projection** (E0 rule), not a stored answer flag.

Temporal applicability at `T`:

```text
valid_from <= T
AND
(valid_to IS NULL OR T < valid_to)
```

Then revision state applies.

---

## 7. Scope / authority / UNKNOWN rules

- Scope identity is **exact**. Semantic similarity must not widen scope.
- Authority is typed; unauthorized / refused outcomes must not become approved.
- **No new authority hierarchy** is introduced in this candidate.
- If two authorities conflict and precedence is underdefined under current
  contract → case labeled `NOT EXPRESSIBLE UNDER CURRENT CONTRACT` (not
  silently given a winner).
- Intentional absence of an optional property → `UNKNOWN`.
- Missing **required** typed qualification dependency → stage failure / non-classifiable
  per contract (`DEPENDENCY LOSS ≠ VALID ABSENCE`).

---

## 8. Oracle isolation (design boundary only)

```text
SYSTEM UNDER TEST ≠ ANSWER KEY
```

Future E1 S0–S5 must not access REQUIRED / FORBIDDEN atoms, expected labels,
or gold structures. Oracle only after S5 bytes fixed + hashed.

See `ORACLE_ISOLATION.md`. **Not implemented in this task.**

---

## 9. Result labels

```text
SEM_REV_E1_CORE_PASS
SEM_REV_E1_CORE_FAIL
SEM_REV_E1_CORE_INCOMPLETE
```

No majority-pass. One CORE hard fail → `CORE_PASS` prohibited.

Per-fixture:

```text
FIXTURE_EXPECTATION = PASS | FAIL
```

### C1 — expected fail-closed ≠ experiment failure

E1-F-01 intentionally omits a **required** typed qualification dependency.
The preregistered outcome is **S4 fail-closed**.

If and only if that exact fail-closed outcome occurs:

```text
FIXTURE_EXPECTATION = PASS
```

This does **not** prohibit `SEM_REV_E1_CORE_PASS`.

```text
EXPECTED_FAIL_CLOSED ≠ EXPERIMENT_EXECUTION_FAILURE
EXPECTED_FAIL_CLOSED ≠ ordinary NO_QUALIFIED_RESULT
```

Unexpected pipeline / execution failure (crash, integrity abort, S4 FAIL on a
fixture that expected S4 PASS / S5) remains FAIL or INCOMPLETE.

The future execution protocol MUST process CORE fixtures **independently**, so
an expected fail-closed negative control cannot abort the suite.

Do **not** rewrite E1-F-01 as ordinary `NO_QUALIFIED_RESULT`.

See `PASS_FAIL_INCOMPLETE_RULES.md`.

---

## 10. Strongest allowed claim if PASS

> Across the frozen SEM-REV-E1 adversarial fixture suite, the bounded
> deterministic mechanism preserved the preregistered semantic distinctions
> under the tested revision, temporal, scope, authority, dependency,
> late-arrival, conflict, UNKNOWN, and reopen perturbations.

Even PASS does **not** claim universal correctness, production readiness,
human-like memory, unrestricted understanding, arbitrary domain
generalization, or that graph is unnecessary.

See `CLAIM_BOUNDARY.md`.

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
9. `fixtures/E1-A` … `E1-J`

---

## 12. Explicit non-goals

- Do not change frozen E0 evidence or the E0 scientific result.
- Do not invent hidden precedence to “solve” authority conflicts.
- Do not design oracle atoms from implementation outputs.
- Do not execute SQLite / S0–S5 / scorer in this candidate phase.
