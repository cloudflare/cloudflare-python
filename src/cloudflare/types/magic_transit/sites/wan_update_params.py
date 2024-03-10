# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["WanUpdateParams", "Wan", "WanStaticAddressing"]


class WanUpdateParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    site_identifier: Required[str]
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
    description: str

    physport: int

    priority: int

    static_addressing: WanStaticAddressing
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: int
    """VLAN port number."""
