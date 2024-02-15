# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["RouteDeleteResponse"]


class RouteDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_route: Optional[object] = None
