# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TestDeleteResponse"]


class TestDeleteResponse(BaseModel):
    __test__ = False
    count: Optional[float] = None
    """Number of items affected."""
