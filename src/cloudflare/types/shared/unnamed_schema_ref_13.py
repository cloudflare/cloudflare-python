# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef13"]


class UnnamedSchemaRef13(BaseModel):
    category: Optional[str] = None
    """Name of the category applied."""

    verification_status: Optional[str] = None
    """Result of human review for this categorization."""
