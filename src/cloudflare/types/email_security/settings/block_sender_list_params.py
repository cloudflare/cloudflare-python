# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BlockSenderListParams"]


class BlockSenderListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    direction: Literal["asc", "desc"]
    """The sorting direction."""

    order: Literal["pattern", "created_at"]
    """Field to sort by."""

    page: int
    """Current page within paginated list of results."""

    pattern: str
    """Filter by pattern value."""

    pattern_type: Literal["EMAIL", "DOMAIN", "IP", "UNKNOWN"]
    """Filter by pattern type."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    search: str
    """Search term for filtering records. Behavior may change."""
