"""Minimal deterministic model for the E6 restore-resurrection experiment.

THIS MODEL IS RESEARCH-ONLY.

It deliberately does not implement a database, event log, permission system,
truth engine, Canon, production restore workflow, or physical/cryptographic
erasure.  ``erase`` below is a fixture-local logical lifecycle transition.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from enum import Enum


class LifecycleState(str, Enum):
    """Fixture-local lifecycle positions used by E6."""

    ACTIVE = "ACTIVE"
    REVOKED = "REVOKED"
    SUPERSEDED = "SUPERSEDED"
    ERASED = "ERASED"
    RESTORED_STALE_CANDIDATE = "RESTORED_STALE_CANDIDATE"
    RESTORED_RECONCILED = "RESTORED_RECONCILED"


class ReconciliationResult(str, Enum):
    """Bounded research outcomes; none grants external authority."""

    APPLICABLE = "APPLICABLE"
    NOT_APPLICABLE = "NOT_APPLICABLE"
    UNKNOWN = "UNKNOWN"
    BLOCKED = "BLOCKED"


class UnknownRecordError(KeyError):
    """Raised when a requested current record does not exist."""


class UnknownSnapshotError(KeyError):
    """Raised when a requested snapshot does not exist."""


class UnknownCandidateError(KeyError):
    """Raised when a requested restored candidate does not exist."""


@dataclass(frozen=True, slots=True)
class StateRecord:
    """A tiny fixture record, not a frozen production schema."""

    id: str
    payload: str | None
    lifecycle_state: LifecycleState
    applicable: bool
    scope: str
    version: int
    provenance: tuple[str, ...]
    superseded_by: str | None = None
    erased: bool = False
    revoked: bool = False


@dataclass(frozen=True, slots=True)
class Snapshot:
    """A copy of fixture bytes captured at one record version."""

    snapshot_id: str
    captured_record: StateRecord
    captured_version: int


class ResearchStateModel:
    """In-memory E6 model with a quarantined restore path.

    Current records, current lifecycle dispositions, snapshots, and restored
    candidates are separate.  Restoring bytes can therefore never overwrite
    later revoke/erase/supersede information.
    """

    def __init__(self) -> None:
        self._current_records: dict[str, StateRecord] = {}
        self._current_dispositions: dict[str, LifecycleState] = {}
        self._snapshots: dict[str, Snapshot] = {}
        self._restored_candidates: dict[str, StateRecord] = {}

    def create(
        self,
        record_id: str,
        payload: str,
        *,
        scope: str,
        version: int = 1,
        provenance: tuple[str, ...] = ("synthetic-fixture",),
    ) -> StateRecord:
        if record_id in self._current_records:
            raise ValueError(f"current record already exists: {record_id}")
        if version < 1:
            raise ValueError("version must be positive")
        record = StateRecord(
            id=record_id,
            payload=payload,
            lifecycle_state=LifecycleState.ACTIVE,
            applicable=True,
            scope=scope,
            version=version,
            provenance=tuple(provenance),
        )
        self._current_records[record_id] = record
        self._current_dispositions[record_id] = LifecycleState.ACTIVE
        return record

    def snapshot(self, record_id: str, snapshot_id: str) -> Snapshot:
        if snapshot_id in self._snapshots:
            raise ValueError(f"snapshot already exists: {snapshot_id}")
        record = self.get_current(record_id)
        snapshot = Snapshot(
            snapshot_id=snapshot_id,
            captured_record=record,
            captured_version=record.version,
        )
        self._snapshots[snapshot_id] = snapshot
        return snapshot

    def revoke(self, record_id: str) -> StateRecord:
        record = self.get_current(record_id)
        self._require_active(record_id, "revoke")
        updated = replace(
            record,
            lifecycle_state=LifecycleState.REVOKED,
            applicable=False,
            revoked=True,
        )
        self._current_records[record_id] = updated
        self._current_dispositions[record_id] = LifecycleState.REVOKED
        return updated

    def erase(self, record_id: str) -> StateRecord:
        """Apply fixture-local logical erasure; no physical claim is made."""

        record = self.get_current(record_id)
        self._require_active(record_id, "erase")
        updated = replace(
            record,
            payload=None,
            lifecycle_state=LifecycleState.ERASED,
            applicable=False,
            erased=True,
        )
        self._current_records[record_id] = updated
        self._current_dispositions[record_id] = LifecycleState.ERASED
        return updated

    def supersede(
        self,
        record_id: str,
        successor_id: str,
        successor_payload: str,
        *,
        version: int,
        provenance: tuple[str, ...] = ("synthetic-fixture",),
    ) -> StateRecord:
        predecessor = self.get_current(record_id)
        self._require_active(record_id, "supersede")
        if successor_id in self._current_records:
            raise ValueError(f"successor already exists: {successor_id}")
        if version <= predecessor.version:
            raise ValueError("successor version must be greater than predecessor")

        self._current_records[record_id] = replace(
            predecessor,
            lifecycle_state=LifecycleState.SUPERSEDED,
            applicable=False,
            superseded_by=successor_id,
        )
        self._current_dispositions[record_id] = LifecycleState.SUPERSEDED

        successor = StateRecord(
            id=successor_id,
            payload=successor_payload,
            lifecycle_state=LifecycleState.ACTIVE,
            applicable=True,
            scope=predecessor.scope,
            version=version,
            provenance=tuple(provenance),
        )
        self._current_records[successor_id] = successor
        self._current_dispositions[successor_id] = LifecycleState.ACTIVE
        return successor

    def restore(self, snapshot_id: str) -> str:
        """Restore bytes into quarantine without changing current state."""

        snapshot = self._snapshots.get(snapshot_id)
        if snapshot is None:
            raise UnknownSnapshotError(snapshot_id)
        candidate_id = f"restore:{snapshot_id}:{snapshot.captured_record.id}"
        if candidate_id in self._restored_candidates:
            raise ValueError(f"restored candidate already exists: {candidate_id}")
        self._restored_candidates[candidate_id] = replace(
            snapshot.captured_record,
            lifecycle_state=LifecycleState.RESTORED_STALE_CANDIDATE,
            applicable=False,
        )
        return candidate_id

    def reconcile(self, candidate_id: str) -> ReconciliationResult:
        """Evaluate a candidate against current owner-local fixture state.

        Reconciliation cannot clear a later invalidation.  A positive result is
        possible only when the current record is still the same active record.
        The candidate remains separate from the live collection either way.
        """

        candidate = self.get_candidate(candidate_id)
        current = self._current_records.get(candidate.id)
        disposition = self._current_dispositions.get(candidate.id)

        if current is None or disposition is None:
            self._mark_candidate_inapplicable(candidate_id)
            return ReconciliationResult.UNKNOWN
        if disposition in {
            LifecycleState.REVOKED,
            LifecycleState.SUPERSEDED,
            LifecycleState.ERASED,
        }:
            self._mark_candidate_inapplicable(candidate_id)
            return ReconciliationResult.NOT_APPLICABLE
        if disposition is not LifecycleState.ACTIVE:
            self._mark_candidate_inapplicable(candidate_id)
            return ReconciliationResult.BLOCKED

        same_current_state = (
            current.version == candidate.version
            and current.payload == candidate.payload
            and current.scope == candidate.scope
            and current.provenance == candidate.provenance
            and current.applicable
        )
        if not same_current_state:
            self._mark_candidate_inapplicable(candidate_id)
            return ReconciliationResult.BLOCKED

        self._restored_candidates[candidate_id] = replace(
            candidate,
            lifecycle_state=LifecycleState.RESTORED_RECONCILED,
            applicable=True,
        )
        return ReconciliationResult.APPLICABLE

    def get_current(self, record_id: str) -> StateRecord:
        record = self._current_records.get(record_id)
        if record is None:
            raise UnknownRecordError(record_id)
        return record

    def get_candidate(self, candidate_id: str) -> StateRecord:
        candidate = self._restored_candidates.get(candidate_id)
        if candidate is None:
            raise UnknownCandidateError(candidate_id)
        return candidate

    def get_current_applicability(self, record_id: str) -> bool:
        return self.get_current(record_id).applicable

    def get_candidate_applicability(self, candidate_id: str) -> bool:
        return self.get_candidate(candidate_id).applicable

    def get_current_disposition(self, record_id: str) -> LifecycleState:
        try:
            return self._current_dispositions[record_id]
        except KeyError as exc:
            raise UnknownRecordError(record_id) from exc

    def _require_active(self, record_id: str, operation: str) -> None:
        disposition = self.get_current_disposition(record_id)
        if disposition is not LifecycleState.ACTIVE:
            raise ValueError(
                f"{operation} requires ACTIVE current disposition; "
                f"{record_id} is {disposition.value}"
            )

    def _mark_candidate_inapplicable(self, candidate_id: str) -> None:
        candidate = self.get_candidate(candidate_id)
        self._restored_candidates[candidate_id] = replace(
            candidate,
            lifecycle_state=LifecycleState.RESTORED_STALE_CANDIDATE,
            applicable=False,
        )
