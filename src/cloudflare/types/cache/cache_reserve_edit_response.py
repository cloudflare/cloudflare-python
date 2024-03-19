# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CacheReserveEditResponse"]


class CacheReserveEditResponse(BaseModel):
    id: Literal["cache_reserve"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["on", "off"]
    """Value of the Cache Reserve zone setting."""
