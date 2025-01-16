# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScanListParams"]


class ScanListParams(TypedDict, total=False):
    q: str
    """Filter scans"""

    size: int
    """Limit the number of objects in the response."""
