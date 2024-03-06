# File generated from our OpenAPI spec by Stainless.

from typing import List

from ..._models import BaseModel

__all__ = ["TSIGListResponse", "TSIGListResponseItem"]


class TSIGListResponseItem(BaseModel):
    id: object

    algo: str
    """TSIG algorithm."""

    name: str
    """TSIG key name."""

    secret: str
    """TSIG secret."""


TSIGListResponse = List[TSIGListResponseItem]
