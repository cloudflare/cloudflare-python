# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TunnelParam", "Connection"]


class Connection(TypedDict, total=False):
    colo_name: str
    """The Cloudflare data center used for this connection."""

    is_pending_reconnect: bool
    """
    Cloudflare continues to track connections for several minutes after they
    disconnect. This is an optimization to improve latency and reliability of
    reconnecting. If `true`, the connection has disconnected but is still being
    tracked. If `false`, the connection is actively serving traffic.
    """


class TunnelParam(TypedDict, total=False):
    connections: Required[Iterable[Connection]]
    """The tunnel connections between your origin and Cloudflare's edge."""

    created_at: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Timestamp of when the tunnel was created."""

    name: Required[str]
    """A user-friendly name for the tunnel."""

    deleted_at: Annotated[Union[str, datetime, None], PropertyInfo(format="iso8601")]
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """
