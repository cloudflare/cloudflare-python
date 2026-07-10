# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel

__all__ = ["AuditProductCategoriesResponse", "Product"]


class Product(BaseModel):
    """A resource product within a product category."""

    label: Optional[str] = None
    """A human-readable label for the product."""

    value: Optional[str] = None
    """The resource_product value that the product category expands to."""


class AuditProductCategoriesResponse(BaseModel):
    """A predefined product category and the resource products it expands to."""

    label: Optional[str] = None
    """A human-readable label for the product category."""

    products: Optional[List[Product]] = None
    """The resource products that the product category expands to."""

    value: Optional[str] = None
    """The product category identifier used with the product_category filter."""
