# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["URLIgnorePatternCreateResponse"]


class URLIgnorePatternCreateResponse(BaseModel):
    """
    A URL ignore pattern that exempts matching URLs from being rewritten by Email Security.
    """

    id: str
    """URL ignore pattern identifier"""

    created_at: datetime

    pattern: str
    """Regular expression matching URLs that should not be rewritten."""

    comments: Optional[str] = None
    """Optional note describing the reason for the ignore pattern."""

    last_modified: Optional[datetime] = None
    """Deprecated, use `modified_at` instead. End of life: November 1, 2026."""

    modified_at: Optional[datetime] = None
