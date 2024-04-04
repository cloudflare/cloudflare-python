# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..shared import UnnamedSchemaRef144
from ..._models import BaseModel

__all__ = ["CacheReserveGetResponse"]


class CacheReserveGetResponse(BaseModel):
    id: UnnamedSchemaRef144
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""

    value: Literal["on", "off"]
    """Value of the Cache Reserve zone setting."""
