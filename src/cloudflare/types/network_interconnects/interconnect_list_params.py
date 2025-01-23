# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["InterconnectListParams"]


class InterconnectListParams(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    cursor: Optional[int]

    limit: Optional[int]

    site: Optional[str]
    """If specified, only show interconnects located at the given site"""

    type: Optional[str]
    """If specified, only show interconnects of the given type"""
