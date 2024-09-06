# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["RouteCreateParams"]


class RouteCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    network: Required[str]
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tunnel_id: Required[str]
    """UUID of the tunnel."""

    comment: str
    """Optional remark describing the route."""

    virtual_network_id: str
    """UUID of the virtual network."""
