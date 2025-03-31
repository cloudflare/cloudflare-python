# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .regional_tiered_cache import RegionalTieredCache

__all__ = ["RegionalTieredCacheGetResponse"]


class RegionalTieredCacheGetResponse(BaseModel):
    id: RegionalTieredCache
    """ID of the zone setting."""

    editable: bool
    """Whether the setting is editable"""

    value: Literal["on", "off"]
    """The value of the feature"""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
