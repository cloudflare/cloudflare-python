# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["URLIgnorePatternEditResponse"]


class URLIgnorePatternEditResponse(BaseModel):
    """
    A URL ignore pattern that exempts matching URLs from Email Security's URL rewriting.
    """

    id: str
    """URL ignore pattern identifier."""

    created_at: datetime

    pattern: str
    """Regular expression identifying URLs to exempt from rewriting."""

    comments: Optional[str] = None
    """Optional note describing the reason for the ignore pattern."""

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None
