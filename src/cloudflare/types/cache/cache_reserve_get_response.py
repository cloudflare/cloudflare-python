# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .cache_reserve import CacheReserve

__all__ = ["CacheReserveGetResponse"]


class CacheReserveGetResponse(BaseModel):
    id: CacheReserve
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["on", "off"]
    """Value of the Cache Reserve zone setting."""
