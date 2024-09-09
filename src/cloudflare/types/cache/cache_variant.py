# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .cache_variant_identifier import CacheVariantIdentifier

__all__ = ["CacheVariant"]


class CacheVariant(BaseModel):
    id: CacheVariantIdentifier
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
