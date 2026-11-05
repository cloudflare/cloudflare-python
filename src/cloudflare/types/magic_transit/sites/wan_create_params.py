# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["WANCreateParams", "StaticAddressing"]


class WANCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    physport: Required[int]

    health_check_rate: Literal["low", "mid", "high"]
    """Magic WAN health check rate for tunnels created on this link.

    The default value is `mid`.
    """

    load_balance_inner_flows: bool

    name: str

    priority: int

    provisioned_download_kbps: int
    """Provisioned download rate of the WAN circuit in kilobits per second."""

    provisioned_upload_kbps: int
    """Provisioned upload rate of the WAN circuit in kilobits per second."""

    static_addressing: StaticAddressing
    """Static addressing configuration for a WAN.

    Omit to use DHCP. Submit secondary_address when the site is in high availability
    mode.
    """

    vlan_tag: int
    """VLAN ID. Use zero for untagged."""


class StaticAddressing(TypedDict, total=False):
    """Static addressing configuration for a WAN.

    Omit to use DHCP. Submit secondary_address when the site is in high availability mode.
    """

    address: Required[str]
    """A valid CIDR notation representing an IP range."""

    gateway_address: Required[str]
    """A valid IPv4 address."""

    secondary_address: str
    """A valid CIDR notation representing an IP range."""

    secondary_gateway_address: str
    """Gateway address for the secondary connector of a high availability site."""
