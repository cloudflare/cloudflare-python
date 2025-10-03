# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SubscriptionListParams"]


class SubscriptionListParams(TypedDict, total=False):
    account_id: Required[str]
    """A Resource identifier."""

    direction: Literal["asc", "desc"]
    """Sort direction"""

    order: Literal["created_at", "name", "enabled", "source"]
    """Field to sort by"""

    page: int
    """Page number for pagination"""

    per_page: int
    """Number of items per page"""
