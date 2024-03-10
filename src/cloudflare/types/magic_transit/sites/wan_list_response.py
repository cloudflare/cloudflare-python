# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["WanListResponse", "Wan", "WanStaticAddressing"]


class WanStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    gateway_address: str
    """A valid IPv4 address."""

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class Wan(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None

    physport: Optional[int] = None

    priority: Optional[int] = None
    """Priority of WAN for traffic loadbalancing."""

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[WanStaticAddressing] = None
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""


class WanListResponse(BaseModel):
    wans: Optional[List[Wan]] = None
