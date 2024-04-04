# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .unnamed_schema_ref_2b5e755404a4bfd7892291ce97c4968d import UnnamedSchemaRef2b5e755404a4bfd7892291ce97c4968d

__all__ = ["CacheReserveClearResponse"]


class CacheReserveClearResponse(BaseModel):
    id: UnnamedSchemaRef2b5e755404a4bfd7892291ce97c4968d
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    start_ts: datetime
    """The time that the latest Cache Reserve Clear operation started."""

    state: Literal["In-progress", "Completed"]
    """The current state of the Cache Reserve Clear operation."""

    end_ts: Optional[datetime] = None
    """The time that the latest Cache Reserve Clear operation completed."""
