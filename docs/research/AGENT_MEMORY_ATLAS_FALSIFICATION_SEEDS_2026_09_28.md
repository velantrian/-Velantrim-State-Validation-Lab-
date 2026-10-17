# Agent Memory Atlas falsification seeds — 2026-09-28

**Status:** `RESEARCH SEEDS · DEDUPLICATED · NOT PREREGISTERED · NOT EXECUTED · NOT CANON · NO NEW EXPERIMENT ID`

Source: https://neoneye.github.io/agent-memory-atlas/

These seeds translate external memory-system patterns into bounded failure questions for SVL. They do not import any external architecture and do not create new experiment IDs or failure families.

Prior Atlas-related / pre-existing overlapping coverage already exists: 💠 Crystal `docs/research/MEMORY_EVAL_ADVERSARIAL_PROFILE_V0.md` ([PR #462](https://github.com/velantrian/velantrim-exocortex-crystal/pull/462)), 🧬 Native Kernel `docs/research/MEMORY_EVALUATION_PROTOCOL_V0.md`, and the 🕸 Graphiti Fractal Lab FM-13 → FM-16 Honest Empty line. This note therefore deduplicates against existing SVL experiments (`docs/ARCHITECTURE.md` §6 Relation and Derived-State Plane, §8 Return Arc, §11 E1–E10) before anything is preregistered.

## Source-fidelity note

Agent Memory Atlas's rejected-value mechanism keys a rejected value under a declared identity/normalization policy (for example scope + subject + predicate + normalized value).

```text
DECLARED NORMALIZED VALUE MATCH != ARBITRARY SEMANTIC PARAPHRASE MATCH
```

The source does not establish general semantic-equivalence blocking. Paraphrase matching is an **OPEN POLICY / SEPARATE TEST QUESTION** and is not part of any fixture below.

## Dedup matrix

| Item | Class | Relation to existing SVL coverage | Residual / disposition |
|---|---|---|---|
| **A. Fresh re-extraction / new-ID reassertion** | `DISTINCT_RESIDUAL — NARROW TRIGGER PATH` | overlaps E2 Supersession, E6 Restore Resurrection, E10 Long-Horizon Mutation, Return Arc; **not the same mechanism as E6** | E6 restores old snapshot bytes into quarantine and reconciles **by record ID** (`src/state_validation_lab/model.py` `restore()` / `reconcile()` look up `candidate.id`). This scenario instead creates a **new** record ID from stale retained source. Candidate for later preregistration; **do not automatically create a new E-ID.** |
| **B. Correction propagation / regeneration** | `PARTIAL_OVERLAP / EXISTING FAMILY REFINEMENT` | Relation & Derived-State Plane; Return Arc; E10; correction/supersession lifecycle (E2) | Residual: correction survives regeneration of materially influential derived artifacts. No new family. |
| **C. Retrieval abstention / forced top-k** | `EXISTING RESEARCH LINE / OWNER OUTSIDE SVL BY DEFAULT` | Graphiti FM-16 / Honest Empty (status `NOT_ESTABLISHED`); Crystal / retrieval evaluation | SVL participates only if tied to persistent-state applicability. Not a new SVL family. |
| **D. Negative retrieval assertion** | `METHOD, NOT FAMILY` | applies across existing experiments where relevant (E2, E4, E6, E7, E10) | Cross-cutting assertion form; always with a positive control. |
| **E. Scope-aware re-extraction** | `FULLY COVERED AS E4 VARIANT` | E4 Scope Leakage | Background extraction/indexing is only a concrete stimulus. No new family. |

## Seed A — fresh re-extraction / new-record-ID reassertion (distinct residual)

Fixture (declared matching rule, not paraphrase):

1. Admit value P.
2. Reject/correct P.
3. Retain stale source material.
4. Re-run extraction.
5. Produce new record ID P2 whose value matches P under a preregistered normalization/identity rule.
6. Test whether P2 regains current applicability.

**Failure:** P2 regains current applicability only because the record identity changed, without an explicit, inspectable reactivation basis.

**Negative/control case (essential):** If P is independently re-observed under a policy that explicitly permits reactivation/new evidence, the system must not blindly block it merely because an old value was rejected. (Compare Crystal profile §4: newly observed equivalent claim != resurrection of erased record identity/provenance.)

Owner split: Crystal / admission runtime = policy implementation; SVL = falsification; Native Kernel = semantic identity question only.

**Crystal prior-coverage note (read-only inspection, 2026-09-28, Crystal main `726b85e`):** exact normalized ingestion identity exists (`core/ingest_identity.py`, explicitly not semantic matching); `store_fact` preserves persisted epistemic state on conflict (`core/memory.py`); the normalized compatibility index resolves only `Validated` targets (`core/normalized_ingest_index.py`); explicit caller-supplied fact IDs bypass that index (`tests/test_dedup.py::test_explicit_custom_fact_id_does_not_use_normalized_legacy_index`); immune memory blocks by normalized pattern only for explicitly recorded threats (`core/immune.py`). No Crystal test was found for rejection/correction followed by a fresh extraction with a **different** record ID whose value matches under the declared rule. Status: `OPEN TEST GAP` — not claimed solved, not claimed failing.

Status: `NOT RUN · NOT PREREGISTERED · NO NEW E-ID YET`.

## Seed B — correction propagation / regeneration (existing-family refinement)

Create source -> summary -> relation -> retrieval projection.

Correct/retract the source, then regenerate the materially influential derived artifacts.

**Failure:** any derived representation continues to influence current applicability without an explicit, inspectable exception.

Maps to: Relation & Derived-State Plane; Return Arc; E10; E2 correction/supersession lifecycle. Refinement only.

## Seed C — retrieval abstention (routed comparison note)

Owner outside SVL by default: Graphiti FM-16 / Honest Empty (`NOT_ESTABLISHED`) and Crystal / retrieval evaluation.

Comparison stimulus: populate only stale/rejected/out-of-scope candidates.

**Failure (persistent-state framing only):** forced top-k inclusion injects state that is no longer currently applicable merely to satisfy non-empty retrieval.

**Positive control:** when admissible relevant state exists, the retrieval owner must be able to return it.

## Assertion form D — cross-cutting negative assertion

Method, not family. Apply across existing experiments where relevant.

For a declared forbidden set F:

```text
expected_relevant_state in retrieved/context
AND
F intersection retrieved/context = empty
```

A positive hit does not compensate for forbidden influence. Always include a positive control (expected relevant state present and required) so an always-empty system cannot pass.

## Seed E — scope-aware re-extraction (E4 variant)

Store a value in scope A, then run background extraction/indexing and query from scope B.

**Failure:** derived jobs silently widen applicability or identity scope.

Fully covered as an E4 Scope Leakage variant; background extraction/indexing is only a concrete stimulus.

## Next step

Before any execution:
- preregister only the genuinely distinct residual (Seed A), including its declared matching rule and the reactivation control case;
- treat B, D and E as refinements/stimuli within existing experiments;
- leave C with its retrieval owner unless tied to persistent-state applicability.

```text
NO NEW EXPERIMENT ID
NO NEW FAILURE FAMILY
NOT PREREGISTERED · NOT EXECUTED
```
