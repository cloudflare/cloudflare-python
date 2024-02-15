# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["SpeedAPITestsDeleteResponse"]


class SpeedAPITestsDeleteResponse(BaseModel):
    count: Optional[float] = None
    """Number of items affected."""
