# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ConnectionGetResponse", "Conn"]


class Conn(BaseModel):
    id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""

    client_id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connector."""

    client_version: Optional[str] = None
    """The cloudflared version used to establish this connection."""

    colo_name: Optional[str] = None
    """The Cloudflare data center used for this connection."""

    opened_at: Optional[datetime] = None
    """Timestamp of when the connection was established."""

    origin_ip: Optional[str] = None
    """The public IP address of the host running WARP Connector."""


class ConnectionGetResponse(BaseModel):
    """
    A WARP Connector client that maintains a connection to a Cloudflare data center.
    """

    id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connector."""

    arch: Optional[str] = None
    """The cloudflared OS architecture used to establish this connection."""

    conns: Optional[List[Conn]] = None
    """
    The WARP Connector Tunnel connections between your origin and Cloudflare's edge.
    """

    features: Optional[List[str]] = None
    """Features enabled for the Cloudflare Tunnel."""

    ha_status: Optional[Literal["offline", "passive", "active"]] = None
    """The HA status of a WARP Connector client."""

    run_at: Optional[datetime] = None
    """Timestamp of when the tunnel connection was started."""

    version: Optional[str] = None
    """The cloudflared version used to establish this connection."""
