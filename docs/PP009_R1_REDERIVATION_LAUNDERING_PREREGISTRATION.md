# PP009-R1 — Re-derivation Laundering Preregistration

**Date:** 2026-09-16  
**Status:** `PREREGISTRATION CANDIDATE · SPECIFIED ONLY`  
**Implementation:** `NOT IMPLEMENTED`  
**Execution:** `NOT EXECUTED`  
**Authority:** `RESEARCH ONLY · NONE`  
**Experiment authorization:** `NOT AUTHORIZED BY THIS DOCUMENT`

## 0. Purpose

This document preregisters one bounded falsification target recovered from the
PP-009 residual review:

> Can semantically non-current state regain current influence merely because an
> older source is legally re-ingested or a derived surface is rebuilt?

The target is **re-derivation laundering**: a system correctly records a
supersession or rejection, but later reconstruction from still-available older
source material silently makes the old semantic content current again.

This preregistration does **not** claim that such a defect exists in Crystal or
State Validation Lab. It defines a falsifiable test before any implementation or
execution is authorized.

```text
old evidence remains available
!= old claim becomes current again

historical retrievability
!= current applicability

re-ingestion
!= rehabilitation

rebuild
!= authority reset
```

## 1. Research boundary

PP009-R1 is a **single bounded experiment family**. It does not create a new
memory subsystem, ledger, owner, ontology, Canon authority, runtime authority, or
production mechanism.

The experiment is designed to distinguish three properties:

1. **history preservation** — old state remains attributable and auditable;
2. **current applicability preservation** — old state remains non-current after
   a governed supersession/rejection;
3. **positive current-state capability** — the system can still admit a genuinely
   eligible later state, so an always-empty/always-deny implementation cannot
   receive a misleading pass.

## 2. Source baselines

### State Validation Lab baseline

Preregistration branch starts from:

```text
repository: velantrian/-Velantrim-State-Validation-Lab-
base main: 665068d114d6f7fc235ad98c4e6d44c9c56d6512
```

Relevant existing research semantics already include:

- E2 — Supersession;
- E6 — Restore Resurrection;
- E10 — Long-Horizon Mutation;
- the Return Arc principle that state must be able to stop influencing the
  present without erasing historical explanation.

PP009-R1 is therefore an adversarial specialization of existing Lab semantics,
**not E11 and not a new architecture plane**.

### Crystal comparator baseline

Current comparator checkpoint at preregistration time:

```text
repository: velantrian/velantrim-exocortex-crystal
main: 3ed3a53ee9b8445a5f2ebf16046f782a3095555e
```

Relevant current/frozen surfaces include:

- `docs/CONTRADICTION_POLICY.md` — governed supersession and explicit no-winner
  semantics;
- `docs/research/MEMORY_EVAL_ADVERSARIAL_PROFILE_V0.md` — research-only
  re-ingest/rebuild resurrection-resistance scenario;
- `docs/STATUS.md` — current authority and evidence-standing boundaries.

Crystal is a **comparator/evidence source**, not execution authority for this Lab
experiment. PP009-R1 does not modify Crystal.

## 3. Target property

### Primary property

After a state item becomes non-current through an explicit governed disposition,
subsequent legal reprocessing of its old source must not, by itself, restore that
item's current applicability.

Formally, for old claim `C_old`, old source `S_old`, and a later governed
non-current disposition `D`:

```text
CURRENT(C_old, T1) = true
D(C_old, T2)       = non-current
REPROCESS(S_old, T3)

must not imply:
CURRENT(C_old, T4) = true
```

unless an explicit, independently qualifying rehabilitation/admission event is
present after `D`.

### What this is not

This is not a test that old content disappears. Historical state may remain
stored, retrievable for audit, or linked by lineage.

This is not a test that repetition is forbidden. The same proposition may be
legitimately observed again if the declared policy permits it and the later event
carries the required independent grounds.

This is not a claim that supersession and rejection are identical. They are two
dispositions sharing the same residual risk: stale semantic influence can be
laundered through reconstruction.

## 4. Frozen terminology

For this experiment:

- **current** — eligible to influence the declared current projection/decision
  surface under the experiment's frozen rules;
- **historical** — retained for provenance/audit but not current influence;
- **re-ingest** — process the same old source again through the allowed input path;
- **rebuild** — reconstruct a permitted derived/index/projection surface from
  available durable inputs;
- **rehabilitation** — an explicit later governed event that is independently
  sufficient to make a previously non-current proposition eligible again;
- **laundering** — current eligibility is restored without such an explicit
  qualifying event, solely because old source material was reprocessed.

`same text != same semantic standing`.

## 5. Frozen case matrix

The minimum implementation must contain all three cases below. No extra case may
be used to rescue a failing primary case after results are observed.

### R1-A — Superseded-source re-derivation

```text
T0  ingest S_old -> C_old
T1  C_old is current
T2  ingest/establish C_new
T3  governed supersession: C_new supersedes C_old
T4  close durable state
T5  open a fresh process / rehydrate
T6  legally re-ingest S_old
T7  rebuild permitted derived/current projection surfaces
T8  retrieve + qualify/project current knowledge
```

Required observations:

```text
C_old historical lineage = reachable
C_old current eligibility = false
C_new current eligibility = true
supersession relation/disposition = reachable
```

Primary forbidden outcome:

```text
S_old reprocessed -> C_old silently current again
```

### R1-B — Rejected-source re-derivation

```text
T0  ingest S_bad -> C_bad candidate
T1  explicit governed rejection/non-admission of C_bad
T2  close durable state
T3  open a fresh process / rehydrate
T4  legally re-ingest the same S_bad
T5  rebuild permitted derived/current projection surfaces
T6  retrieve + qualify/project current knowledge
```

Required observations:

```text
rejection/non-admission evidence = reachable
C_bad current eligibility = false
historical/audit trace = preserved to the extent declared by the model
```

Primary forbidden outcome:

```text
same rejected source -> reconstructed claim -> current eligibility
without a new qualifying ground
```

If the reference model has no explicit rejected-state primitive at implementation
time, this case must be reported `BLOCKED` rather than emulated with a different
state and mislabeled as rejection.

### R1-C — Positive-control lawful update

This case prevents an always-empty/always-deny system from passing.

```text
T0  establish current C_old
T1  govern C_old non-current through supersession/rejection as applicable
T2  introduce genuinely new eligible evidence/event S_new for C_valid
T3  perform the declared governed admission/currentness transition
T4  close + fresh-process reopen
T5  rebuild permitted derived/current projection surfaces
T6  retrieve + qualify/project current knowledge
```

Required observations:

```text
C_valid current eligibility = true
C_old/C_bad remains non-current unless explicitly rehabilitated
new provenance/ground = reachable
```

`S_new` must not be a byte-for-byte or identity-equivalent replay of `S_old`.

## 6. Fresh-process requirement

The primary evaluation must cross a durable boundary:

```text
WRITE / DISPOSITION
-> CLOSE
-> NEW PROCESS
-> REOPEN
-> RE-INGEST / REBUILD
-> QUALIFY
-> PROJECT
```

Passing only in one in-memory session is insufficient for the stated residual.

The implementation may use a deterministic local reference model, but transient
Python object identity or hidden process memory must not carry the answer across
the close/reopen boundary.

## 7. Required observable outputs

Each case must emit enough structured evidence to independently determine:

```text
case_id
input/source identities
state/claim identities
transition sequence
disposition event
fresh-process boundary
re-ingest event
rebuild event
current eligible ids
historical/non-current ids
provenance/lineage reachability
explicit rehabilitation event, if any
result
failure_reason
limitations
exact code/test revision
```

The scorer must not infer a hidden disposition from prose. Required standing must
be observable from structured state or deterministic queries.

## 8. Result rule

### `PP009_R1_PASS`

Only if all executable required cases satisfy their required observations and:

- R1-A does not resurrect `C_old`;
- R1-B does not resurrect `C_bad` when the rejection primitive is implemented;
- R1-C successfully makes the genuinely eligible later state current;
- historical/provenance evidence required by the model remains reachable;
- no undeclared hidden state carries the disposition across restart.

### `PP009_R1_FAIL_REDERIVATION_LAUNDERING`

If a non-current old claim regains current eligibility solely because its old
source was re-ingested or a derived surface was rebuilt.

### `PP009_R1_FAIL_ALWAYS_EMPTY`

If stale state never becomes current but the positive-control eligible later
state also cannot become current.

### `PP009_R1_FAIL_LINEAGE_LOSS`

If non-resurrection is achieved only by losing required historical
provenance/disposition lineage.

### `PP009_R1_BLOCKED`

If the reference model cannot represent a preregistered mandatory semantic state
without changing the experiment after observing outcomes.

### `PP009_R1_INSUFFICIENT_EVIDENCE`

If execution records are incomplete or cannot establish the current-vs-historical
standing deterministically.

A mixed or incomplete case set must not be summarized as PASS.

## 9. Anti-cheat / anti-confound rules

The implementation must not:

1. hard-code expected claim IDs into the currentness query;
2. delete all historical state merely to prevent resurrection;
3. treat retrieval absence alone as proof of non-currentness;
4. treat source repetition as new epistemic authority by default;
5. add a hidden blacklist after a result is observed;
6. silently convert `UNKNOWN` into non-current or current;
7. let timestamp recency alone choose current truth;
8. use an LLM judge where deterministic standing is available;
9. change case data, result thresholds, or disposition rules after first execution;
10. claim mechanism equivalence to Crystal from behavior alone.

## 10. Falsification logic

The experiment is intentionally able to fail the current research hypothesis.

A failure is scientifically useful if the system preserves history but allows
old semantic standing to return through legal reconstruction.

A PASS supports only this bounded statement:

> In the frozen reference model and preregistered cases, governed non-current
> standing survived fresh-process re-ingestion/rebuild without blocking a
> genuinely eligible later state.

It does **not** prove:

- universal semantic reversion resistance;
- correctness of Crystal runtime;
- correctness of every memory architecture;
- cognition, learning, or understanding;
- production safety;
- a need for event sourcing, graphs, or a new memory module.

## 11. Implementation gate

Before implementation, a separate review must confirm:

```text
PREREGISTRATION_FROZEN = YES
CASE_MATRIX_FROZEN = YES
RESULT_RULE_FROZEN = YES
REFERENCE_MODEL_MAPPING = REVIEWED
IMPLEMENTATION_AUTHORIZATION = EXPLICIT
```

This document alone does not authorize code, fixtures, workflows, execution, or
cross-project changes.

## 12. Current status

```text
PP009-R1 = SPECIFIED
PREREGISTRATION = CANDIDATE
IMPLEMENTATION = NOT_IMPLEMENTED
EXECUTION = NOT_EXECUTED
RESULT = NONE
ARCHITECTURE GAP = NOT_ESTABLISHED
NEW MODULE = NONE
PRODUCTION AUTHORIZATION = NO
CANON AUTHORITY = NO
```

The next bounded decision after review is either:

```text
FREEZE PREREGISTRATION
```

or:

```text
REVISE BEFORE FREEZE
```

—not implementation by default.
