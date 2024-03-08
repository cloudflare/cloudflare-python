# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["CacheVariants"]


class CacheVariants(BaseModel):
    id: Literal["variants"]
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
