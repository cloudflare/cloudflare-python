# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .nat_param import NatParam
from .routed_subnet_param import RoutedSubnetParam
from .static_addressing_param import StaticAddressingParam

__all__ = ["LANUpdateParams", "LAN"]


class LANUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    lan: LAN


class LAN(TypedDict, total=False):
    description: str

    nat: NatParam

    physport: int

    routed_subnets: Iterable[RoutedSubnetParam]

    static_addressing: StaticAddressingParam
    """
    If the site is not configured in high availability mode, this configuration is
    optional (if omitted, use DHCP). However, if in high availability mode,
    static_address is required along with secondary and virtual address.
    """

    vlan_tag: int
    """VLAN port number."""
