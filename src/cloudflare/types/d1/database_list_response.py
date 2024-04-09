# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DatabaseListResponse"]


class DatabaseListResponse(BaseModel):
    created_at: Optional[str] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[str] = None
