# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["CNIListParams"]


class CNIListParams(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    cursor: Optional[int]

    limit: Optional[int]

    slot: Optional[str]
    """If specified, only show CNIs associated with the specified slot"""
