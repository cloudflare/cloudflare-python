# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WanCreateParams", "Wan", "WanStaticAddressing"]


class WanCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    wan: Wan


class WanStaticAddressing(TypedDict, total=False):
    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    gateway_address: Required[str]
    """A valid IPv4 address."""

    secondary_address: str
    """A valid CIDR notation representing an IP range."""


class Wan(TypedDict, total=False):
    physport: Required[int]

    vlan_tag: Required[int]
    """VLAN port number."""

    description: str

    priority: int

    static_addressing: WanStaticAddressing
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """
