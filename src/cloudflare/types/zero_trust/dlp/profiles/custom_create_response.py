# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = [
    "CustomCreateResponse",
    "CustomCreateResponseItem",
    "CustomCreateResponseItemContextAwareness",
    "CustomCreateResponseItemContextAwarenessSkip",
    "CustomCreateResponseItemEntry",
    "CustomCreateResponseItemEntryPattern",
]


class CustomCreateResponseItemContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class CustomCreateResponseItemContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: CustomCreateResponseItemContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class CustomCreateResponseItemEntryPattern(BaseModel):
    regex: str
    """The regex pattern."""

    validation: Optional[Literal["luhn"]] = None
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class CustomCreateResponseItemEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[CustomCreateResponseItemEntryPattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class CustomCreateResponseItem(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[CustomCreateResponseItemContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[CustomCreateResponseItemEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["custom"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


CustomCreateResponse = List[CustomCreateResponseItem]
