# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["InternetServiceCategoriesResponse", "Categories0"]


class Categories0(BaseModel):
    name: str


class InternetServiceCategoriesResponse(BaseModel):
    categories_0: List[Categories0]
