# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["CustomTrustStoreListParams"]


class CustomTrustStoreListParams(TypedDict, total=False):
    zone_id: str
    """Identifier."""

    limit: int
    """Limit to the number of records returned."""

    offset: int
    """Offset the results"""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of records per page."""
