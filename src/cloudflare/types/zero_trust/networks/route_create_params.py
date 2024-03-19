# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RouteCreateParams"]


class RouteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    ip_network: Required[str]
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    comment: str
    """Optional remark describing the route."""

    virtual_network_id: object
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """
