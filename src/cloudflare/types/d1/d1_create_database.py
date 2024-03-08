# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["D1CreateDatabase"]


class D1CreateDatabase(BaseModel):
    created_at: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    name: Optional[str] = None

    uuid: Optional[str] = None

    version: Optional[str] = None
