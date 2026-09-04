"""Owner-local executable research fixtures for State Validation Lab.

This package is research-only.  It is not a production truth engine, Canon,
permission issuer, identity authority, action authority, runtime controller,
rollback authority, or production storage model.
"""

from .model import (
    LifecycleState,
    ReconciliationResult,
    ResearchStateModel,
    Snapshot,
    StateRecord,
    UnknownCandidateError,
    UnknownRecordError,
    UnknownSnapshotError,
)

__all__ = [
    "LifecycleState",
    "ReconciliationResult",
    "ResearchStateModel",
    "Snapshot",
    "StateRecord",
    "UnknownCandidateError",
    "UnknownRecordError",
    "UnknownSnapshotError",
]
