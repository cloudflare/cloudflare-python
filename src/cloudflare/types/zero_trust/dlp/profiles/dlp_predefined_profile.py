# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["DLPPredefinedProfile", "ContextAwareness", "ContextAwarenessSkip", "Entry"]


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


class Entry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    profile_id: Optional[object] = None
    """ID of the parent profile"""


class DLPPredefinedProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    entries: Optional[List[Entry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    ocr_enabled: Optional[bool] = None
    """If true, scan images via OCR to determine if any text present matches filters."""

    type: Optional[Literal["predefined"]] = None
    """The type of the profile."""
