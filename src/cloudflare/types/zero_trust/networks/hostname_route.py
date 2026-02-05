# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["HostnameRoute"]


class HostnameRoute(BaseModel):
    id: Optional[str] = None
    """The hostname route ID."""

    comment: Optional[str] = None
    """An optional description of the hostname route."""

    created_at: Optional[datetime] = None
    """Timestamp of when the resource was created."""

    deleted_at: Optional[datetime] = None
    """Timestamp of when the resource was deleted.

    If `null`, the resource has not been deleted.
    """

    hostname: Optional[str] = None
    """The hostname of the route."""

    tunnel_id: Optional[str] = None
    """UUID of the tunnel."""

    tunnel_name: Optional[str] = None
    """A user-friendly name for a tunnel."""
