# File generated from our OpenAPI spec by Stainless.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "ProfileListResponse",
    "ProfileListResponseItem",
    "ProfileListResponseItemDLPPredefinedProfile",
    "ProfileListResponseItemDLPPredefinedProfileContextAwareness",
    "ProfileListResponseItemDLPPredefinedProfileContextAwarenessSkip",
    "ProfileListResponseItemDLPPredefinedProfileEntry",
    "ProfileListResponseItemDLPCustomProfile",
    "ProfileListResponseItemDLPCustomProfileContextAwareness",
    "ProfileListResponseItemDLPCustomProfileContextAwarenessSkip",
    "ProfileListResponseItemDLPCustomProfileEntry",
    "ProfileListResponseItemDLPCustomProfileEntryPattern",
    "ProfileListResponseItemDLPIntegrationProfile",
    "ProfileListResponseItemDLPIntegrationProfileEntry",
]


class ProfileListResponseItemDLPPredefinedProfileContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class ProfileListResponseItemDLPPredefinedProfileContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: ProfileListResponseItemDLPPredefinedProfileContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class ProfileListResponseItemDLPPredefinedProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    profile_id: Optional[object] = None
    """ID of the parent profile"""


class ProfileListResponseItemDLPPredefinedProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[ProfileListResponseItemDLPPredefinedProfileContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    entries: Optional[List[ProfileListResponseItemDLPPredefinedProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["predefined"]] = None
    """The type of the profile."""


class ProfileListResponseItemDLPCustomProfileContextAwarenessSkip(BaseModel):
    files: bool
    """If the content type is a file, skip context analysis and return all matches."""


class ProfileListResponseItemDLPCustomProfileContextAwareness(BaseModel):
    enabled: bool
    """
    If true, scan the context of predefined entries to only return matches
    surrounded by keywords.
    """

    skip: ProfileListResponseItemDLPCustomProfileContextAwarenessSkip
    """Content types to exclude from context analysis and return all matches."""


class ProfileListResponseItemDLPCustomProfileEntryPattern(BaseModel):
    regex: str
    """The regex pattern."""

    validation: Optional[Literal["luhn"]] = None
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class ProfileListResponseItemDLPCustomProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[ProfileListResponseItemDLPCustomProfileEntryPattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class ProfileListResponseItemDLPCustomProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: Optional[ProfileListResponseItemDLPCustomProfileContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[ProfileListResponseItemDLPCustomProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["custom"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


class ProfileListResponseItemDLPIntegrationProfileEntry(BaseModel):
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


class ProfileListResponseItemDLPIntegrationProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[ProfileListResponseItemDLPIntegrationProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["integration"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


ProfileListResponseItem = Union[
    ProfileListResponseItemDLPPredefinedProfile,
    ProfileListResponseItemDLPCustomProfile,
    ProfileListResponseItemDLPIntegrationProfile,
]

ProfileListResponse = List[ProfileListResponseItem]
