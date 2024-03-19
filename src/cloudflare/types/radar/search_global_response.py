# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["SearchGlobalResponse", "Search"]


class Search(BaseModel):
    code: str

    name: str

    type: str


class SearchGlobalResponse(BaseModel):
    search: List[Search]
