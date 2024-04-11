# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .zero_trust import Connection

__all__ = ["WARPConnectorCreateResponse", "TunnelCfdTunnel", "TunnelWARPConnectorTunnel"]


class TunnelCfdTunnel(BaseModel):
    id: Optional[str] = None
    """UUID of the tunnel."""

    account_tag: Optional[str] = None
    """Cloudflare account ID"""

    connections: Optional[Connection] = None
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
    """Timestamp of when the tunnel was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """

    metadata: Optional[object] = None
    """Metadata associated with the tunnel."""

    name: Optional[str] = None
    """A user-friendly name for the tunnel."""

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


class TunnelWARPConnectorTunnel(BaseModel):
    id: Optional[str] = None
    """UUID of the tunnel."""

    account_tag: Optional[str] = None
    """Cloudflare account ID"""

    connections: Optional[Connection] = None
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
    """Timestamp of when the tunnel was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """

    metadata: Optional[object] = None
    """Metadata associated with the tunnel."""

    name: Optional[str] = None
    """A user-friendly name for the tunnel."""

    status: Optional[str] = None
    """The status of the tunnel.

    Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is
    active and able to serve traffic but in an unhealthy state), `healthy` (tunnel
    is active and able to serve traffic), or `down` (tunnel can not serve traffic as
    it has no connections to the Cloudflare Edge).
    """

    tun_type: Optional[Literal["cfd_tunnel", "warp_connector", "ip_sec", "gre", "cni"]] = None
    """The type of tunnel."""


WARPConnectorCreateResponse = Union[TunnelCfdTunnel, TunnelWARPConnectorTunnel]
