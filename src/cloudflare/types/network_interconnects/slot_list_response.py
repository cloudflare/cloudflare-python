# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SlotListResponse", "Item", "ItemFacility"]


class ItemFacility(BaseModel):
    address: List[str]

    name: str


class Item(BaseModel):
    id: str
    """Slot ID"""

    facility: ItemFacility

    occupied: bool
    """Whether the slot is occupied or not"""

    site: str

    speed: str

    account: Optional[str] = None
    """Customer account tag"""


class SlotListResponse(BaseModel):
    items: List[Item]

    next: Optional[int] = None
