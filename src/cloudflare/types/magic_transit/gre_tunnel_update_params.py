# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .health_check_param import HealthCheckParam

__all__ = ["GRETunnelUpdateParams"]


class GRETunnelUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    cloudflare_gre_endpoint: Required[str]
    """The IP address assigned to the Cloudflare side of the GRE tunnel."""

    customer_gre_endpoint: Required[str]
    """The IP address assigned to the customer side of the GRE tunnel."""

    interface_address: Required[str]
    """
    A 31-bit prefix (/31 in CIDR notation) supporting two hosts, one for each side
    of the tunnel. Select the subnet from the following private IP space:
    10.0.0.0–10.255.255.255, 172.16.0.0–172.31.255.255, 192.168.0.0–192.168.255.255.
    """

    name: Required[str]
    """The name of the tunnel.

    The name cannot contain spaces or special characters, must be 15 characters or
    less, and cannot share a name with another GRE tunnel.
    """

    description: str
    """An optional description of the GRE tunnel."""

    health_check: HealthCheckParam

    mtu: int
    """Maximum Transmission Unit (MTU) in bytes for the GRE tunnel.

    The minimum value is 576.
    """

    ttl: int
    """Time To Live (TTL) in number of hops of the GRE tunnel."""
