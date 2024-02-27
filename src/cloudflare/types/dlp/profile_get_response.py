# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ProfileGetResponse",
    "DLPPredefinedProfile",
    "DLPPredefinedProfileContextAwareness",
    "DLPPredefinedProfileContextAwarenessSkip",
    "DLPPredefinedProfileEntry",
    "DLPCustomProfile",
    "DLPCustomProfileContextAwareness",
    "DLPCustomProfileContextAwarenessSkip",
    "DLPCustomProfileEntry",
    "DLPCustomProfileEntryPattern",
    "DLPIntegrationProfile",
    "DLPIntegrationProfileEntry",
]


class DLPPredefinedProfileContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class DLPPredefinedProfileContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: DLPPredefinedProfileContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class DLPPredefinedProfileEntry(BaseModel):
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

    context_awareness: Optional[DLPPredefinedProfileContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    entries: Optional[List[DLPPredefinedProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["predefined"]] = None
    """The type of the profile."""


class DLPCustomProfileContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class DLPCustomProfileContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: DLPCustomProfileContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class DLPCustomProfileEntryPattern(BaseModel):
    regex: str
    """The regex pattern."""

    validation: Optional[Literal["luhn"]] = None
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class DLPCustomProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[DLPCustomProfileEntryPattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class DLPCustomProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[DLPCustomProfileContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[DLPCustomProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["custom"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


class DLPIntegrationProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class DLPIntegrationProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[DLPIntegrationProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["integration"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


ProfileGetResponse = Union[DLPPredefinedProfile, DLPCustomProfile, DLPIntegrationProfile]
