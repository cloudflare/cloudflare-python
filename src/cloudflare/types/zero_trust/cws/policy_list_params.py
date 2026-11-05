# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["PolicyListParams"]


class PolicyListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    cursor: str
    """Pagination cursor from previous response"""

    direction: Literal["asc", "desc"]
    """Sort direction (default: asc)"""

    name: str
    """Filter by policy name (case-insensitive substring match)"""

    order: Literal["name", "created_at", "updated_at"]
    """Field to order results by (default: created_at)"""

    package_path: str
    """Filter by package path (case-sensitive literal substring match)"""

    per_page: int
    """Number of items per page (1-100, default 20)"""

    policy_set_id: str
    """Filter to policies attached to (members of) this policy set"""
