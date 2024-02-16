# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["RouteWorkerRoutesListRoutesResponse", "RouteWorkerRoutesListRoutesResponseItem"]


class RouteWorkerRoutesListRoutesResponseItem(BaseModel):
    id: str
    """Identifier"""

    pattern: str

    script: str
    """Name of the script, used in URLs and route configuration."""


RouteWorkerRoutesListRoutesResponse = List[RouteWorkerRoutesListRoutesResponseItem]
