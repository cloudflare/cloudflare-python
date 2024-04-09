# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["RouteParam"]


class RouteParam(TypedDict, total=False):
    comment: str
    """Optional remark describing the route."""

    created_at: object
    """Timestamp of when the route was created."""

    network: str
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tunnel_id: object
    """UUID of the Cloudflare Tunnel serving the route."""

    virtual_network_id: object
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """
