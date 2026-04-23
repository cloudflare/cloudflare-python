# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TunnelListParams"]


class TunnelListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    exclude_prefix: str

    existed_at: str
    """
    If provided, include only resources that were created (and not deleted) before
    this time. URL encoded.
    """

    include_prefix: str

    is_deleted: bool
    """If `true`, only include deleted tunnels.

    If `false`, exclude deleted tunnels. If empty, all tunnels will be included.
    """

    name: str
    """A user-friendly name for the tunnel."""

    page: float
    """Page number of paginated results."""

    per_page: float
    """Number of results to display."""

    status: Literal["inactive", "degraded", "healthy", "down"]
    """The status of the tunnel.

    Valid values are `inactive` (tunnel has never been run), `degraded` (tunnel is
    active and able to serve traffic but in an unhealthy state), `healthy` (tunnel
    is active and able to serve traffic), or `down` (tunnel can not serve traffic as
    it has no connections to the Cloudflare Edge).
    """

    tun_types: List[Literal["cfd_tunnel", "warp_connector", "warp", "magic", "ip_sec", "gre", "cni"]]
    """The types of tunnels to filter by, separated by commas."""

    uuid: str
    """UUID of the tunnel."""

    was_active_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    was_inactive_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
