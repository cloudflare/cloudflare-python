# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Teamnet"]


class Teamnet(BaseModel):
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

    tun_type: Optional[Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]] = None
    """The type of tunnel."""

    tunnel_id: Optional[str] = None
    """UUID of the tunnel."""

    tunnel_name: Optional[str] = None
    """A user-friendly name for a tunnel."""

    virtual_network_id: Optional[str] = None
    """UUID of the virtual network."""

    virtual_network_name: Optional[str] = None
    """A user-friendly name for the virtual network."""
