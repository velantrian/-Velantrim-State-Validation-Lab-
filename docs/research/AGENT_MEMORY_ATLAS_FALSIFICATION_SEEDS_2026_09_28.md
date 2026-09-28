# Agent Memory Atlas falsification seeds — 2026-09-28

**Status:** `RESEARCH SEEDS · NOT PREREGISTERED · NOT EXECUTED · NOT CANON`

Source: https://neoneye.github.io/agent-memory-atlas/

These seeds translate external memory-system patterns into bounded failure questions for SVL. They do not import any external architecture.

## Seed A — rejected-value resurrection

1. Admit proposition P from source S1.
2. Reject/correct P.
3. Re-process stale source material or equivalent text.
4. A new record ID for equivalent P is generated.

**Failure:** P becomes applicable again only because identity changed.

## Seed B — correction propagation

Create source -> summary -> relation -> retrieval projection.

Correct/retract the source.

**Failure:** any derived representation continues to influence current applicability without an explicit, inspectable exception.

## Seed C — retrieval abstention

Populate only stale/rejected/out-of-scope candidates.

**Expected candidate behavior:** retrieval may return no admissible state.

**Failure:** forced top-k inclusion injects disallowed state merely to satisfy non-empty retrieval.

## Seed D — negative retrieval assertion

For a declared forbidden set F:

```text
expected_relevant_state in retrieved/context
AND
F intersection retrieved/context = empty
```

A positive hit does not compensate for forbidden influence.

## Seed E — scope-aware re-extraction

Store a value in scope A, then run background extraction/indexing and query from scope B.

**Failure:** derived jobs silently widen applicability or identity scope.

## Existing overlap

SVL already studies restore resurrection, scope leakage, poisoned durable state, supersession and the return arc. These seeds should therefore be treated as refinements/recombinations until a distinct uncovered failure is demonstrated.

## Next step

Before any execution:
- map each seed to existing SVL experiment families;
- deduplicate against E3/E4/E6 and current return-arc coverage;
- preregister only genuinely distinct residuals.
