# File generated from our OpenAPI spec by Stainless.

from typing_extensions import Literal

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["CacheRegionalTieredCachesResponse", "Value"]


class Value(BaseModel):
    id: Literal["tc_regional"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class CacheRegionalTieredCachesResponse(BaseModel):
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
