# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "LanCreateParams",
    "Lan",
    "LanNat",
    "LanRoutedSubnet",
    "LanRoutedSubnetNat",
    "LanStaticAddressing",
    "LanStaticAddressingDhcpRelay",
    "LanStaticAddressingDhcpServer",
]


class LanCreateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    lan: Lan


class LanNat(TypedDict, total=False):
    static_prefix: str
    """A valid CIDR notation representing an IP range."""


class LanRoutedSubnetNat(TypedDict, total=False):
    static_prefix: str
    """A valid CIDR notation representing an IP range."""


class LanRoutedSubnet(TypedDict, total=False):
    next_hop: Required[str]
    """A valid IPv4 address."""

    prefix: Required[str]
    """A valid CIDR notation representing an IP range."""

    nat: LanRoutedSubnetNat


class LanStaticAddressingDhcpRelay(TypedDict, total=False):
    server_addresses: List[str]
    """List of DHCP server IPs."""


class LanStaticAddressingDhcpServer(TypedDict, total=False):
    dhcp_pool_end: str
    """A valid IPv4 address."""

    dhcp_pool_start: str
    """A valid IPv4 address."""

    dns_server: str
    """A valid IPv4 address."""

    reservations: Dict[str, str]
    """Mapping of MAC addresses to IP addresses"""


class LanStaticAddressing(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: LanStaticAddressingDhcpRelay

    dhcp_server: LanStaticAddressingDhcpServer

    secondary_address: str
    """A valid CIDR notation representing an IP range."""

    virtual_address: str
    """A valid CIDR notation representing an IP range."""


class Lan(TypedDict, total=False):
    physport: Required[int]

    vlan_tag: Required[int]
    """VLAN port number."""

    description: str

    ha_link: bool
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    nat: LanNat

    routed_subnets: Iterable[LanRoutedSubnet]

    static_addressing: LanStaticAddressing
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """
