# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from .index_dimension_configuration import IndexDimensionConfiguration

__all__ = ["CreateIndex"]


class CreateIndex(BaseModel):
    config: Optional[IndexDimensionConfiguration] = None

    created_on: Optional[datetime] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    description: Optional[str] = None
    """Specifies the description of the index."""

    modified_on: Optional[datetime] = None
    """Specifies the timestamp the resource was modified as an ISO8601 string."""

    name: Optional[str] = None
