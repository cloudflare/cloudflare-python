# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .unnamed_schema_ref_37c385b4ebac5c7a6475b3f81ef9a7ad import UnnamedSchemaRef37c385b4ebac5c7a6475b3f81ef9a7ad

__all__ = ["CacheReserveEditResponse"]


class CacheReserveEditResponse(BaseModel):
    id: UnnamedSchemaRef37c385b4ebac5c7a6475b3f81ef9a7ad
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["on", "off"]
    """Value of the Cache Reserve zone setting."""
