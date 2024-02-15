# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["TunnelArgoTunnelCreateAnArgoTunnelResponse", "Connection"]


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


class TunnelArgoTunnelCreateAnArgoTunnelResponse(BaseModel):
    id: str
    """UUID of the tunnel."""

    connections: List[Connection]
    """The tunnel connections between your origin and Cloudflare's edge."""

    created_at: datetime
    """Timestamp of when the tunnel was created."""

    name: str
    """A user-friendly name for the tunnel."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """
