# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .unnamed_schema_ref_6535d2df7d4d089d21166bd140651307 import UnnamedSchemaRef6535d2df7d4d089d21166bd140651307

__all__ = ["RegionalTieredCacheGetResponse", "Value"]


class Value(BaseModel):
    id: UnnamedSchemaRef6535d2df7d4d089d21166bd140651307
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""


class RegionalTieredCacheGetResponse(BaseModel):
    id: UnnamedSchemaRef6535d2df7d4d089d21166bd140651307
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Value
    """
    Instructs Cloudflare to check a regional hub data center on the way to your
    upper tier. This can help improve performance for smart and custom tiered cache
    topologies.
    """
