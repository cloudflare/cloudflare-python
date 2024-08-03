# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from .profiles.custom_profile import CustomProfile
from .profiles.predefined_profile import PredefinedProfile

__all__ = ["Profile", "DLPIntegrationProfile", "DLPIntegrationProfileEntry"]


class DLPIntegrationProfileEntry(BaseModel):
    id: Optional[str] = None
    """Unique identifier for a DLP entry"""

    created_at: Optional[datetime] = None

    enabled: Optional[bool] = None
    """Whether the entry is enabled or not."""

    name: Optional[str] = None
    """The name of the entry."""

    profile_id: Optional[str] = None
    """Unique identifier for a DLP profile"""

    updated_at: Optional[datetime] = None


class DLPIntegrationProfile(BaseModel):
    id: Optional[str] = None
    """Unique identifier for a DLP profile"""

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


Profile = Union[PredefinedProfile, CustomProfile, DLPIntegrationProfile]
