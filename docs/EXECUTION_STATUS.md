# Execution Status

> This document tracks, per Falsification Engine experiment (E1-E10,
> see [`ARCHITECTURE.md`](ARCHITECTURE.md)), whether the experiment is
> merely `SPECIFIED` in prose, or has been made `IMPLEMENTED` and
> `EXECUTED` against a deterministic reference model.
>
> None of these labels are a claim of production readiness. See
> [Constitutional boundaries](../README.md#-constitutional-boundaries).

## Labels used

| Label | Meaning |
|---|---|
| `SPECIFIED` | Described in `ARCHITECTURE.md` only; no code exists. |
| `IMPLEMENTED` | A deterministic reference-model mechanism and tests exist. |
| `EXECUTED` | Tests have been run and produced Evidence Ledger records. |
| `NOT_PRODUCTION_AUTHORIZED` | Applies to every row below, unconditionally. |

This project never uses the words "validated", "proven", "safe", or
"production ready" for any row in this table.

## Experiment status

| Experiment | Status | Reference model | Tests | Evidence |
|---|---|---|---|---|
| E6 — Restore Resurrection | `IMPLEMENTED`, `EXECUTED` | [`src/state_validation_lab/model.py`](../src/state_validation_lab/model.py) | [`tests/test_e6_restore_resurrection.py`](../tests/test_e6_restore_resurrection.py) | [`evidence/E6/`](../evidence/E6/) |
| E3 — Interrupted Deletion | `SPECIFIED` | not started | not started | none |
| E4 — Scope Leakage | `SPECIFIED` | not started (a minimal scope guard used by E6 restore/get operations exists as a building block; no dedicated E4 fixtures or tests exist yet) | not started | none |
| E1, E2, E5, E7-E10 | `SPECIFIED` | not started | not started | none |

All rows are `NOT_PRODUCTION_AUTHORIZED`.

## E6 — Restore Resurrection

**Core invariant under test:**

```text
RESTORED_BYTES != RESTORED_CURRENT_APPLICABILITY
```

**Result:** all five required deterministic cases (`E6-01`..`E6-05`),
plus one boundary case and one deterministic-replay case, are
`IMPLEMENTED` and `EXECUTED`, with `PASS` recorded in
[`evidence/E6/`](../evidence/E6/) for the five ledgered cases.

| Case | Transition sequence | Expected property | Result |
|---|---|---|---|
| E6-01 | create -> snapshot -> revoke -> restore | restored state is a stale candidate; applicability = false | `PASS` |
| E6-02 | create -> snapshot -> supersede -> restore (+ reconcile attempt) | old state does not replace validated current state | `PASS` |
| E6-03 | create -> snapshot -> erase -> restore | restored payload does not silently regain processability | `PASS` |
| E6-04 | restore -> explicit reconciliation | only explicit owner-local reconciliation may grant applicability | `PASS` |
| E6-05 | restore without reconciliation | fail closed / remain stale candidate | `PASS` |

**Reproduce:**

```bash
cd src-or-repo-root  # repository root
PYTHONPATH=src python3 -m unittest tests.test_e6_restore_resurrection -v
PYTHONPATH=src python3 -m unittest tests.test_evidence_ledger_schema -v
```

Re-running the suite regenerates the evidence JSON files in place
(deterministic content, aside from `repo_head`, which reflects the
git commit checked out at test-execution time).

**Known limitations (E6):**

- single-process, in-memory model only; no concurrent-writer
  interleaving, no persistence layer, no real clock;
- supersession lineage walk is tested to depth 2 (`A -> A2`); very
  long chains are explicitly deferred to E10 (Long-Horizon Mutation),
  which is out of scope for this wave;
- erasure is modeled as logical erasure (payload set to `None`);
  physical/cryptographic erasure is out of scope;
- `reconcile()`'s `rationale` is an unvalidated free-text string; no
  reviewer or approval workflow is modeled — this stays a research
  fixture, not a permission system.

## Native Kernel cross-check

See [`NATIVE_KERNEL_CROSS_CHECK.md`](NATIVE_KERNEL_CROSS_CHECK.md).
No material semantic conflict was found for E6; implementation
proceeded per the assignment's stop conditions.
