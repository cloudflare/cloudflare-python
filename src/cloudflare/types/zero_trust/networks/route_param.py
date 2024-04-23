# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["RouteParam"]


class RouteParam(TypedDict, total=False):
    comment: str
    """Optional remark describing the route."""

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp of when the resource was created."""

    deleted_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """

    network: str
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    virtual_network_id: str
    """UUID of the virtual network."""
