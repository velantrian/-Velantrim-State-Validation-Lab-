# 🔬 Velantrim State Validation Lab 👨‍🔬 — Architecture

## 1. Purpose

Velantrim State Validation Lab is a **standalone research architecture** for studying long-lived persistent state as a governed trajectory rather than as a static memory item.

It asks one central question:

> **Can persistent state evolve, conflict, be corrected, revoked, erased, restored, replayed, and continued without losing meaning, provenance, scope, applicability, continuity, or causal explainability?**

The Lab is intentionally research-first. It does not own production truth, identity, permissions, actions, or global rollback authority.

## 2. Architectural premise

A persistent record is not sufficient by itself. Long-lived systems need to reason about:

- what the state means;
- where it came from;
- whether it is still current;
- who or what it applies to;
- what changed it;
- what depends on it;
- whether it may still influence a decision;
- what survives correction, deletion, restore, or replay;
- whether a later result can be traced back to its causal state.

The Lab therefore models state as a sequence of governed transitions.

```text
source / event / observation
          ↓
capture + source binding
          ↓
semantic separation
          ↓
governed state
       ↙         ↘
temporal graph   applicability envelope
       ↘         ↙
        continuity process
              ↓
          return arc
              ↓
       causal trace + evidence
              ↓
        falsification result
```

## 3. Semantic Plane

The system keeps distinct state kinds separate:

```text
Observation
Claim
Evidence
Belief
Permission
Commitment
Process State
Derived State
Relation
```

The core semantic boundary is:

```text
Observation ≠ Claim ≠ Evidence ≠ Belief
≠ Permission ≠ Commitment ≠ Process State
```

These objects may reference one another, but a reference is not a promotion.

### 3.1 Governed State Record

The Lab uses a conceptual governed-state model containing at least:

```text
identity
state kind
payload or content reference
source / provenance
temporal position
scope
applicability / authority class
lifecycle state
relations / derivations
retention / erasure semantics
transition history
known limits / declared loss
```

This is a research model, not a frozen storage schema.

## 4. Governance and Applicability Plane

Persistence does not imply applicability.

The Lab studies:

```text
actor / principal
source
scope
operation
resource / subject
temporal validity
expiry
revocation
delegation
policy version
known limitations
```

Primary boundaries:

```text
persistent state ≠ permission to act
permission ≠ identity
receipt ≠ authority
capability ≠ truth
delegation ≠ impersonation
```

A state may remain historically present while being no longer currently applicable.

## 5. Temporal and Mutation Plane

State is represented as a trajectory:

```text
create
update
reinforce
contradict
supersede
retract
expire
revoke
erase
tombstone
restore candidate
reconcile
```

The Lab preserves the following distinctions:

```text
newer ≠ automatically true
old ≠ automatically wrong
conflict ≠ overwrite
superseded ≠ deleted
erased value ≠ erased history
restore bytes ≠ restore semantic validity
```

### 5.1 Example trajectory

```text
S0: X = A
 ↓ new evidence
S1: conflict(A, B)
 ↓ validation
S2: B supersedes A
 ↓ erasure request
S3: A is no longer processable; minimal audit lineage remains
 ↓ old backup restored
S4: restored A exists only as stale candidate until reconciliation
```

## 6. Relation and Derived-State Plane

The Lab studies explicit relationships such as:

```text
DERIVED_FROM
SUPERSEDES
SUPERSEDED_BY
CONTRADICTS
CORRECTS
RETRACTS
DEPENDS_ON
SAME_SUBJECT
CAUSED_BY
```

Key research questions include:

- Which derived states depend on a deleted source?
- Which relations become stale after correction?
- What should stop influencing retrieval?
- What may remain solely as historical provenance?
- What information was lost during transformation?

Similarity, graph distance, or salience do not create truth or authority.

## 7. Continuity Plane

The Lab studies persistent state across:

- restart;
- handoff;
- model replacement;
- provider replacement;
- snapshot;
- restore;
- replay;
- duplicate delivery;
- crash between transitions;
- rehydration.

Core continuity path:

```text
capture
  ↓
durable state
  ↓
handoff / restart
  ↓
rehydration
  ↓
revalidation of current applicability
  ↓
continuation
```

Important distinctions:

```text
session resumed ≠ process continuity proven
snapshot restored ≠ authority restored
replay consistency ≠ truth
duplicate replay ≠ permission for duplicate effect
```

A simple snapshot or `state.json` representation remains a valid baseline. More complex event-sourced or graph mechanisms must earn their complexity through evidence.

## 8. Return Arc

The Lab gives equal attention to creation and relinquishment.

```text
Forward arc:
observe → write → validate → organize → retrieve → use

Return arc:
correct → supersede → retract → revoke → forget
→ erase → audit → restore / rollback / compensate
```

The central return-arc question is:

> **Can the system correctly stop relying on state that should no longer influence the present?**

Research probes include:

- source deletion with surviving derived state;
- stale commitments after permission revocation;
- restore after post-backup erasure;
- partial failure during deletion;
- audit retention without forbidden content retention.

## 9. Causal Trace

The Lab studies an explicit forward trace:

```text
source
  ↓
state
  ↓
transformation / derived state
  ↓
current applicability decision
  ↓
decision candidate
  ↓
attempted effect
  ↓
effect / denial
```

And the reverse audit path:

```text
effect / denial
  ↑
which decision?
  ↑
which applicability evidence?
  ↑
which state?
  ↑
which source?
```

Unknown links must remain `UNKNOWN` or `DECLARED LOSS` rather than being inferred as fact.

## 10. Evidence Ledger

Every experiment should record:

```text
experiment ID
architecture/version under test
initial state
exact transition sequence
fault / mutation injection
expected observable property
observed trajectory
retained provenance
result
failure point
unknowns / limitations
reproducibility information
```

Result vocabulary:

```text
PASS
FAIL
UNKNOWN
NOT_APPLICABLE
BLOCKED
INSUFFICIENT_EVIDENCE
```

Rules:

```text
UNKNOWN ≠ FAIL
PASS ≠ universal truth
one successful trajectory ≠ proof across all environments
```

## 11. Falsification Engine

The Lab is defined by adversarial scenarios, not by architecture enthusiasm.

### E1 — Stale Permission

A permission or applicability decision exists at T1, is revoked or expires at T2, and an old commitment attempts use at T3.

Expected property: current applicability must be re-evaluated.

### E2 — Supersession

Old and new state coexist.

Expected property: current applicability reflects validated supersession without rewriting history as if the old state never existed.

### E3 — Interrupted Deletion

A failure occurs after each deletion transition.

Expected property: retry converges or leaves explicitly detectable incomplete state; no hidden partial semantics remain.

### E4 — Scope Leakage

State in scope A is read, mutated, derived, replayed, or deleted from scope B.

Expected property: fail closed unless explicit scope transfer is present.

### E5 — Restart / Rehydration

Process memory is lost and durable state is reloaded.

Expected property: provenance and applicability survive without gaining authority.

### E6 — Restore Resurrection

A snapshot is created before later erase/revoke/supersede operations.

Expected property: restored bytes do not automatically regain current applicability.

### E7 — Poisoned Durable State

Untrusted state attempts to gain persistent influence.

Expected property: it remains untrusted/candidate unless independently admitted.

### E8 — Duplicate Replay

The same transition or event is replayed after crash/retry.

Expected property: no unintended duplicate consequential effect.

### E9 — Causal Audit

A significant result is produced.

Expected property: the exact state and applicability path can be reconstructed without invented links.

### E10 — Long-Horizon Mutation

Many correction, conflict, retraction, erase, restore, and replay cycles occur.

Expected property: state remains explainable and stale material does not silently regain influence.

## 12. Research Decision Gate

A failure is evidence, not authorization for redesign.

```text
FAIL
 ↓
REPRODUCE
 ↓
ISOLATE
 ↓
TRACE CAUSE
 ↓
CHECK EXISTING MECHANIC
 ↓
MINIMAL CHANGE OR NEW EXPERIMENT
 ↓
NEGATIVE REGRESSION
 ↓
RE-MEASURE
```

Only a reproducible failure that cannot be expressed or repaired by the current mechanic justifies a new architectural hypothesis.

## 13. Three Core Questions

The architecture can be compressed into three planes:

| Plane | Core question |
|---|---|
| 🧠 Meaning | What kind of state is this, and what does it mean? |
| 🛡️ Applicability | Why, for whom, where, and when may it influence anything? |
| 🕰️ Continuity | How does it change and remain explainable across time, failure, and recovery? |

All other mechanisms serve these questions.

## 14. Constitutional Boundaries

State Validation Lab is not:

- a production memory service;
- a Canon or truth authority;
- an identity authority;
- a permission issuer;
- an autonomous action runtime;
- a global rollback controller;
- a mandatory ecosystem-wide schema;
- a proven universal law of cognition.

It is a **research architecture and falsification environment**.

## 15. First Research Wave

The first research wave should focus on three high-information properties:

### 15.1 Interrupted deletion convergence

Inject a fault after every destructive transition. A retry must converge to declared erasure or expose explicit incomplete state.

### 15.2 Restore non-resurrection

Restore a snapshot created before later revocation, supersession, or erasure. Restored state must remain non-current until reconciliation.

### 15.3 Cross-scope isolation

Create state in scope A and attempt read/mutate/derive/delete/replay from B. Scope must never widen implicitly.

Only after these experiments should stale-permission, duplicate replay, causal audit, and long-horizon mutation be expanded.

## 16. Research Origin

This architecture abstracts strong recurring ideas from prior Velantrim research into one system:

- evidence, provenance, admission, correction, erasure, and recovery;
- bounded applicability, expiry, revocation, idempotency, and non-authorizing receipts;
- claim/belief/identity/permission/commitment separation;
- governed continuation, replay, redaction, and explainable change;
- capture → durable state → handoff → rehydration;
- semantic invariants, `UNKNOWN`, and falsification-first research;
- composition without automatic authority transfer and with declared loss;
- temporal graph and living memory without truth sovereignty.

The external Always-On Agents work is treated as a falsification lens, not as a target ontology or authority source.

---

> **Velantrim State Validation Lab studies how long-lived state can live, change, conflict, be forgotten, restored, replayed, and continued without losing meaning, provenance, applicability boundaries, or explainability.**
