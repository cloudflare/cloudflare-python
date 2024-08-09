# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .pattern import Pattern
from ....._models import BaseModel
from ..context_awareness import ContextAwareness

__all__ = ["CustomProfile", "Entry"]


class Entry(BaseModel):
    id: Optional[str] = None
    """Unique identifier for a DLP entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[Pattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[str] = None
    """Unique identifier for a DLP profile"""

    updated_at: Optional[datetime] = None


class CustomProfile(BaseModel):
    id: Optional[str] = None
    """Unique identifier for a DLP profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[Entry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    ocr_enabled: Optional[bool] = None
    """If true, scan images via OCR to determine if any text present matches filters."""

    type: Optional[Literal["custom"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None
