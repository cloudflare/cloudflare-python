# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from .connection import Connection

__all__ = ["TunnelParam"]


class TunnelParam(TypedDict, total=False):
    account_tag: str
    """Cloudflare account ID"""

    connections: Connection
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
