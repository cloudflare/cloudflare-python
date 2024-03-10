# File generated from our OpenAPI spec by Stainless.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = [
    "LanDeleteResponse",
    "DeletedLan",
    "DeletedLanNat",
    "DeletedLanRoutedSubnet",
    "DeletedLanRoutedSubnetNat",
    "DeletedLanStaticAddressing",
    "DeletedLanStaticAddressingDhcpRelay",
    "DeletedLanStaticAddressingDhcpServer",
]


class DeletedLanNat(BaseModel):
    static_prefix: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class DeletedLanRoutedSubnetNat(BaseModel):
    static_prefix: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class DeletedLanRoutedSubnet(BaseModel):
    next_hop: str
    """A valid IPv4 address."""

    prefix: str
    """A valid CIDR notation representing an IP range."""

    nat: Optional[DeletedLanRoutedSubnetNat] = None


class DeletedLanStaticAddressingDhcpRelay(BaseModel):
    server_addresses: Optional[List[str]] = None
    """List of DHCP server IPs."""


class DeletedLanStaticAddressingDhcpServer(BaseModel):
    dhcp_pool_end: Optional[str] = None
    """A valid IPv4 address."""

    dhcp_pool_start: Optional[str] = None
    """A valid IPv4 address."""

    dns_server: Optional[str] = None
    """A valid IPv4 address."""

    reservations: Optional[Dict[str, str]] = None
    """Mapping of MAC addresses to IP addresses"""


class DeletedLanStaticAddressing(BaseModel):
    address: str
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: Optional[DeletedLanStaticAddressingDhcpRelay] = None

    dhcp_server: Optional[DeletedLanStaticAddressingDhcpServer] = None

    secondary_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""

    virtual_address: Optional[str] = None
    """A valid CIDR notation representing an IP range."""


class DeletedLan(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    description: Optional[str] = None

    ha_link: Optional[bool] = None
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    nat: Optional[DeletedLanNat] = None

    physport: Optional[int] = None

    routed_subnets: Optional[List[DeletedLanRoutedSubnet]] = None

    site_id: Optional[str] = None
    """Identifier"""

    static_addressing: Optional[DeletedLanStaticAddressing] = None
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """

    vlan_tag: Optional[int] = None
    """VLAN port number."""


class LanDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_lan: Optional[DeletedLan] = None
