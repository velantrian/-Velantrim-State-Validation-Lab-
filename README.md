# 🔬 Velantrim State Validation Lab 👨‍🔬

> **Standalone research architecture for studying how persistent state can evolve, conflict, expire, be erased, restored, replayed, and audited over time without losing provenance, scope, applicability, continuity, or causal explainability.**

**Status:** `FOUNDATION v0.2 · RESEARCH ARCHITECTURE · NOT PRODUCTION AUTHORITY`

**Runtime authority:** `FALSE` · **Canon authority:** `FALSE` · **Action authority:** `FALSE` · **Production authorization:** `FALSE`

## 🧠 What this project is

Velantrim State Validation Lab is **one coherent research system**, not a directory of other Velantrim projects.

It abstracts the strongest ideas developed across the wider Velantrim research ecosystem—provenance, evidence, bounded authority, temporal memory, correction, continuity, replay, deletion, restore, composition, and falsification—into a single architecture for studying one problem:

> **Can long-lived state change, be corrected, forgotten, restored, and continued without losing meaning, origin, scope, current applicability, and explainability?**

The Lab studies not only **what state exists now**, but **how that state arrived here and why it is still allowed to influence the present**.

## 🏛️ Core architecture

The system is organized as a set of interacting research planes:

```text
Source / Event / Observation
          ↓
Capture & Source Binding
          ↓
Semantic Separation
          ↓
Governed State Record
      ↙               ↘
Temporal &         Scope &
Relation Graph     Applicability
      ↘               ↙
       Continuity Engine
              ↓
          Return Arc
 update / retract / erase /
 restore / replay / compensate
              ↓
   Causal Trace & Evidence Ledger
              ↓
      Falsification Engine
              ↓
 PASS / FAIL / UNKNOWN / BLOCKED
              ↓
       Research Decision Gate
```

### 🧩 Semantic Plane

Keeps different state meanings separate:

```text
Observation ≠ Claim ≠ Evidence ≠ Belief
≠ Permission ≠ Commitment ≠ Process State
```

The architecture can relate these objects, but does not silently convert one into another.

### 🛡️ Governance / Applicability Plane

Studies **why a stored state is still applicable**:

- source / actor / principal;
- scope;
- operation and resource;
- temporal validity;
- revocation and expiry;
- delegation;
- scope expansion during transformation;
- whether persistent instructions can accidentally become autonomous authority.

Key boundary:

```text
persistent state ≠ permission to act
```

### 🕰️ Temporal & Mutation Plane

Treats state as a trajectory rather than a single row:

```text
create → update → contradict → supersede → retract
→ expire → revoke → erase → tombstone
→ restore candidate → reconcile
```

Important distinctions:

```text
newer ≠ automatically true
old ≠ automatically wrong
conflict ≠ overwrite
superseded ≠ deleted
erased value ≠ erased history
restore bytes ≠ restore semantic validity
```

### 🕸️ Relation & Derived-State Plane

Models how state depends on other state:

```text
DERIVED_FROM
SUPERSEDES / SUPERSEDED_BY
CONTRADICTS
CORRECTS
RETRACTS
DEPENDS_ON
SAME_SUBJECT
CAUSED_BY
```

This allows the Lab to test whether derived state, retrieval influence, summaries, or relations remain active after their source is corrected, revoked, or erased.

### 🌎 Continuity Plane

Studies state across:

- restart;
- context replacement;
- model/provider replacement;
- snapshot and restore;
- replay;
- handoff and rehydration;
- duplicate delivery;
- crash between transitions.

```text
capture
  ↓
durable state
  ↓
handoff / restart
  ↓
rehydration
  ↓
revalidate current applicability
  ↓
continuation
```

### ↩️ Return Arc

The Lab gives special attention to the often-weaker second half of persistent-state systems:

```text
Forward arc:
observe → write → validate → organize → retrieve → use

Return arc:
correct → supersede → retract → revoke → forget
→ erase → audit → restore / rollback / compensate
```

The core research question is not only whether a system can create state, but whether it can **stop relying on state correctly**.

### 🔗 Causal Trace

The target research trace is:

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

And the reverse audit path should answer:

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

Unknown causality must remain `UNKNOWN` or `DECLARED LOSS`, never invented.

## 📜 Evidence Ledger

Every experiment should be reproducible and record at least:

- experiment ID;
- architecture/version under test;
- exact initial state;
- transition sequence;
- injected failure or mutation;
- expected observable property;
- observed trajectory;
- provenance and retained evidence;
- result;
- failure point;
- unknowns and limitations;
- reproducibility data.

Result vocabulary:

```text
PASS
FAIL
UNKNOWN
NOT_APPLICABLE
BLOCKED
INSUFFICIENT_EVIDENCE
```

`UNKNOWN ≠ FAIL` and `PASS ≠ universal truth`.

## 🔬 Falsification Engine

The Lab is designed to attack its own assumptions with bounded adversarial scenarios:

1. **Stale Permission** — permission is revoked after a delayed commitment exists.
2. **Supersession** — old and new state compete for current applicability.
3. **Interrupted Deletion** — a crash occurs between erasure steps.
4. **Scope Leakage** — state from scope A attempts to influence B.
5. **Restart / Rehydration** — state survives process loss and continuation.
6. **Restore Resurrection** — an old snapshot attempts to revive erased/revoked state.
7. **Poisoned Durable State** — untrusted input attempts to gain durable influence.
8. **Duplicate Replay** — replay attempts to repeat a consequential effect.
9. **Causal Audit** — exact lineage to an outcome must be reconstructible.
10. **Long-Horizon Mutation** — many correction/conflict/retraction/erase/restore cycles.

Each experiment follows:

```text
GIVEN  controlled initial state
WHEN   an exact transition or failure occurs
THEN   an observable property must hold
```

## 🧭 Research Decision Gate

A failure does **not** automatically justify new architecture.

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

Only a reproducible failure can justify a new architectural hypothesis.

## 🧬 Three questions summarize the whole system

| Plane | Core question |
|---|---|
| 🧠 Meaning | What kind of state is this, and what does it mean? |
| 🛡️ Applicability | Why, for whom, where, and when may it influence anything? |
| 🕰️ Continuity | How does it change and remain explainable across time, failure, and recovery? |

Everything else—provenance, relations, replay, deletion, restore, causal trace, and falsification—serves these three questions.

## 🚫 Constitutional boundaries

The Lab is a standalone research architecture, but it is **not**:

- a production memory service;
- a Canon or truth authority;
- an identity authority;
- a permission issuer;
- an autonomous action runtime;
- a global rollback controller;
- a mandatory schema for the Velantrim ecosystem;
- a proven universal law of cognition.

It may later produce tested contracts or mechanisms, but only after experiments justify them.

## 🧪 First research wave

The first three high-information experiments are:

**🥇 Interrupted deletion convergence**  
Inject a fault after every deletion transition. Retry must converge to declared erasure or leave an explicitly discoverable incomplete state—never hidden partial semantics.

**🥈 Restore non-resurrection**  
Create a snapshot before revoke/erase/supersede. Restored bytes may exist, but current applicability must not return without reconciliation with later history.

**🥉 Cross-scope isolation**  
Create state in scope A. Scope B attempts to read, mutate, derive, delete, or replay it. Any scope expansion must be explicit and testable.

## ▶️ Executable research status

The first bounded executable layer implements **E6 — Restore Resurrection**
only. It is an owner-local, deterministic, in-memory falsification fixture:

```text
E6: SPECIFIED · IMPLEMENTED · EXECUTION RESULT BOUND TO EACH EVIDENCE LEDGER RUN
E3: SPECIFIED · NOT IMPLEMENTED · NOT EXECUTED
E4: SPECIFIED · NOT IMPLEMENTED · NOT EXECUTED
```

Run the standard-library test suite:

```bash
python -m unittest discover -s tests -p 'test_*.py' -v
```

See [`docs/EXECUTION_STATUS.md`](docs/EXECUTION_STATUS.md) for exact commands
and authority boundaries. This model is not a production schema, runtime,
truth engine, Canon, permission issuer, or rollback authority.

## 📚 Detailed architecture

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for the full research model and architectural rationale.

## 🔬 Research origin

This architecture was informed by the strongest state, evidence, continuity, identity, composition, and memory ideas developed across Velantrim research, then stress-tested against external work on always-on persistent state.

External research lens:

- *Always-On Agents: A Survey of Persistent Memory, State, and Governance in LLM Agents* — arXiv:2606.30306

---

> **Velantrim State Validation Lab studies how persistent state can live, change, conflict, be forgotten, restored, and continued over time without losing meaning, provenance, applicability boundaries, or explainability.**
