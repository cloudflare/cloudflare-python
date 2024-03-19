# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .profiles import DLPCustomProfile, DLPPredefinedProfile
from ...._models import BaseModel

__all__ = ["ProfileGetResponse", "DLPIntegrationProfile", "DLPIntegrationProfileEntry"]


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
