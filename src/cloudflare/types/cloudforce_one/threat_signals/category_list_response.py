# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ...._models import BaseModel

__all__ = ["CategoryListResponse", "Category"]


class Category(BaseModel):
    id: str
    """Wire value accepted by the feed `category_id` field."""

    description: str
    """Plain-language description of the category."""

    name: str
    """Human-readable display label."""


class CategoryListResponse(BaseModel):
    categories: List[Category]
