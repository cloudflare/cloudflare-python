# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SnippetListResponse"]


class SnippetListResponse(BaseModel):
    """Define a snippet."""

    created_on: datetime
    """Indicates when the snippet was created."""

    snippet_name: str
    """Identify the snippet."""

    modified_on: Optional[datetime] = None
    """Indicates when the snippet was last modified."""
