# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DynamicRoutingListParams"]


class DynamicRoutingListParams(TypedDict, total=False):
    account_id: Required[str]

    page: int
    """Page number"""

    per_page: int
    """Number of routes per page"""
