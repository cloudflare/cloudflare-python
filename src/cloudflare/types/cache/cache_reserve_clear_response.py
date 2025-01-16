# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .state import State
from ..._models import BaseModel
from .cache_reserve_clear import CacheReserveClear

__all__ = ["CacheReserveClearResponse"]


class CacheReserveClearResponse(BaseModel):
    id: CacheReserveClear
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    start_ts: datetime
    """The time that the latest Cache Reserve Clear operation started."""

    state: State
    """The current state of the Cache Reserve Clear operation."""

    end_ts: Optional[datetime] = None
    """The time that the latest Cache Reserve Clear operation completed."""
