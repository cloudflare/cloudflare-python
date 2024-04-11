# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ..connection import Connection

__all__ = ["Client"]


class Client(BaseModel):
    id: Optional[str] = None
    """UUID of the Cloudflare Tunnel connection."""

    arch: Optional[str] = None
    """The cloudflared OS architecture used to establish this connection."""

    config_version: Optional[int] = None
    """The version of the remote tunnel configuration.

    Used internally to sync cloudflared with the Zero Trust dashboard.
    """

    conns: Optional[Connection] = None
    """The Cloudflare Tunnel connections between your origin and Cloudflare's edge."""

    features: Optional[List[str]] = None
    """Features enabled for the Cloudflare Tunnel."""

    run_at: Optional[datetime] = None
    """Timestamp of when the tunnel connection was started."""

    version: Optional[str] = None
    """The cloudflared version used to establish this connection."""
