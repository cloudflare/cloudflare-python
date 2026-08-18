# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["InterconnectLOAParams"]


class InterconnectLOAParams(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    name: Optional[str]
    """Custom name to use in the LOA instead of the account name (200 Character limit)"""
