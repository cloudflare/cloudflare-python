# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "MaintenanceConfigGetResponse",
    "MaintenanceConfig",
    "MaintenanceConfigCompaction",
    "MaintenanceConfigSnapshotExpiration",
]


class MaintenanceConfigCompaction(BaseModel):
    """Configures compaction for catalog maintenance."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Sets the target file size for compaction in megabytes."""


class MaintenanceConfigSnapshotExpiration(BaseModel):
    """Configures snapshot expiration settings."""

    max_snapshot_age: str
    """Specifies the maximum age for snapshots.

    The system deletes snapshots older than this age. Format: <number><unit> where
    unit is d (days), h (hours), m (minutes), or s (seconds). Examples: "7d" (7
    days), "48h" (48 hours), "2880m" (2,880 minutes).
    """

    min_snapshots_to_keep: int
    """Specifies the minimum number of snapshots to retain."""

    state: Literal["enabled", "disabled"]
    """Specifies the state of maintenance operations."""


class MaintenanceConfig(BaseModel):
    """Configures maintenance for the catalog."""

    compaction: Optional[MaintenanceConfigCompaction] = None
    """Configures compaction for catalog maintenance."""

    snapshot_expiration: Optional[MaintenanceConfigSnapshotExpiration] = None
    """Configures snapshot expiration settings."""


class MaintenanceConfigGetResponse(BaseModel):
    """Contains maintenance configuration and credential status."""

    credential_status: Literal["present", "absent"]
    """Shows the credential configuration status."""

    maintenance_config: MaintenanceConfig
    """Configures maintenance for the catalog."""
