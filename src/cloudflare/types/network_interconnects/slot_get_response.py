# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SlotGetResponse", "Facility"]


class Facility(BaseModel):
    address: List[str]

    name: str


class SlotGetResponse(BaseModel):
    id: str
    """Slot ID"""

    facility: Facility

    occupied: bool
    """Whether the slot is occupied or not"""

    site: str

    speed: str

    account: Optional[str] = None
    """Customer account tag"""
