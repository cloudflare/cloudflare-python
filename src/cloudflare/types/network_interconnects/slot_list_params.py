# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SlotListParams"]


class SlotListParams(TypedDict, total=False):
    account_id: Required[str]
    """Customer account tag"""

    address_contains: Optional[str]
    """If specified, only show slots with the given text in their address field"""

    cursor: Optional[int]

    limit: Optional[int]

    occupied: Optional[bool]
    """If specified, only show slots with a specific occupied/unoccupied state"""

    site: Optional[str]
    """If specified, only show slots located at the given site"""

    speed: Optional[str]
    """If specified, only show slots that support the given speed"""
