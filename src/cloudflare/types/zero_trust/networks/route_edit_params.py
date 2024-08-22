# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["RouteEditParams"]

class RouteEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """Optional remark describing the route."""

    network: str
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tunnel_id: str
    """UUID of the tunnel."""

    virtual_network_id: str
    """UUID of the virtual network."""