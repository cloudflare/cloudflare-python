# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """Optional remark describing the route."""

    existed_at: object
    """
    If provided, include only routes that were created (and not deleted) before this
    time.
    """

    is_deleted: object
    """If `true`, only include deleted routes.

    If `false`, exclude deleted routes. If empty, all routes will be included.
    """

    network_subset: object
    """If set, only list routes that are contained within this IP range."""

    network_superset: object
    """If set, only list routes that contain this IP range."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    tun_types: str
    """The types of tunnels to filter separated by a comma."""

    tunnel_id: object
    """UUID of the Cloudflare Tunnel serving the route."""

    virtual_network_id: object
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """
