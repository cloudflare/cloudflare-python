# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "InterconnectListResponse",
    "Item",
    "ItemNscInterconnectPhysicalBody",
    "ItemNscInterconnectPhysicalBodyFacility",
    "ItemNscInterconnectGcpPartnerBody",
]


class ItemNscInterconnectPhysicalBodyFacility(BaseModel):
    address: List[str]

    name: str


class ItemNscInterconnectPhysicalBody(BaseModel):
    account: str

    facility: ItemNscInterconnectPhysicalBodyFacility

    name: str

    site: str
    """A Cloudflare site name."""

    slot_id: str

    speed: str

    type: str

    owner: Optional[str] = None


class ItemNscInterconnectGcpPartnerBody(BaseModel):
    account: str

    name: str

    region: str

    type: str

    owner: Optional[str] = None


Item: TypeAlias = Union[ItemNscInterconnectPhysicalBody, ItemNscInterconnectGcpPartnerBody]


class InterconnectListResponse(BaseModel):
    items: List[Item]

    next: Optional[int] = None
