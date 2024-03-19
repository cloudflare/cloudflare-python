# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegionalTieredCacheEditResponse", "Value"]


class Value(BaseModel):
    id: Literal["tc_regional"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class RegionalTieredCacheEditResponse(BaseModel):
    id: Literal["tc_regional"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Value
    """
    Instructs Cloudflare to check a regional hub data center on the way to your
    upper tier. This can help improve performance for smart and custom tiered cache
    topologies.
    """
