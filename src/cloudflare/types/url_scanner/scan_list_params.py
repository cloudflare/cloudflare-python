# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScanListParams"]


class ScanListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    q: str
    """Filter scans"""

    size: int
    """Limit the number of objects in the response."""
