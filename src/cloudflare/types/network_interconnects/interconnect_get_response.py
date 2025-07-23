# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "InterconnectGetResponse",
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

    speed: Optional[Literal["50M", "100M", "200M", "300M", "400M", "500M", "1G", "2G", "5G", "10G", "20G", "50G"]] = (
        None
    )
    """Bandwidth structure as visible through the customer-facing API."""


InterconnectGetResponse: TypeAlias = Union[NscInterconnectPhysicalBody, NscInterconnectGcpPartnerBody]
