# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .connection import Connection

__all__ = ["TunnelCreateResponse"]


class TunnelCreateResponse(BaseModel):
    id: str
    """UUID of the tunnel."""

    connections: List[Connection]
    """The tunnel connections between your origin and Cloudflare's edge."""

    created_at: datetime
    """Timestamp of when the resource was created."""

    name: str
    """A user-friendly name for a tunnel."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """
