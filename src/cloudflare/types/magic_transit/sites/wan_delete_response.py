# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["WANDeleteResponse", "DeletedWAN", "DeletedWANStaticAddressing"]


class DeletedWANStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    gateway_address: str
    """A valid IPv4 address."""

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class DeletedWAN(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None

    physport: Optional[int] = None

    priority: Optional[int] = None
    """Priority of WAN for traffic loadbalancing."""

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[DeletedWANStaticAddressing] = None
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""


class WANDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_wan: Optional[DeletedWAN] = None
