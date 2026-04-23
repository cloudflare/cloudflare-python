# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostnameRouteEditParams"]


class HostnameRouteEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """An optional description of the hostname route."""

    hostname: str
    """The hostname of the route."""

    tunnel_id: str
    """UUID of the tunnel."""
