# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from .._models import BaseModel

__all__ = ["SpeedDeleteResponse"]


class SpeedDeleteResponse(BaseModel):
    count: Optional[float] = None
    """Number of items affected."""
