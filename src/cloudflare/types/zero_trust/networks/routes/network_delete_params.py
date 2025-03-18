# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["NetworkDeleteParams"]


class NetworkDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    tun_type: Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]
    """The type of tunnel."""

    tunnel_id: str
    """UUID of the tunnel."""

    virtual_network_id: str
    """UUID of the virtual network."""
