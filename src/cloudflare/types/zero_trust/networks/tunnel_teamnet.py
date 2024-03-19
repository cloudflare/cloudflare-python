# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TunnelTeamnet"]


class TunnelTeamnet(BaseModel):
    id: Optional[str] = None
    """UUID of the route."""

    comment: Optional[str] = None
    """Optional remark describing the route."""

    created_at: Optional[object] = None
    """Timestamp of when the route was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the route was deleted.

    If `null`, the route has not been deleted.
    """

    network: Optional[str] = None
    """The private IPv4 or IPv6 range connected by the route, in CIDR notation."""

    tun_type: Optional[Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]] = None
    """The type of tunnel."""

    tunnel_id: Optional[object] = None
    """UUID of the Cloudflare Tunnel serving the route."""

    tunnel_name: Optional[object] = None
    """The user-friendly name of the Cloudflare Tunnel serving the route."""

    virtual_network_id: Optional[object] = None
    """UUID of the Tunnel Virtual Network this route belongs to.

    If no virtual networks are configured, the route is assigned to the default
    virtual network of the account.
    """

    virtual_network_name: Optional[str] = None
    """A user-friendly name for the virtual network."""
