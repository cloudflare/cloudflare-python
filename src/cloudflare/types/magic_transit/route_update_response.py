# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteUpdateResponse"]


class RouteUpdateResponse(BaseModel):
    modified: Optional[bool] = None

    modified_route: Optional[object] = None
