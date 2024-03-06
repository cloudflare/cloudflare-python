# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["FilterListResponse", "FilterListResponseItem"]


class FilterListResponseItem(BaseModel):
    id: str
    """Identifier"""

    enabled: bool

    pattern: str


FilterListResponse = List[FilterListResponseItem]
