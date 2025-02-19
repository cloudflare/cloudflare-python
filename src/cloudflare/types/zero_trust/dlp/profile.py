# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._compat import PYDANTIC_V2
from ...._models import BaseModel

__all__ = [
    "Profile",
    "CustomProfile",
    "CustomProfileEntry",
    "CustomProfileEntryCustomEntry",
    "CustomProfileEntryPredefinedEntry",
    "CustomProfileEntryPredefinedEntryConfidence",
    "CustomProfileEntryIntegrationEntry",
    "CustomProfileEntryExactDataEntry",
    "CustomProfileEntryWordListEntry",
    "PredefinedProfile",
    "PredefinedProfileEntry",
    "PredefinedProfileEntryCustomEntry",
    "PredefinedProfileEntryPredefinedEntry",
    "PredefinedProfileEntryPredefinedEntryConfidence",
    "PredefinedProfileEntryIntegrationEntry",
    "PredefinedProfileEntryExactDataEntry",
    "PredefinedProfileEntryWordListEntry",
    "IntegrationProfile",
    "IntegrationProfileEntry",
    "IntegrationProfileEntryCustomEntry",
    "IntegrationProfileEntryPredefinedEntry",
    "IntegrationProfileEntryPredefinedEntryConfidence",
    "IntegrationProfileEntryIntegrationEntry",
    "IntegrationProfileEntryExactDataEntry",
    "IntegrationProfileEntryWordListEntry",
]


class CustomProfileEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation"""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service
    """


class CustomProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: CustomProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomProfileEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomProfileEntryExactDataEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomProfileEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomProfileEntry: TypeAlias = Union[
    CustomProfileEntryCustomEntry,
    CustomProfileEntryPredefinedEntry,
    CustomProfileEntryIntegrationEntry,
    CustomProfileEntryExactDataEntry,
    CustomProfileEntryWordListEntry,
]


class CustomProfile(BaseModel):
    id: str
    """The id of the profile (uuid)"""

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    context_awareness: ContextAwareness
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    created_at: datetime
    """When the profile was created"""

    entries: List[CustomProfileEntry]

    name: str
    """The name of the profile"""

    ocr_enabled: bool

    type: Literal["custom"]

    updated_at: datetime
    """When the profile was lasted updated"""

    ai_context_enabled: Optional[bool] = None

    confidence_threshold: Optional[Literal["low", "medium", "high", "very_high"]] = None

    description: Optional[str] = None
    """The description of the profile"""


class PredefinedProfileEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation"""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service
    """


class PredefinedProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class PredefinedProfileEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedProfileEntryExactDataEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class PredefinedProfileEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


PredefinedProfileEntry: TypeAlias = Union[
    PredefinedProfileEntryCustomEntry,
    PredefinedProfileEntryPredefinedEntry,
    PredefinedProfileEntryIntegrationEntry,
    PredefinedProfileEntryExactDataEntry,
    PredefinedProfileEntryWordListEntry,
]


class PredefinedProfile(BaseModel):
    id: str
    """The id of the predefined profile (uuid)"""

    allowed_match_count: int

    entries: List[PredefinedProfileEntry]

    name: str
    """The name of the predefined profile"""

    type: Literal["predefined"]

    ai_context_enabled: Optional[bool] = None

    confidence_threshold: Optional[Literal["low", "medium", "high", "very_high"]] = None

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    ocr_enabled: Optional[bool] = None

    open_access: Optional[bool] = None
    """Whether this profile can be accessed by anyone"""


class IntegrationProfileEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation"""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service
    """


class IntegrationProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: IntegrationProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class IntegrationProfileEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationProfileEntryExactDataEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class IntegrationProfileEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


IntegrationProfileEntry: TypeAlias = Union[
    IntegrationProfileEntryCustomEntry,
    IntegrationProfileEntryPredefinedEntry,
    IntegrationProfileEntryIntegrationEntry,
    IntegrationProfileEntryExactDataEntry,
    IntegrationProfileEntryWordListEntry,
]


class IntegrationProfile(BaseModel):
    id: str

    created_at: datetime

    entries: List[IntegrationProfileEntry]

    name: str

    type: Literal["integration"]

    updated_at: datetime

    description: Optional[str] = None
    """The description of the profile"""


Profile: TypeAlias = Union[CustomProfile, PredefinedProfile, IntegrationProfile]

from .profiles.pattern import Pattern
from .context_awareness import ContextAwareness

if PYDANTIC_V2:
    CustomProfile.model_rebuild()
    CustomProfileEntryCustomEntry.model_rebuild()
    CustomProfileEntryPredefinedEntry.model_rebuild()
    CustomProfileEntryPredefinedEntryConfidence.model_rebuild()
    CustomProfileEntryIntegrationEntry.model_rebuild()
    CustomProfileEntryExactDataEntry.model_rebuild()
    CustomProfileEntryWordListEntry.model_rebuild()
    PredefinedProfile.model_rebuild()
    PredefinedProfileEntryCustomEntry.model_rebuild()
    PredefinedProfileEntryPredefinedEntry.model_rebuild()
    PredefinedProfileEntryPredefinedEntryConfidence.model_rebuild()
    PredefinedProfileEntryIntegrationEntry.model_rebuild()
    PredefinedProfileEntryExactDataEntry.model_rebuild()
    PredefinedProfileEntryWordListEntry.model_rebuild()
    IntegrationProfile.model_rebuild()
    IntegrationProfileEntryCustomEntry.model_rebuild()
    IntegrationProfileEntryPredefinedEntry.model_rebuild()
    IntegrationProfileEntryPredefinedEntryConfidence.model_rebuild()
    IntegrationProfileEntryIntegrationEntry.model_rebuild()
    IntegrationProfileEntryExactDataEntry.model_rebuild()
    IntegrationProfileEntryWordListEntry.model_rebuild()
else:
    CustomProfile.update_forward_refs()  # type: ignore
    CustomProfileEntryCustomEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryPredefinedEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryPredefinedEntryConfidence.update_forward_refs()  # type: ignore
    CustomProfileEntryIntegrationEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryExactDataEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryWordListEntry.update_forward_refs()  # type: ignore
    PredefinedProfile.update_forward_refs()  # type: ignore
    PredefinedProfileEntryCustomEntry.update_forward_refs()  # type: ignore
    PredefinedProfileEntryPredefinedEntry.update_forward_refs()  # type: ignore
    PredefinedProfileEntryPredefinedEntryConfidence.update_forward_refs()  # type: ignore
    PredefinedProfileEntryIntegrationEntry.update_forward_refs()  # type: ignore
    PredefinedProfileEntryExactDataEntry.update_forward_refs()  # type: ignore
    PredefinedProfileEntryWordListEntry.update_forward_refs()  # type: ignore
    IntegrationProfile.update_forward_refs()  # type: ignore
    IntegrationProfileEntryCustomEntry.update_forward_refs()  # type: ignore
    IntegrationProfileEntryPredefinedEntry.update_forward_refs()  # type: ignore
    IntegrationProfileEntryPredefinedEntryConfidence.update_forward_refs()  # type: ignore
    IntegrationProfileEntryIntegrationEntry.update_forward_refs()  # type: ignore
    IntegrationProfileEntryExactDataEntry.update_forward_refs()  # type: ignore
    IntegrationProfileEntryWordListEntry.update_forward_refs()  # type: ignore
