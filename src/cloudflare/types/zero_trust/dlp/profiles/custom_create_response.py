# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from .pattern import Pattern
from ..profile import Profile
from ....._utils import PropertyInfo
from ....._models import BaseModel
from ..context_awareness import ContextAwareness

__all__ = [
    "CustomCreateResponse",
    "CustomProfile",
    "CustomProfileEntry",
    "CustomProfileEntryCustom",
    "CustomProfileEntryPredefined",
    "CustomProfileEntryPredefinedConfidence",
    "CustomProfileEntryIntegration",
    "CustomProfileEntryExactData",
    "CustomProfileEntryWordList",
    "PredefinedProfile",
    "PredefinedProfileEntry",
    "PredefinedProfileEntryCustom",
    "PredefinedProfileEntryPredefined",
    "PredefinedProfileEntryPredefinedConfidence",
    "PredefinedProfileEntryIntegration",
    "PredefinedProfileEntryExactData",
    "PredefinedProfileEntryWordList",
    "IntegrationProfile",
    "IntegrationProfileEntry",
    "IntegrationProfileEntryCustom",
    "IntegrationProfileEntryPredefined",
    "IntegrationProfileEntryPredefinedConfidence",
    "IntegrationProfileEntryIntegration",
    "IntegrationProfileEntryExactData",
    "IntegrationProfileEntryWordList",
]


class CustomProfileEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomProfileEntryPredefinedConfidence(BaseModel):
    available: bool
    """
    Indicates whether this entry can be made more or less sensitive by setting a
    confidence threshold. Profiles that use an entry with `available` set to true
    can use confidence thresholds
    """


class CustomProfileEntryPredefined(BaseModel):
    id: str

    confidence: CustomProfileEntryPredefinedConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class CustomProfileEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomProfileEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomProfileEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomProfileEntry: TypeAlias = Annotated[
    Union[
        CustomProfileEntryCustom,
        CustomProfileEntryPredefined,
        CustomProfileEntryIntegration,
        CustomProfileEntryExactData,
        CustomProfileEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
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

    confidence_threshold: Optional[Literal["low", "medium", "high", "very_high"]] = None

    description: Optional[str] = None
    """The description of the profile"""


class PredefinedProfileEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedProfileEntryPredefinedConfidence(BaseModel):
    available: bool
    """
    Indicates whether this entry can be made more or less sensitive by setting a
    confidence threshold. Profiles that use an entry with `available` set to true
    can use confidence thresholds
    """


class PredefinedProfileEntryPredefined(BaseModel):
    id: str

    confidence: PredefinedProfileEntryPredefinedConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class PredefinedProfileEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedProfileEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class PredefinedProfileEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


PredefinedProfileEntry: TypeAlias = Annotated[
    Union[
        PredefinedProfileEntryCustom,
        PredefinedProfileEntryPredefined,
        PredefinedProfileEntryIntegration,
        PredefinedProfileEntryExactData,
        PredefinedProfileEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
]


class PredefinedProfile(BaseModel):
    id: str
    """The id of the predefined profile (uuid)"""

    allowed_match_count: int

    entries: List[PredefinedProfileEntry]

    name: str
    """The name of the predefined profile"""

    type: Literal["predefined"]

    confidence_threshold: Optional[Literal["low", "medium", "high", "very_high"]] = None

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    ocr_enabled: Optional[bool] = None

    open_access: Optional[bool] = None
    """Whether this profile can be accessed by anyone"""


class IntegrationProfileEntryCustom(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationProfileEntryPredefinedConfidence(BaseModel):
    available: bool
    """
    Indicates whether this entry can be made more or less sensitive by setting a
    confidence threshold. Profiles that use an entry with `available` set to true
    can use confidence thresholds
    """


class IntegrationProfileEntryPredefined(BaseModel):
    id: str

    confidence: IntegrationProfileEntryPredefinedConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class IntegrationProfileEntryIntegration(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationProfileEntryExactData(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class IntegrationProfileEntryWordList(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


IntegrationProfileEntry: TypeAlias = Annotated[
    Union[
        IntegrationProfileEntryCustom,
        IntegrationProfileEntryPredefined,
        IntegrationProfileEntryIntegration,
        IntegrationProfileEntryExactData,
        IntegrationProfileEntryWordList,
    ],
    PropertyInfo(discriminator="type"),
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


CustomCreateResponse: TypeAlias = Union[CustomProfile, PredefinedProfile, IntegrationProfile, List[Profile]]
