# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DatabaseListResponse"]


class DatabaseListResponse(BaseModel):
    created_at: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[str] = None
