# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SmartTieredCacheEditResponse"]


class SmartTieredCacheEditResponse(BaseModel):
    id: Literal["tiered_cache_smart_topology_enable"]
    """The identifier of the caching setting."""

    editable: bool
    """Whether the setting is editable."""

    value: Literal["on", "off"]
    """Value of the Smart Tiered Cache zone setting."""

    modified_on: Optional[datetime] = None
    """Last time this setting was modified."""
