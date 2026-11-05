# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WANUpdateParams", "StaticAddressing"]


class WANUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    site_id: Required[str]
    """Identifier"""

    health_check_rate: Literal["low", "mid", "high"]
    """Magic WAN health check rate for tunnels created on this link."""

    load_balance_inner_flows: Optional[bool]

    name: str

    physport: int

    priority: int

    provisioned_download_kbps: Optional[int]
    """Provisioned download rate of the WAN circuit in kilobits per second.

    Set to null to remove it.
    """

    provisioned_upload_kbps: Optional[int]
    """Provisioned upload rate of the WAN circuit in kilobits per second.

    Set to null to remove it.
    """

    static_addressing: StaticAddressing
    """Static addressing configuration.

    PATCH updates only the fields provided, and PUT replaces the configuration.
    """

    vlan_tag: int
    """VLAN ID. Use zero for untagged."""


class StaticAddressing(TypedDict, total=False):
    """Static addressing configuration.

    PATCH updates only the fields provided, and PUT replaces the configuration.
    """

    address: str
    """A valid CIDR notation representing an IP range."""

    gateway_address: str
    """A valid IPv4 address."""

    secondary_address: str
    """A valid CIDR notation representing an IP range."""

    secondary_gateway_address: Optional[str]
    """Gateway address for the secondary connector of a high availability site.

    Set to null to remove it.
    """
