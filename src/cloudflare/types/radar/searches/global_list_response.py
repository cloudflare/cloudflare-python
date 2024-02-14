# File generated from our OpenAPI spec by Stainless.

from typing import List

from ...._models import BaseModel

__all__ = ["GlobalListResponse", "Search"]


class Search(BaseModel):
    code: str

    name: str

    type: str


class GlobalListResponse(BaseModel):
    search: List[Search]
