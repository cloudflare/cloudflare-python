# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RouteEditParams"]


class RouteEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """Optional remark describing the route."""

    network: str
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]
    """The type of tunnel."""

    tunnel_id: object
    """UUID of the Cloudflare Tunnel serving the route."""

    virtual_network_id: object
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """
