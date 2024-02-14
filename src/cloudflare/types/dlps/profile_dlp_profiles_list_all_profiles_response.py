# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = [
    "ProfileDLPProfilesListAllProfilesResponse",
    "ProfileDLPProfilesListAllProfilesResponseItem",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfile",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfileEntry",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfile",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntry",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntryPattern",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfile",
    "ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfileEntry",
]


class ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    profile_id: Optional[object] = None
    """ID of the parent profile"""


class ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    entries: Optional[List[ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["predefined"]] = None
    """The type of the profile."""


class ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntryPattern(BaseModel):
    regex: str
    """The regex pattern."""

    validation: Optional[Literal["luhn"]] = None
    """Validation algorithm for the pattern.

    This algorithm will get run on potential matches, and if it returns false, the
    entry will not be matched.
    """


class ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntry(BaseModel):
    id: Optional[str] = None
    """The ID for this entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    pattern: Optional[ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntryPattern] = None
    """A pattern that matches an entry"""

    profile_id: Optional[object] = None
    """ID of the parent profile"""

    updated_at: Optional[datetime] = None


class ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    allowed_match_count: Optional[float] = None
    """Related DLP policies will trigger when the match count exceeds the number set."""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["custom"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


class ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfileEntry(BaseModel):
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


class ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfile(BaseModel):
    id: Optional[str] = None
    """The ID for this profile"""

    created_at: Optional[datetime] = None

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfileEntry]] = None
    """The entries for this profile."""

    name: Optional[str] = None
    """The name of the profile."""

    type: Optional[Literal["integration"]] = None
    """The type of the profile."""

    updated_at: Optional[datetime] = None


ProfileDLPProfilesListAllProfilesResponseItem = Union[
    ProfileDLPProfilesListAllProfilesResponseItemDLPPredefinedProfile,
    ProfileDLPProfilesListAllProfilesResponseItemDLPCustomProfile,
    ProfileDLPProfilesListAllProfilesResponseItemDLPIntegrationProfile,
]

ProfileDLPProfilesListAllProfilesResponse = List[ProfileDLPProfilesListAllProfilesResponseItem]
