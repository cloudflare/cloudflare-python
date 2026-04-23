# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RuleListParams"]


class RuleListParams(TypedDict, total=False):
    account_id: Required[str]

    page: Required[float]
    """Page number of paginated results"""

    per_page: Required[float]
    """Number of items per page"""

    name: str
    """Filter results by rule name"""

    sort_by: Literal["name", "created_at", "updated_at"]
    """Which property to sort results by"""

    sort_order: Literal["ASC", "DESC"]
    """Sort direction for sort_by property"""
