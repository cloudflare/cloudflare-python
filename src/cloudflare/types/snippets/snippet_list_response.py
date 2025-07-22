# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SnippetListResponse"]


class SnippetListResponse(BaseModel):
    created_on: datetime
    """The timestamp of when the snippet was created."""

    snippet_name: str
    """The identifying name of the snippet."""

    modified_on: Optional[datetime] = None
    """The timestamp of when the snippet was last modified."""
