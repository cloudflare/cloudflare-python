# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated, Literal

from typing import Union

from datetime import datetime

from ..._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo

__all__ = ["WARPConnectorListParams"]


class WARPConnectorListParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID"""

    exclude_prefix: str

    existed_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """
    If provided, include only tunnels that were created (and not deleted) before
    this time.
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

    uuid: str
    """UUID of the tunnel."""

    was_active_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    was_inactive_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
