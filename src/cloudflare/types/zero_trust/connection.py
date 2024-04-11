# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""

    client_id: Optional[object] = None
    """UUID of the cloudflared instance."""

    client_version: Optional[str] = None
    """The cloudflared version used to establish this connection."""

    colo_name: Optional[str] = None
    """The Cloudflare data center used for this connection."""

    is_pending_reconnect: Optional[bool] = None
    """
    Cloudflare continues to track connections for several minutes after they
    disconnect. This is an optimization to improve latency and reliability of
    reconnecting. If `true`, the connection has disconnected but is still being
    tracked. If `false`, the connection is actively serving traffic.
    """

    opened_at: Optional[datetime] = None
    """Timestamp of when the connection was established."""

    origin_ip: Optional[str] = None
    """The public IP address of the host running cloudflared."""

    uuid: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""
