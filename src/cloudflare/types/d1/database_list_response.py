# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DatabaseListResponse"]


class DatabaseListResponse(BaseModel):
    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None
    """D1 database name."""

    uuid: Optional[str] = None
    """D1 database identifier (UUID)."""

    version: Optional[str] = None
