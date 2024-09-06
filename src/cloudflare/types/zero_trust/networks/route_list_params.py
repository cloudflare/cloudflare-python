# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from typing import Union

from datetime import datetime

from ...._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["RouteListParams"]


class RouteListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    comment: str
    """Optional remark describing the route."""

    existed_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, include only tunnels that were created (and not deleted) before
    this time.
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

    tun_types: str
    """The types of tunnels to filter separated by a comma."""

    tunnel_id: str
    """UUID of the tunnel."""

    virtual_network_id: str
    """UUID of the virtual network."""
