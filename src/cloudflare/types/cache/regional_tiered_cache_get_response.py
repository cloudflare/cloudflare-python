# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from .regional_tiered_cache import RegionalTieredCache

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RegionalTieredCacheGetResponse", "Value"]


class Value(BaseModel):
    id: RegionalTieredCache
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class RegionalTieredCacheGetResponse(BaseModel):
    id: RegionalTieredCache
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Value
    """
    Instructs Cloudflare to check a regional hub data center on the way to your
    upper tier. This can help improve performance for smart and custom tiered cache
    topologies.
    """
