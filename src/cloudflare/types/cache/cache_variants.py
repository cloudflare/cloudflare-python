# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .unnamed_schema_ref_669bfbb16c0913af7077c3c194fbfcd0 import UnnamedSchemaRef669bfbb16c0913af7077c3c194fbfcd0

__all__ = ["CacheVariants"]


class CacheVariants(BaseModel):
    id: UnnamedSchemaRef669bfbb16c0913af7077c3c194fbfcd0
    """ID of the zone setting."""

    modified_on: Optional[datetime] = None
    """last time this setting was modified."""
