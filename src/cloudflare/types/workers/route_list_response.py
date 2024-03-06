# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["RouteListResponse", "RouteListResponseItem"]


class RouteListResponseItem(BaseModel):
    id: str
    """Identifier"""

    pattern: str

    script: str
    """Name of the script, used in URLs and route configuration."""


RouteListResponse = List[RouteListResponseItem]
