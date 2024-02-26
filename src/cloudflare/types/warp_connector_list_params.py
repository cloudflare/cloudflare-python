# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

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

    was_active_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    was_inactive_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
