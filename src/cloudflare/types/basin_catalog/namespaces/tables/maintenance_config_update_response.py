# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["MaintenanceConfigUpdateResponse", "Compaction", "SnapshotExpiration"]


class Compaction(BaseModel):
    """Configures compaction settings for table optimization."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Sets the target file size for compaction in megabytes. Defaults to "128"."""

    next_eligible_at: Optional[datetime] = None
    """Earliest time when the scheduler can claim this operation. Null when disabled."""


class SnapshotExpiration(BaseModel):
    max_snapshot_age: str
    """Specifies the maximum age for snapshots."""

    min_snapshots_to_keep: int
    """Specifies the minimum number of snapshots to retain. Defaults to 100."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    next_eligible_at: Optional[datetime] = None
    """Earliest time when the scheduler can claim this operation. Null when disabled."""


class MaintenanceConfigUpdateResponse(BaseModel):
    """Configures maintenance for the table."""

    compaction: Optional[Compaction] = None
    """Configures compaction settings for table optimization."""

    interval: Optional[str] = None
    """Scheduling interval between normal table maintenance runs."""

    snapshot_expiration: Optional[SnapshotExpiration] = None
