# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["Connection"]


class Connection(BaseModel):
    colo_name: Optional[str] = None
    """The Cloudflare data center used for this connection."""

    is_pending_reconnect: Optional[bool] = None
    """
    Cloudflare continues to track connections for several minutes after they
    disconnect. This is an optimization to improve latency and reliability of
    reconnecting. If `true`, the connection has disconnected but is still being
    tracked. If `false`, the connection is actively serving traffic.
    """

    uuid: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""
