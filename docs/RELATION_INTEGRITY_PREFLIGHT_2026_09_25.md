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

## 2. Primary null

A minimal reconstruction path that receives the same source-bound observations will not materially outperform an ordinary model reconstruction at preventing unsupported relation promotion.

A null-preserving result is a valid research result.

No architectural benefit is assumed in advance.

## 3. Primary failure family

The initial fixture family should target only these transformations:

```text
AFTER           -> BECAUSE
LATER           -> SUPERSEDES
SIMILAR         -> SAME
NEW_STATEMENT   -> REJECTION_OF_OLD
SEQUENCE A->B   -> B->A
```

These are test families, not a complete relation taxonomy.

## 4. Fixture construction rule

Each fixture must have an arm-invariant source ledger.

For every fixture freeze:

```text
OBSERVATIONS
TEMPORAL ORDER
EXPLICIT RELATIONS PRESENT IN SOURCE
RELATIONS NOT ESTABLISHED BY SOURCE
SCOPE / QUALIFIERS
CURRENTNESS FACTS IF ANY
EXPECTED UNKNOWN LINKS
```

Gold must distinguish:

- `SUPPORTED_RELATIONS` — relations directly established by the frozen source;
- `UNSUPPORTED_CANDIDATES` — tempting but ungrounded stronger relations;
- `UNKNOWN_LINKS` — links for which the fixture does not establish a truth value;
- `FORBIDDEN_DIRECTION_INVERSIONS`;
- `SCOPE_BOUNDARIES`.

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

## 11. Scientific donors — bounded role only

Relevant donors informing the question:

- McCarthy & Hayes — persistence/change/frame-problem lineage.
- RIKEN/Higuchi et al. — relation/order fidelity can be vulnerable in human sequence memory.
- StateMem / A-TMA — current/historical/transition information can coexist and answer-time resolution can fail.

These sources motivate the question. They do not validate this fixture or prescribe its software implementation.

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
- a new relation ontology.

## 14. Overlap boundary

```text
Continuum Experiment 0 -> minimum sufficient process state
CLOS IR-01            -> value of supplied C/G/X/R for resumption
E0-B / U0b            -> USER act/boundary/typing reliability
Native Kernel         -> semantic/state invariants and falsification questions
SVL                    -> relation/applicability/causal-trace falsification
```

This preflight belongs in SVL only if the owner accepts the residual as distinct.

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

## 17. Next bounded action

Human/owner review of this preflight.

If accepted:
1. construct a tiny frozen fixture set;
2. freeze scoring;
3. only then decide whether a numbered SVL experiment is warranted.

If rejected or duplicate:
record the reason and close without creating a new experiment.
