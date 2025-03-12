# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from ...._models import BaseModel

__all__ = ["CountryListResponse", "CountryListResponseItem", "CountryListResponseItemResult"]


class CountryListResponseItemResult(BaseModel):
    alpha3: str

    name: str


class CountryListResponseItem(BaseModel):
    result: List[CountryListResponseItemResult]

    success: str


CountryListResponse: TypeAlias = List[CountryListResponseItem]
