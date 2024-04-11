# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .connection import Connection

__all__ = ["TunnelDeleteResponse"]


class TunnelDeleteResponse(BaseModel):
    id: str
    """UUID of the tunnel."""

    connections: List[Connection]
    """The tunnel connections between your origin and Cloudflare's edge."""

    created_at: datetime
    """Timestamp of when the tunnel was created."""

    name: str
    """A user-friendly name for the tunnel."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the tunnel was deleted.

    If `null`, the tunnel has not been deleted.
    """
