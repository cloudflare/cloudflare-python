# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .profiles.pattern import Pattern
from .context_awareness import ContextAwareness

__all__ = [
    "Profile",
    "CustomProfile",
    "CustomProfileEntry",
    "CustomProfileEntryCustomEntry",
    "CustomProfileEntryPredefinedEntry",
    "CustomProfileEntryPredefinedEntryConfidence",
    "CustomProfileEntryPredefinedEntryVariant",
    "CustomProfileEntryIntegrationEntry",
    "CustomProfileEntryExactDataEntry",
    "CustomProfileEntryDocumentFingerprintEntry",
    "CustomProfileEntryWordListEntry",
    "PredefinedProfile",
    "PredefinedProfileEntry",
    "PredefinedProfileEntryCustomEntry",
    "PredefinedProfileEntryPredefinedEntry",
    "PredefinedProfileEntryPredefinedEntryConfidence",
    "PredefinedProfileEntryPredefinedEntryVariant",
    "PredefinedProfileEntryIntegrationEntry",
    "PredefinedProfileEntryExactDataEntry",
    "PredefinedProfileEntryDocumentFingerprintEntry",
    "PredefinedProfileEntryWordListEntry",
    "IntegrationProfile",
    "IntegrationProfileEntry",
    "IntegrationProfileEntryCustomEntry",
    "IntegrationProfileEntryPredefinedEntry",
    "IntegrationProfileEntryPredefinedEntryConfidence",
    "IntegrationProfileEntryPredefinedEntryVariant",
    "IntegrationProfileEntryIntegrationEntry",
    "IntegrationProfileEntryExactDataEntry",
    "IntegrationProfileEntryDocumentFingerprintEntry",
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
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class CustomProfileEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class CustomProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: CustomProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[CustomProfileEntryPredefinedEntryVariant] = None


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

    case_sensitive: bool
    """
    Only applies to custom word lists. Determines if the words should be matched in
    a case-sensitive manner Cannot be set to false if secret is true
    """

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class CustomProfileEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

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
    CustomProfileEntryDocumentFingerprintEntry,
    CustomProfileEntryWordListEntry,
]


class CustomProfile(BaseModel):
    id: str
    """The id of the profile (uuid)."""

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    created_at: datetime
    """When the profile was created."""

    entries: List[CustomProfileEntry]

    name: str
    """The name of the profile."""

    ocr_enabled: bool

    type: Literal["custom"]

    updated_at: datetime
    """When the profile was lasted updated."""

    ai_context_enabled: Optional[bool] = None

    confidence_threshold: Optional[Literal["low", "medium", "high", "very_high"]] = None

    context_awareness: Optional[ContextAwareness] = None
    """
    Scan the context of predefined entries to only return matches surrounded by
    keywords.
    """

    description: Optional[str] = None
    """The description of the profile."""


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
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class PredefinedProfileEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class PredefinedProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[PredefinedProfileEntryPredefinedEntryVariant] = None


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

    case_sensitive: bool
    """
    Only applies to custom word lists. Determines if the words should be matched in
    a case-sensitive manner Cannot be set to false if secret is true
    """

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class PredefinedProfileEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

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
    PredefinedProfileEntryDocumentFingerprintEntry,
    PredefinedProfileEntryWordListEntry,
]


class PredefinedProfile(BaseModel):
    id: str
    """The id of the predefined profile (uuid)."""

    allowed_match_count: int

    entries: List[PredefinedProfileEntry]

    name: str
    """The name of the predefined profile."""

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
    """Whether this profile can be accessed by anyone."""


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
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class IntegrationProfileEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class IntegrationProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: IntegrationProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[IntegrationProfileEntryPredefinedEntryVariant] = None


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

    case_sensitive: bool
    """
    Only applies to custom word lists. Determines if the words should be matched in
    a case-sensitive manner Cannot be set to false if secret is true
    """

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

    updated_at: datetime


class IntegrationProfileEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

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
    IntegrationProfileEntryDocumentFingerprintEntry,
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
    """The description of the profile."""


Profile: TypeAlias = Union[CustomProfile, PredefinedProfile, IntegrationProfile]
