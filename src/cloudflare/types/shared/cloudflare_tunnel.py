# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CloudflareTunnel", "Connection"]


class Connection(BaseModel):
    id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""

    client_id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connector."""

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


class CloudflareTunnel(BaseModel):
    id: Optional[str] = None
    """UUID of the tunnel."""

    account_tag: Optional[str] = None
    """Cloudflare account ID"""

    connections: Optional[List[Connection]] = None
    """The Cloudflare Tunnel connections between your origin and Cloudflare's edge."""

    conns_active_at: Optional[datetime] = None
    """
    Timestamp of when the tunnel established at least one connection to Cloudflare's
    edge. If `null`, the tunnel is inactive.
    """

    conns_inactive_at: Optional[datetime] = None
    """
    Timestamp of when the tunnel became inactive (no connections to Cloudflare's
    edge). If `null`, the tunnel is active.
    """

    created_at: Optional[datetime] = None
    """Timestamp of when the resource was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """

    metadata: Optional[object] = None
    """Metadata associated with the tunnel."""

    name: Optional[str] = None
    """A user-friendly name for a tunnel."""

    remote_config: Optional[bool] = None
    """If `true`, the tunnel can be configured remotely from the Zero Trust dashboard.

    If `false`, the tunnel must be configured locally on the origin machine.
    """

    status: Optional[str] = None
    """The status of the tunnel.

    Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is
    active and able to serve traffic but in an unhealthy state), `healthy` (tunnel
    is active and able to serve traffic), or `down` (tunnel can not serve traffic as
    it has no connections to the Cloudflare Edge).
    """

    tun_type: Optional[Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]] = None
    """The type of tunnel."""
