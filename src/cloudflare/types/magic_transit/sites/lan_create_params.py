# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Required, TypedDict

__all__ = [
    "LANCreateParams",
    "LAN",
    "LANNat",
    "LANRoutedSubnet",
    "LANRoutedSubnetNat",
    "LANStaticAddressing",
    "LANStaticAddressingDhcpRelay",
    "LANStaticAddressingDhcpServer",
]


class LANCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    lan: LAN


class LANNat(TypedDict, total=False):
    static_prefix: str
    """A valid CIDR notation representing an IP range."""


class LANRoutedSubnetNat(TypedDict, total=False):
    static_prefix: str
    """A valid CIDR notation representing an IP range."""


class LANRoutedSubnet(TypedDict, total=False):
    next_hop: Required[str]
    """A valid IPv4 address."""

    prefix: Required[str]
    """A valid CIDR notation representing an IP range."""

    nat: LANRoutedSubnetNat


class LANStaticAddressingDhcpRelay(TypedDict, total=False):
    server_addresses: List[str]
    """List of DHCP server IPs."""


class LANStaticAddressingDhcpServer(TypedDict, total=False):
    dhcp_pool_end: str
    """A valid IPv4 address."""

    dhcp_pool_start: str
    """A valid IPv4 address."""

    dns_server: str
    """A valid IPv4 address."""

    reservations: Dict[str, str]
    """Mapping of MAC addresses to IP addresses"""


class LANStaticAddressing(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    dhcp_relay: LANStaticAddressingDhcpRelay

    dhcp_server: LANStaticAddressingDhcpServer

    secondary_address: str
    """A valid CIDR notation representing an IP range."""

    virtual_address: str
    """A valid CIDR notation representing an IP range."""


class LAN(TypedDict, total=False):
    physport: Required[int]

    vlan_tag: Required[int]
    """VLAN port number."""

    description: str

    ha_link: bool
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    nat: LANNat

    routed_subnets: Iterable[LANRoutedSubnet]

    static_addressing: LANStaticAddressing
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """
