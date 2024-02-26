# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteEmptyResponse"]


class RouteEmptyResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_routes: Optional[object] = None
