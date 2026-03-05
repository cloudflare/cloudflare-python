# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["DatabaseListResponse"]


class DatabaseListResponse(BaseModel):
    created_at: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    jurisdiction: Optional[Literal["eu", "fedramp"]] = None
    """Specify the location to restrict the D1 database to run and store data.

    If this option is present, the location hint is ignored.
    """

    name: Optional[str] = None
    """D1 database name."""

    uuid: Optional[str] = None
    """D1 database identifier (UUID)."""

    version: Optional[str] = None
