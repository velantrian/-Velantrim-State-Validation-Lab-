"""Minimal in-memory reference model for State Validation Lab experiments.

THIS MODEL IS:
    RESEARCH-ONLY

THIS MODEL IS NOT:
    - a production truth engine
    - a Canon
    - a permission issuer
    - an identity authority
    - an action authority
    - a runtime controller
    - a rollback authority
    - a production storage model

It is a deterministic fixture used to falsify or support the
Falsification Engine experiments described in docs/ARCHITECTURE.md
(E1-E10). It is not a frozen production schema and carries no
authority beyond this repository's own research scope.
"""

from __future__ import annotations

import copy
import itertools
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class LifecycleState(str, Enum):
    ACTIVE = "ACTIVE"
    SUPERSEDED = "SUPERSEDED"
    REVOKED = "REVOKED"
    ERASED = "ERASED"
    RESTORED_CANDIDATE = "RESTORED_CANDIDATE"
    RECONCILED_APPLICABLE = "RECONCILED_APPLICABLE"
    RECONCILED_STALE = "RECONCILED_STALE"


class ScopeViolation(Exception):
    """Raised when an operation targets a record outside the acting scope.

    Research-level applicability guard only; not a production
    authorization system.
    """


class ReconciliationError(Exception):
    """Raised when reconcile() is called without an explicit, owner-local rationale."""


@dataclass
class StateRecord:
    id: str
    payload: Any
    lifecycle_state: LifecycleState
    applicable: bool
    scope: str
    version: int
    provenance: tuple[str, ...] = field(default_factory=tuple)
    superseded_by: str | None = None
    erased: bool = False
    revoked: bool = False

    def copy(self) -> "StateRecord":
        return copy.deepcopy(self)


@dataclass(frozen=True)
class Snapshot:
    snapshot_id: str
    captured_state: StateRecord
    captured_version: int


class ResearchStateModel:
    """Deterministic, in-memory, owner-local reference model.

    No wall-clock time, randomness, network, or external storage is
    used, so a fixed call sequence always produces an identical
    resulting state (see tests/test_e6_restore_resurrection.py
    deterministic-replay case).
    """

    def __init__(self) -> None:
        self._records: dict[str, StateRecord] = {}
        self._snapshots: dict[str, Snapshot] = {}
        self._restored_candidates: dict[str, StateRecord] = {}
        self._counter = itertools.count(1)

    # -- internal helpers ---------------------------------------------

    def _require_scope(self, record: StateRecord, scope: str, op: str) -> None:
        if record.scope != scope:
            raise ScopeViolation(
                f"{op} denied: record scope={record.scope!r} != requesting scope={scope!r}"
            )

    def _get_active(self, id: str, scope: str, op: str) -> StateRecord:
        record = self._records.get(id)
        if record is None:
            raise KeyError(f"no record {id!r}")
        self._require_scope(record, scope, op)
        return record

    def _lineage_has_live_successor(self, original_id: str) -> bool:
        """True if original_id's supersession chain currently ends in a live ACTIVE record."""
        current = self._records.get(original_id)
        if current is None:
            return False
        seen = {original_id}
        while current.superseded_by is not None:
            successor = self._records.get(current.superseded_by)
            if successor is None or successor.id in seen:
                break
            current = successor
            seen.add(current.id)
        return current.lifecycle_state == LifecycleState.ACTIVE and current.applicable

    # -- public API -----------------------------------------------------

    def create(self, id: str, payload: Any, scope: str) -> StateRecord:
        if id in self._records:
            raise ValueError(f"record {id!r} already exists")
        record = StateRecord(
            id=id,
            payload=payload,
            lifecycle_state=LifecycleState.ACTIVE,
            applicable=True,
            scope=scope,
            version=1,
            provenance=("create",),
        )
        self._records[id] = record
        return record.copy()

    def snapshot(self, id: str, scope: str) -> Snapshot:
        record = self._get_active(id, scope, "snapshot")
        snapshot_id = f"snap-{id}-v{record.version}-{next(self._counter)}"
        snap = Snapshot(
            snapshot_id=snapshot_id,
            captured_state=record.copy(),
            captured_version=record.version,
        )
        self._snapshots[snapshot_id] = snap
        return snap

    def revoke(self, id: str, scope: str) -> StateRecord:
        record = self._get_active(id, scope, "revoke")
        record.lifecycle_state = LifecycleState.REVOKED
        record.applicable = False
        record.revoked = True
        record.version += 1
        record.provenance += ("revoke",)
        return record.copy()

    def erase(self, id: str, scope: str) -> StateRecord:
        record = self._get_active(id, scope, "erase")
        record.lifecycle_state = LifecycleState.ERASED
        record.applicable = False
        record.erased = True
        # Logical erasure: payload becomes non-processable going forward.
        # The record's transition history (provenance) is retained, since
        # "erased value != erased history".
        record.payload = None
        record.version += 1
        record.provenance += ("erase",)
        return record.copy()

    def supersede(self, id: str, scope: str, new_id: str, new_payload: Any) -> tuple[StateRecord, StateRecord]:
        old = self._get_active(id, scope, "supersede")
        if new_id in self._records:
            raise ValueError(f"record {new_id!r} already exists")
        old.lifecycle_state = LifecycleState.SUPERSEDED
        old.applicable = False
        old.superseded_by = new_id
        old.version += 1
        old.provenance += (f"superseded_by:{new_id}",)
        new_record = StateRecord(
            id=new_id,
            payload=new_payload,
            lifecycle_state=LifecycleState.ACTIVE,
            applicable=True,
            scope=scope,
            version=1,
            provenance=(f"supersedes:{id}",),
        )
        self._records[new_id] = new_record
        return old.copy(), new_record.copy()

    def restore(self, snapshot_id: str, scope: str) -> StateRecord:
        """Materialize a stale restore candidate from a snapshot.

        CORE INVARIANT: RESTORED_BYTES != RESTORED_CURRENT_APPLICABILITY.
        The candidate is always created with applicable=False; only an
        explicit reconcile() call can change that.
        """
        snap = self._snapshots.get(snapshot_id)
        if snap is None:
            raise KeyError(f"no snapshot {snapshot_id!r}")
        if snap.captured_state.scope != scope:
            raise ScopeViolation(
                f"restore denied: snapshot scope={snap.captured_state.scope!r} "
                f"!= requesting scope={scope!r}"
            )
        candidate = snap.captured_state.copy()
        original_id = candidate.id
        candidate.id = f"{original_id}-restored-{next(self._counter)}"
        candidate.lifecycle_state = LifecycleState.RESTORED_CANDIDATE
        candidate.applicable = False
        candidate.provenance += (f"restored_from:{snapshot_id}",)
        self._restored_candidates[candidate.id] = candidate
        return candidate.copy()

    def reconcile(
        self,
        candidate_id: str,
        scope: str,
        grant_applicability: bool,
        rationale: str,
    ) -> StateRecord:
        """Explicit owner-local reconciliation of a restore candidate.

        This is the ONLY mechanism by which a restored candidate may
        become applicable again. A candidate can never be granted
        applicability if its original lineage already has a live
        (ACTIVE, applicable) successor: doing so would silently let a
        stale record replace validated current state, which this
        research model treats as a hard invariant rather than a
        judgment call reconcile() is allowed to override.
        """
        if not rationale:
            raise ReconciliationError("reconcile requires an explicit non-empty owner-local rationale")
        candidate = self._restored_candidates.get(candidate_id)
        if candidate is None:
            raise KeyError(f"no restored candidate {candidate_id!r}")
        self._require_scope(candidate, scope, "reconcile")

        if not grant_applicability:
            candidate.lifecycle_state = LifecycleState.RECONCILED_STALE
            candidate.applicable = False
            candidate.provenance += (f"reconciled_stale:{rationale}",)
            return candidate.copy()

        original_id = candidate.id.rsplit("-restored-", 1)[0]
        if self._lineage_has_live_successor(original_id):
            candidate.lifecycle_state = LifecycleState.RECONCILED_STALE
            candidate.applicable = False
            candidate.provenance += (f"reconcile_denied_live_successor:{rationale}",)
            return candidate.copy()

        candidate.lifecycle_state = LifecycleState.RECONCILED_APPLICABLE
        candidate.applicable = True
        candidate.provenance += (f"reconciled_applicable:{rationale}",)
        return candidate.copy()

    def get_current_applicability(self, id: str, scope: str) -> bool:
        record = self._records.get(id) or self._restored_candidates.get(id)
        if record is None:
            raise KeyError(f"no record {id!r}")
        self._require_scope(record, scope, "get_current_applicability")
        return record.applicable

    def get_record(self, id: str, scope: str) -> StateRecord:
        record = self._records.get(id) or self._restored_candidates.get(id)
        if record is None:
            raise KeyError(f"no record {id!r}")
        self._require_scope(record, scope, "get_record")
        return record.copy()
