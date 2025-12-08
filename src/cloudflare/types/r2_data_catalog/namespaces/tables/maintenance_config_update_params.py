# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MaintenanceConfigUpdateParams", "Compaction"]


class MaintenanceConfigUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Use this to identify the account."""

    bucket_name: Required[str]
    """Specifies the R2 bucket name."""

    namespace: Required[str]

    compaction: Compaction
    """Updates compaction configuration (all fields optional)."""


class Compaction(TypedDict, total=False):
    """Updates compaction configuration (all fields optional)."""

    state: Literal["enabled", "disabled"]
    """Updates the state optionally."""

    target_size_mb: Literal["64", "128", "256", "512"]
    """Updates the target file size optionally."""
