# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["InstanceListParams"]


class InstanceListParams(TypedDict, total=False):
    account_id: Required[str]

    namespace: str
    """Filter by namespace."""

    order_by: Literal["created_at"]
    """Field to order results by."""

    order_by_direction: Literal["asc", "desc"]
    """Order direction."""

    page: int
    """Page number (1-indexed)."""

    per_page: int
    """Number of results per page."""

    search: str
    """Filter instances whose id contains this string (case-insensitive)."""
