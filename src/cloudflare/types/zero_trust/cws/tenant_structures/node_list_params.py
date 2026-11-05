# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NodeListParams"]


class NodeListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    cursor: str
    """Pagination cursor from previous response"""

    direction: Literal["asc", "desc"]
    """Sort direction (default: asc)"""

    name: str
    """Filter by node name (case-insensitive substring match)"""

    native_id: str
    """Filter by exact cloud-native identifier"""

    node_kind: str
    """Filter by exact node kind"""

    order: Literal["name", "created_at", "updated_at"]
    """Field to order results by (default: created_at)"""

    parent: str
    """Filter by exact parent native ID"""

    per_page: int
    """Number of items per page (1-100, default 20)"""
