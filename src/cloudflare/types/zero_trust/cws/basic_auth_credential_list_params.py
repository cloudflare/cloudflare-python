# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BasicAuthCredentialListParams"]


class BasicAuthCredentialListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    cursor: str
    """Pagination cursor from previous response"""

    deployment_id: str
    """Filter to credentials attached to this deployment"""

    direction: Literal["asc", "desc"]
    """Sort direction (default: asc)"""

    order: Literal["username", "created_at", "updated_at"]
    """Field to order results by (default: created_at)"""

    per_page: int
    """Number of items per page (1-100, default 20)"""

    username: str
    """Filter by username (case-insensitive substring match)"""
