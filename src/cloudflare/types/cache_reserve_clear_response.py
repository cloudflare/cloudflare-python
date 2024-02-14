# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["CacheReserveClearResponse"]


class CacheReserveClearResponse(BaseModel):
    id: Literal["cache_reserve_clear"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    start_ts: datetime
    """The time that the latest Cache Reserve Clear operation started."""

    state: Literal["In-progress", "Completed"]
    """The current state of the Cache Reserve Clear operation."""

    end_ts: Optional[datetime] = None
    """The time that the latest Cache Reserve Clear operation completed."""
