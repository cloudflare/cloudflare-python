# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Route"]


class Route(BaseModel):
    id: Optional[str] = None
    """UUID of the route."""

    comment: Optional[str] = None
    """Optional remark describing the route."""

    created_at: Optional[datetime] = None
    """Timestamp of when the resource was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """

    network: Optional[str] = None
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tunnel_id: Optional[str] = None
    """UUID of the tunnel."""

    virtual_network_id: Optional[str] = None
    """UUID of the virtual network."""
