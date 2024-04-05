# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .static_addressing_param import StaticAddressingParam

__all__ = ["WANUpdateParams", "WAN"]


class WANUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    wan: WAN


class WAN(TypedDict, total=False):
    description: str

    physport: int

    priority: int

    static_addressing: StaticAddressingParam
    """(optional) if omitted, use DHCP.

    Submit secondary_address when site is in high availability mode.
    """

    vlan_tag: int
    """VLAN port number."""
