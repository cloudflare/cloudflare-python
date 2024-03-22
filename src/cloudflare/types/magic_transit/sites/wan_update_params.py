# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WANUpdateParams", "WAN", "WANStaticAddressing"]


class WANUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    wan: WAN


class WANStaticAddressing(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    gateway_address: Required[str]
    """A valid IPv4 address."""

    secondary_address: str
    """A valid CIDR notation representing an IP range."""


class WAN(TypedDict, total=False):
    description: str

    physport: int

    priority: int

    static_addressing: WANStaticAddressing
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: int
    """VLAN port number."""
