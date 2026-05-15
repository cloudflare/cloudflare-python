# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["CategoryListResponse"]


class CategoryListResponse(BaseModel):
    id: str
    """Returns the category ID."""

    created_at: str
    """Returns the category creation time."""

    description: str
    """Returns the category description."""

    name: str
    """Returns the category name."""
