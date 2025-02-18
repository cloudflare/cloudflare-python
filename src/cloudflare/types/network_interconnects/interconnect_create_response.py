# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = [
    "InterconnectCreateResponse",
    "NscInterconnectPhysicalBody",
    "NscInterconnectPhysicalBodyFacility",
    "NscInterconnectGcpPartnerBody",
]


class NscInterconnectPhysicalBodyFacility(BaseModel):
    address: List[str]

    name: str


class NscInterconnectPhysicalBody(BaseModel):
    account: str

    facility: NscInterconnectPhysicalBodyFacility

    name: str

    site: str
    """A Cloudflare site name."""

    slot_id: str

    speed: str

    type: str

    owner: Optional[str] = None


class NscInterconnectGcpPartnerBody(BaseModel):
    account: str

    name: str

    region: str

    type: str

    owner: Optional[str] = None


InterconnectCreateResponse: TypeAlias = Union[NscInterconnectPhysicalBody, NscInterconnectGcpPartnerBody]
