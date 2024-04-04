# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UnnamedSchemaRef209db30ed499548152d6f3bccf720b54"]


class UnnamedSchemaRef209db30ed499548152d6f3bccf720b54(BaseModel):
    category: Optional[str] = None
    """Name of the category applied."""

    verification_status: Optional[str] = None
    """Result of human review for this categorization."""
