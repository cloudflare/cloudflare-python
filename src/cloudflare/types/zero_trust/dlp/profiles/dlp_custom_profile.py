# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["DLPCustomProfile", "ContextAwareness", "ContextAwarenessSkip", "Entry", "EntryPattern"]


class ContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class ContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: ContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class EntryPattern(BaseModel):
    regex: str
    """The regex pattern."""

    validation: Optional[Literal["luhn"]] = None
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class Entry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[EntryPattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class DLPCustomProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

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
