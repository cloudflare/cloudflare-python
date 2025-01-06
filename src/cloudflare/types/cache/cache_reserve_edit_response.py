# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .cache_reserve import CacheReserve

__all__ = ["CacheReserveEditResponse"]


class CacheReserveEditResponse(BaseModel):
    id: CacheReserve
    """ID of the zone setting."""

    editable: bool
    """Whether the setting is editable"""

    value: Literal["on", "off"]
    """The value of the feature"""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
