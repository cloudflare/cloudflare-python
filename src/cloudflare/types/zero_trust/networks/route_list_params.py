# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """Optional remark describing the route."""

    existed_at: str
    """
    If provided, include only resources that were created (and not deleted) before
    this time. URL encoded.
    """

    is_deleted: bool
    """If `true`, only include deleted routes.

    If `false`, exclude deleted routes. If empty, all routes will be included.
    """

    network_subset: str
    """If set, only list routes that are contained within this IP range."""

    network_superset: str
    """If set, only list routes that contain this IP range."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    route_id: str
    """UUID of the route."""

    tun_types: List[Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]]
    """The types of tunnels to filter by, separated by commas."""

    tunnel_id: str
    """UUID of the tunnel."""

    virtual_network_id: str
    """UUID of the virtual network."""
