# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DatabaseCreateResponse"]


class DatabaseCreateResponse(BaseModel):
    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[str] = None
