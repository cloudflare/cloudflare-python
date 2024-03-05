# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["D1DatabaseDetails"]


class D1DatabaseDetails(BaseModel):
    created_at: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    file_size: Optional[float] = None
    """The D1 database's size, in bytes."""

    name: Optional[str] = None

    num_tables: Optional[float] = None

    uuid: Optional[str] = None

    version: Optional[str] = None
