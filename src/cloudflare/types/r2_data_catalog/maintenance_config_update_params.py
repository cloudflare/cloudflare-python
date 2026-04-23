# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MaintenanceConfigUpdateParams", "Compaction", "SnapshotExpiration"]


class MaintenanceConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    compaction: Compaction
    """Updates compaction configuration (all fields optional)."""

    snapshot_expiration: SnapshotExpiration
    """Updates snapshot expiration configuration (all fields optional)."""


class Compaction(TypedDict, total=False):
    """Updates compaction configuration (all fields optional)."""

    state: Literal["enabled", "disabled"]
    """Updates the state optionally."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Updates the target file size optionally."""


class SnapshotExpiration(TypedDict, total=False):
    """Updates snapshot expiration configuration (all fields optional)."""

    max_snapshot_age: str
    """Updates the maximum age for snapshots optionally."""

    min_snapshots_to_keep: int
    """Updates the minimum number of snapshots to retain optionally."""

    state: Literal["enabled", "disabled"]
    """Updates the state optionally."""
