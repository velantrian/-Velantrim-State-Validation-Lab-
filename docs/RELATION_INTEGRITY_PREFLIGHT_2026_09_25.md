# Relation Integrity / Qualification — bounded preflight (2026-09-25)

**Status:** `RESEARCH PREFLIGHT · NO EXPERIMENT ID · NOT EXECUTED · NOT CANON · NOT RUNTIME AUTHORIZATION`

## 0. Why this preflight exists

The current Memory → Situation → Understanding checkpoint identified one residual that is not yet covered by an executable bounded fixture on State Validation Lab `main`:

> Can a system preserve what the source actually establishes without silently promoting temporal order, similarity, or later occurrence into a stronger relation?

This preflight stays inside the Lab's existing **Relation & Derived-State Plane**, **Scope & Applicability Plane**, **Causal Trace**, and **Falsification Engine**.

It does **not** create a new engine, owner, relation ontology, or production requirement.

```text
OBSERVED A
+ OBSERVED B
+ TEMPORAL ORDER
!=
SUPPORTED RELATION(A,B)
```

## 1. Research question

Given source-bound observations whose chronology is known but whose stronger relation is not established, can the tested reconstruction path:

1. preserve explicit relations that the source does establish;
2. preserve relation direction and scope;
3. leave unsupported relation candidates `UNKNOWN`;
4. avoid promotion from chronology/similarity/later occurrence into causality, supersession, rejection, refinement, or identity?

## 1A. Object separation — no silent epistemic promotion

The preflight must distinguish four objects that may refer to the same A/B pair but do not have the same epistemic meaning:

```text
OBSERVATION
!= SOURCE_ASSERTION
!= RELATION_CANDIDATE
!= RELATION_QUALIFICATION
```

A source statement such as:

```text
Paper P asserts: "A caused B"
```

licenses a source-bound fact:

```text
SOURCE_ASSERTION:
P asserts CAUSES(A,B)
```

It does **not** by itself license:

```text
WORLD_RELATION:
CAUSES(A,B) = SUPPORTED
```

A world-relation candidate must remain a separate derived object until a declared qualification step evaluates the available evidence, assumptions, identifiability conditions where relevant, and scope.

Primary invariant:

```text
NO SILENT PROMOTION BETWEEN
OBSERVATION
SOURCE_ASSERTION
RELATION_CANDIDATE
RELATION_QUALIFICATION
```

## 1B. Independent axes

The bounded research contract must not collapse these axes into one enum or label:

```text
RELATION_TYPE
!= DIRECTION
!= EVIDENCE
!= EVIDENCE_STRENGTH
!= ASSUMPTIONS
!= EPISTEMIC_STATUS
!= SCOPE
```

A valid intermediate state can therefore be:

```text
RELATION_TYPE_CANDIDATE = CAUSED_BY
DIRECTION               = A -> B
EVIDENCE_ITEMS          = [TEXTUAL_ASSERTION]
ASSUMPTIONS             = [not established]
EPISTEMIC_STATUS        = HYPOTHESIS
SCOPE                   = source P only
```

No combination of relation type, source count, chronology, or plausibility may manufacture a stronger epistemic status.

## 2. Primary null

A minimal reconstruction path that receives the same source-bound observations will not materially outperform an ordinary model reconstruction at preventing unsupported relation promotion.

A null-preserving result is a valid research result.

No architectural benefit is assumed in advance.

## 3. Primary failure family

The initial failure family is bounded to silent promotion and relation fidelity:

```text
F1  TEMPORAL ORDER          -> CAUSAL SUPPORT
F2  SOURCE ASSERTION        -> WORLD TRUTH
F3  MULTI-SOURCE AGREEMENT  -> CAUSAL IDENTIFICATION
F4  LATER                   -> SUPERSEDES
F5  NEW_STATEMENT           -> REJECTION_OF_OLD
F6  SIMILAR                 -> SAME
F7  SEQUENCE A->B           -> B->A
F8  RELATION CANDIDATE      -> SUPPORTED
F9  UNKNOWN                 -> FALSE
F10 SOURCE / MODEL ASSERTS  -> USER / PROJECT / CANON ACCEPTS
```

These are failure families, not a complete relation taxonomy.

The causal boundary is deliberately weaker than `NO INTERVENTION => ONLY HYPOTHESIS`.
The allowed research guard is:

```text
OBSERVATIONAL DATA ALONE
DOES NOT AUTOMATICALLY LICENSE CAUSALITY
```

A stronger scoped causal qualification may be possible only when its evidence, assumptions, identifiability conditions, method, and scope are explicit. Temporal adjacency, textual plausibility, and source repetition are never sufficient by themselves.

## 4. Fixture construction rule

Each fixture must have an arm-invariant source ledger.

For every fixture freeze:

```text
OBSERVATIONS
SOURCE_ASSERTIONS
TEMPORAL ORDER
EXPLICIT RELATION CANDIDATES
RELATIONS NOT ESTABLISHED
EVIDENCE ITEMS
ASSUMPTIONS
SCOPE / QUALIFIERS
CURRENTNESS FACTS IF ANY
EXPECTED UNKNOWN LINKS
FORBIDDEN PROMOTIONS
```

Gold must distinguish:

- `SOURCE_ASSERTIONS` — what a specific source explicitly says;
- `QUALIFIED_WORLD_RELATIONS` — only relations whose qualification is separately justified by the frozen contract;
- `UNSUPPORTED_CANDIDATES` — tempting but ungrounded stronger relations;
- `UNKNOWN_LINKS` — links for which the fixture does not establish a truth value;
- `FORBIDDEN_DIRECTION_INVERSIONS`;
- `SCOPE_BOUNDARIES`;
- `COUNTEREVIDENCE` where present.

A source assertion may itself be perfectly preserved while the corresponding world relation remains `UNKNOWN`.

Absence of a supported relation must **not** be reinterpreted as proof of the opposite relation.

```text
NOT ESTABLISHED != FALSE
UNKNOWN != FALSE
```

## 5. Minimal fixture examples

### F-A — temporal adjacency without causality

Source establishes:

```text
A happened.
Later B happened.
```

Source does not establish:

```text
A CAUSED B
B CAUSED A
```

Expected behavior: chronology preserved; causality remains `UNKNOWN`.

### F-B — later statement without supersession

Source establishes:

```text
At T1 the user considered option A.
At T2 the user discussed option B.
```

No cancellation / replacement statement is present.

Expected behavior: do not infer `B SUPERSEDES A`.

### F-C — similarity without identity

Source establishes two similar objects / claims.

Expected behavior: do not collapse them into `SAME` without identity evidence.

### F-D — new statement without rejection

Source establishes an earlier proposal and a later additional statement.

Expected behavior: do not infer that the later statement rejects the earlier proposal unless the source establishes rejection.

### F-E — direction fidelity

Source establishes `A -> B` in a declared relation or sequence.

Expected behavior: do not return `B -> A` unless the source independently establishes it.

### F-F — source assertion without world acceptance

Source establishes only:

```text
Paper P asserts "A caused B".
```

Expected behavior: preserve the assertion and its provenance; keep world-relation qualification separate.

### F-G — repeated assertion without causal identification

Several sources repeat the same observational association or causal wording without additional identifying evidence.

Expected behavior: source multiplicity is recorded as evidence metadata, not silently converted into causal entitlement.

### F-H — UNKNOWN preservation

A relation candidate exists but the frozen material does not establish its truth value.

Expected behavior: preserve `UNKNOWN`; do not emit `FALSE`, `SUPPORTED`, or an owner/user belief.

## 6. Conditions to compare

Freeze conditions only after fixtures exist.

Candidate comparison:

```text
A — ordinary reconstruction from frozen source material
B — reconstruction with explicit source-bound relation ledger
```

Do not add more arms unless they reduce a declared confound.

This is not a test of a new “relation engine”.

## 7. Primary outcome

### O1 — Unsupported Relation Promotion Rate

For each answer / reconstructed state:

```text
URPR =
unsupported stronger relation assertions
/
all scored relation opportunities
```

Primary success direction: lower is better.

A relation assertion counts as unsupported when it exceeds the frozen source ledger without an explicit `UNKNOWN / hypothesis / tentative` qualification allowed by the scoring contract.

## 8. Secondary outcomes

Score separately:

- **O2 Explicit relation preservation** — source-established relations retained correctly.
- **O3 Direction fidelity** — no A→B / B→A inversion.
- **O4 Scope fidelity** — relation scope not silently widened.
- **O5 UNKNOWN preservation** — underdetermined links remain underdetermined.
- **O6 False supersession rate**.
- **O7 False causality rate**.
- **O8 False rejection/refinement promotion rate**.
- **O9 Collateral currentness error** — relation handling must not corrupt otherwise correct current/historical state.
- **O10 Source/world separation accuracy** — source attribution is preserved without converting attribution into world truth.
- **O11 Status-transition violation rate** — candidate/status changes occur only through a declared qualification guard.
- **O12 Provenance completeness** — qualified or downgraded relations retain the trace needed to reconstruct why.
- **O13 Multi-source promotion error** — repeated assertions do not become stronger epistemic status merely by count.

Do not collapse these into one “understanding score”.

## 9. Result vocabulary

Use the Lab's existing vocabulary:

```text
PASS
FAIL
UNKNOWN
NOT_APPLICABLE
BLOCKED
INSUFFICIENT_EVIDENCE
```

Any PASS must be fixture- and model/run-family-bounded.

## 10. Required controls

Before execution:

1. Freeze source ledger and scoring rules before model outputs are observed.
2. Keep model-visible source identical across compared conditions except the declared relation-ledger treatment.
3. Do not expose gold-only relation labels to the tested model unless that exposure is the experimental factor.
4. Use a separate evaluator or deterministic scorer where possible.
5. Predeclare how tentative language is scored.
6. Predeclare ambiguous cases as `UNKNOWN` rather than forcing a relation class.
7. Record model/version, prompt, serializer, source fixture hash, evaluator version, and exact repo head.
8. Preserve negative / null results.
9. Record evidence items separately; do not use a compound state such as `MULTI_SOURCE_SUPPORTED`.
10. Predeclare the qualification transition that may change a relation candidate's epistemic status.
11. Preserve counterevidence and invalidation/reopen conditions when the fixture contains them.

## 10A. Evidence accumulation and qualification guard

Evidence is a collection of traceable items, not an epistemic conclusion:

```text
EVIDENCE_ITEMS[]
!= EVIDENCE_STRENGTH
!= EPISTEMIC_STATUS
```

Candidate evidence item kinds may include:

```text
TEXTUAL_ASSERTION
TEMPORAL_OBSERVATION
OBSERVATIONAL_ASSOCIATION
INDEPENDENT_REPLICATION
EXPERT_ANNOTATION
QUASI_EXPERIMENT
ENVIRONMENT_SHIFT
INTERVENTION
COUNTERFACTUAL_TEST
SYNTHETIC_GROUND_TRUTH
```

This list is fixture vocabulary only, not a universal evidence ontology.

Any transition such as:

```text
UNKNOWN -> HYPOTHESIS
HYPOTHESIS -> SUPPORTED
SUPPORTED -> CONTESTED / INVALIDATED
```

must be an explicit, traceable qualification event. No in-place silent overwrite is allowed.

## 10B. Bounded research-contract fields

For this preflight, the following are **REQUIRED NOW** as fixture/scoring concepts, not as a production schema:

```text
RELATION_ID
FROM
TO
RELATION_TYPE_CANDIDATE
DIRECTION
SOURCE_ASSERTIONS
EVIDENCE_ITEMS
ASSUMPTIONS
EPISTEMIC_STATUS
SCOPE
COUNTEREVIDENCE
PROVENANCE
```

**CONDITIONALLY REQUIRED** when a causal qualification is stronger than a source-bound hypothesis:

```text
IDENTIFIABILITY_CONDITIONS
METHOD
```

**OPTIONAL FOR THIS PREFLIGHT** unless a frozen fixture needs lifecycle change:

```text
PARENTS
VERSION
SUPERSEDES
INVALIDATED_BY
REOPEN_IF
```

**OUT OF SCOPE**:

- a universal Velantrim relation schema;
- a new relation/causal engine;
- a new authority owner;
- production persistence or runtime mutation.

The field split exists only to make silent promotion falsifiable.

## 11. Scientific donors — bounded role only

Relevant donors informing the question:

- McCarthy & Hayes — persistence/change/frame-problem lineage.
- RIKEN/Higuchi et al. — relation/order fidelity can be vulnerable in human sequence memory.
- StateMem / A-TMA — current/historical/transition information can coexist and answer-time resolution can fail.
- Causal-representation learning work — research donor for separating representation from causal entitlement, not a module or experiment owner.
- Manus review — engineering-contract donor for versioned derived objects, trace, guarded transitions, rollback, falsification, matched baseline/equal-budget/ablation discipline.

These sources motivate constraints. They do not validate this fixture, prescribe its software implementation, redefine Velantrim as an “epistemic state machine”, or authorize Manus-proposed experiment IDs.

IIT is used only as an overclaim boundary:

```text
SELF MODEL != CONSCIOUSNESS
INTEGRATED PROCESSING != CONSCIOUSNESS
CAUSAL STRUCTURE != CONSCIOUS EXPERIENCE
```

No Phi module, consciousness engine, IIT benchmark, or consciousness score belongs to this line.

## 12. Internal observations

Multi-AI research has repeatedly produced natural examples of:

- `AFTER -> BECAUSE`;
- project-history trajectories invented from chronological adjacency;
- later notes treated as replacement decisions;
- correct scientific result paired with wrong provenance/attribution;
- local result promoted to general mechanism.

These observations are fixture-seed material only, not independent scientific evidence.

## 13. Non-goals

This preflight does not test:

- truth adjudication in general;
- universal causal inference;
- semantic understanding as a whole;
- human consciousness;
- production authorization;
- goal-conditioned relevance;
- minimum sufficient process state;
- U0b typing/boundary reliability;
- CLOS IR-01;
- a new relation ontology;
- a Relation Engine, Causal Engine, CRL engine, Provenance Bus, or Epistemic Substrate service;
- Mentaury Soul ATR-v0.1 representation correctness as if it were a new SVL discovery.

## 14. Overlap boundary

Live overlap audit on 2026-09-25 found:

```text
Continuum Experiment 0
  -> minimum sufficient process state / currentness / provenance

CLOS IR-01 draft
  -> value of supplied CONTENT / GOAL / CONTEXT / RATIONALE for resumption

Eiti-Wizard-Lab E0-B
  -> raw USER semantic-act / authority typing reliability

Native Kernel ADR-0006
  -> accepted docs-only causal placement as typed directed relation;
     explicitly separates topology, epistemic status, evidence/provenance;
     no public causal runtime or contract tests recorded there

Mentaury Soul ATR-v0.1
  -> executable pure relation representation already tests:
     TEMPORAL != CAUSAL,
     CORRELATIONAL != CAUSAL,
     SOURCE_ASSERTED != relation truth,
     basis/source count != evidence support,
     UNKNOWN not implicitly upgraded,
     scope + orientation preservation
  -> intentionally does NOT perform Evidence Gate qualification or emit truth/support status

SVL
  -> owner for bounded relation/applicability/causal-trace falsification
```

Therefore this preflight is **PARTIAL_OVERLAP**, not a claim that relation separation is novel across Velantrim.

Do not duplicate Mentaury Soul's pure representation tests as a new mechanism. The residual retained here is narrower:

> Can a reconstruction / qualification path preserve source assertions and relation candidates while preventing evidence, repetition, chronology, or plausibility from silently promoting them into a stronger world-relation qualification?

This residual belongs in SVL only if the owner accepts that qualification question as distinct from already-tested relation representation.

## 15. Gate before experiment ID

No experiment ID is assigned by this document.

Promotion to a numbered executable experiment requires:

```text
FROZEN FIXTURE
+ FROZEN SCORING
+ DISTINCT_RESIDUAL CONFIRMED
+ OWNER DECISION
+ IMPLEMENTATION / EVIDENCE PLAN
```

Until then:

```text
STATUS = PREFLIGHT_ONLY
RUN_AUTHORIZED = FALSE
ARCHITECTURE_CONSEQUENCE = NONE
```

## 16. Falsification / downgrade conditions

Downgrade or stop this line if:

- existing SVL experiments already measure the same unsupported-relation failure under equivalent evidence;
- deterministic source qualification alone removes the failure without a new mechanism;
- fixtures cannot distinguish relation error from upstream typing/source-binding error;
- evaluator agreement is too weak to identify unsupported relation promotion;
- the effect disappears under matched source/prompt controls.

## 17. Owner decision and current bounded state

Owner decision on 2026-09-25:

```text
GO = FREEZE TINY FIXTURE + SCORING PACKAGE
GO != EXECUTION AUTHORIZATION
GO != MERGE AUTHORIZATION
GO != EXPERIMENT ID
GO != ARCHITECTURE PROMOTION
```

The bounded package now exists on this draft branch:

- `docs/RELATION_INTEGRITY_TINY_FIXTURE_SCORING_2026_09_25.md`;
- `fixtures/relation_integrity_qualification_v0_1.jsonl`.

Frozen first package:

```text
F-A  temporal adjacency without causality
F-F  source assertion without world acceptance
F-G  multi-source repetition without causal identification
F-H  UNKNOWN preservation
```

Primary metric:

```text
O1 Unsupported Relation Promotion Rate
```

Targeted secondary metrics only:

```text
O5  UNKNOWN preservation
O7  False causality
O10 Source/world separation
O13 Multi-source promotion error
```

The package deliberately does not pull all F1-F10 or O1-O13 into the first bounded test.

Current gate state:

```text
PARTIAL_OVERLAP DECLARED            = TRUE
OWNER GO TO FREEZE PACKAGE          = TRUE
FROZEN FIXTURE                      = PRESENT
FROZEN SCORING                      = PRESENT
DISTINCT_RESIDUAL CONFIRMED         = PENDING PACKAGE REVIEW
IMPLEMENTATION / EVIDENCE PLAN      = NOT CREATED
EXPERIMENT ID                       = NONE
RUN_AUTHORIZED                      = FALSE
MERGE_AUTHORIZED                    = FALSE
ARCHITECTURE_CONSEQUENCE            = NONE
```

## 18. Next bounded action

Review only the frozen fixture/scoring package.

Allowed review outcomes:

```text
ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING
REVISE_PACKAGE_BEFORE_EXECUTION_PLANNING
CLOSE_AS_DUPLICATE
```

Even `ACCEPT_PACKAGE_FOR_EXECUTION_PLANNING` does not authorize execution.

Do not assign an experiment ID, create runtime code, merge PR #4, or promote any architectural claim until that later gate is explicitly passed.
