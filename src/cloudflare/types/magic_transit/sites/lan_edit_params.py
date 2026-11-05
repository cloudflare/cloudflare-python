# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .nat_param import NatParam
from .routed_subnet_param import RoutedSubnetParam
from .lan_static_addressing_param import LANStaticAddressingParam

__all__ = ["LANEditParams", "RemoteSubnet"]


class LANEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    bond_id: int

    ha_link: bool
    """mark true to use this LAN for HA probing.

    only works for site with HA turned on. only one LAN can be set as the ha_link.
    """

    is_breakout: bool
    """mark true to use this LAN for source-based breakout traffic"""

    is_prioritized: bool
    """mark true to use this LAN for source-based prioritized traffic"""

    name: str

    nat: NatParam

    physport: int

    remote_subnets: Iterable[RemoteSubnet]

    routed_subnets: Iterable[RoutedSubnetParam]

    static_addressing: LANStaticAddressingParam
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """

    vlan_tag: int
    """VLAN ID. Use zero for untagged."""


class RemoteSubnet(TypedDict, total=False):
    """
    A remote subnet reachable through Cloudflare that is addressed from this LAN by a local alias prefix of the same size. The local alias prefix must not overlap other subnets on the LAN, and the remote prefix must not overlap other remote prefixes on the LAN.
    """

    local_alias_prefix: Required[str]
    """A valid CIDR notation representing an IP range."""

    remote_prefix: Required[str]
    """A valid CIDR notation representing an IP range."""
