# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IndexListResponse", "IndexListResponseItem", "IndexListResponseItemConfig"]


class IndexListResponseItemConfig(BaseModel):
    dimensions: int
    """Specifies the number of dimensions for the index"""

    metric: Literal["cosine", "euclidean", "dot-product"]
    """Specifies the type of metric to use calculating distance."""


class IndexListResponseItem(BaseModel):
    config: Optional[IndexListResponseItemConfig] = None

    created_on: Optional[object] = None
    """Specifies the timestamp the resource was created as an ISO8601 string."""

    description: Optional[str] = None
    """Specifies the description of the index."""

    modified_on: Optional[object] = None
    """Specifies the timestamp the resource was modified as an ISO8601 string."""

    name: Optional[str] = None


IndexListResponse = List[IndexListResponseItem]
