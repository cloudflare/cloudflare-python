# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TunnelParam", "Connection"]


class Connection(TypedDict, total=False):
    client_id: object
    """UUID of the cloudflared instance."""

    client_version: str
    """The cloudflared version used to establish this connection."""

    colo_name: str
    """The Cloudflare data center used for this connection."""

    is_pending_reconnect: bool
    """
    Cloudflare continues to track connections for several minutes after they
    disconnect. This is an optimization to improve latency and reliability of
    reconnecting. If `true`, the connection has disconnected but is still being
    tracked. If `false`, the connection is actively serving traffic.
    """

    opened_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp of when the connection was established."""

    origin_ip: str
    """The public IP address of the host running cloudflared."""


class TunnelParam(TypedDict, total=False):
    account_tag: str
    """Cloudflare account ID"""

    connections: Iterable[Connection]
    """The Cloudflare Tunnel connections between your origin and Cloudflare's edge."""

    conns_active_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Timestamp of when the tunnel established at least one connection to Cloudflare's
    edge. If `null`, the tunnel is inactive.
    """

    conns_inactive_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """
    Timestamp of when the tunnel became inactive (no connections to Cloudflare's
    edge). If `null`, the tunnel is active.
    """

    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Timestamp of when the tunnel was created."""

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """

    metadata: object
    """Metadata associated with the tunnel."""

    name: str
    """A user-friendly name for the tunnel."""

    remote_config: bool
    """If `true`, the tunnel can be configured remotely from the Zero Trust dashboard.

    If `false`, the tunnel must be configured locally on the origin machine.
    """

    status: str
    """The status of the tunnel.

    Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is
    active and able to serve traffic but in an unhealthy state), `healthy` (tunnel
    is active and able to serve traffic), or `down` (tunnel can not serve traffic as
    it has no connections to the Cloudflare Edge).
    """

    tun_type: Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]
    """The type of tunnel."""
