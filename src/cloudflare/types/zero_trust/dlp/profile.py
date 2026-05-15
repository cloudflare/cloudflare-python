# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._compat import (  # type: ignore[attr-defined]
    PYDANTIC_V2,  # pyright: ignore[reportAttributeAccessIssue, reportUnknownVariableType]
)
from ...._models import BaseModel

__all__ = [
    "Profile",
    "CustomProfile",
    "CustomProfileEntry",
    "CustomProfileEntryCustomEntry",
    "CustomProfileEntryCustomPromptTopicEntry",
    "CustomProfileEntryPredefinedEntry",
    "CustomProfileEntryPredefinedEntryConfidence",
    "CustomProfileEntryPredefinedEntryVariant",
    "CustomProfileEntryPredefinedEntryVariantUnionMember0",
    "CustomProfileEntryPredefinedEntryVariantUnionMember1",
    "CustomProfileEntryIntegrationEntry",
    "CustomProfileEntryExactDataEntry",
    "CustomProfileEntryDocumentFingerprintEntry",
    "CustomProfileEntryWordListEntry",
    "CustomProfileSensitivityLevel",
    "CustomProfileSharedEntry",
    "CustomProfileSharedEntryCustomEntry",
    "CustomProfileSharedEntryCustomPromptTopicEntry",
    "CustomProfileSharedEntryPredefinedEntry",
    "CustomProfileSharedEntryPredefinedEntryConfidence",
    "CustomProfileSharedEntryPredefinedEntryVariant",
    "CustomProfileSharedEntryPredefinedEntryVariantUnionMember0",
    "CustomProfileSharedEntryPredefinedEntryVariantUnionMember1",
    "CustomProfileSharedEntryIntegrationEntry",
    "CustomProfileSharedEntryExactDataEntry",
    "CustomProfileSharedEntryDocumentFingerprintEntry",
    "CustomProfileSharedEntryWordListEntry",
    "PredefinedProfile",
    "PredefinedProfileEntry",
    "PredefinedProfileEntryCustomEntry",
    "PredefinedProfileEntryCustomPromptTopicEntry",
    "PredefinedProfileEntryPredefinedEntry",
    "PredefinedProfileEntryPredefinedEntryConfidence",
    "PredefinedProfileEntryPredefinedEntryVariant",
    "PredefinedProfileEntryPredefinedEntryVariantUnionMember0",
    "PredefinedProfileEntryPredefinedEntryVariantUnionMember1",
    "PredefinedProfileEntryIntegrationEntry",
    "PredefinedProfileEntryExactDataEntry",
    "PredefinedProfileEntryDocumentFingerprintEntry",
    "PredefinedProfileEntryWordListEntry",
    "IntegrationProfile",
    "IntegrationProfileEntry",
    "IntegrationProfileEntryCustomEntry",
    "IntegrationProfileEntryCustomPromptTopicEntry",
    "IntegrationProfileEntryPredefinedEntry",
    "IntegrationProfileEntryPredefinedEntryConfidence",
    "IntegrationProfileEntryPredefinedEntryVariant",
    "IntegrationProfileEntryPredefinedEntryVariantUnionMember0",
    "IntegrationProfileEntryPredefinedEntryVariantUnionMember1",
    "IntegrationProfileEntryIntegrationEntry",
    "IntegrationProfileEntryExactDataEntry",
    "IntegrationProfileEntryDocumentFingerprintEntry",
    "IntegrationProfileEntryWordListEntry",
    "IntegrationProfileSharedEntry",
    "IntegrationProfileSharedEntryCustomEntry",
    "IntegrationProfileSharedEntryCustomPromptTopicEntry",
    "IntegrationProfileSharedEntryPredefinedEntry",
    "IntegrationProfileSharedEntryPredefinedEntryConfidence",
    "IntegrationProfileSharedEntryPredefinedEntryVariant",
    "IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember0",
    "IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember1",
    "IntegrationProfileSharedEntryIntegrationEntry",
    "IntegrationProfileSharedEntryExactDataEntry",
    "IntegrationProfileSharedEntryDocumentFingerprintEntry",
    "IntegrationProfileSharedEntryWordListEntry",
]


class CustomProfileEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None


class CustomProfileEntryCustomPromptTopicEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime


class CustomProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class CustomProfileEntryPredefinedEntryVariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class CustomProfileEntryPredefinedEntryVariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


CustomProfileEntryPredefinedEntryVariant: TypeAlias = Union[
    CustomProfileEntryPredefinedEntryVariantUnionMember0, CustomProfileEntryPredefinedEntryVariantUnionMember1
]


class CustomProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: CustomProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[CustomProfileEntryPredefinedEntryVariant] = None
    """A Predefined AI prompt classification topic entry."""


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
    CustomProfileEntryCustomPromptTopicEntry,
    CustomProfileEntryPredefinedEntry,
    CustomProfileEntryIntegrationEntry,
    CustomProfileEntryExactDataEntry,
    CustomProfileEntryDocumentFingerprintEntry,
    CustomProfileEntryWordListEntry,
]


class CustomProfileSensitivityLevel(BaseModel):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: str

    level_id: str


class CustomProfileSharedEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None


class CustomProfileSharedEntryCustomPromptTopicEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime


class CustomProfileSharedEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class CustomProfileSharedEntryPredefinedEntryVariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class CustomProfileSharedEntryPredefinedEntryVariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


CustomProfileSharedEntryPredefinedEntryVariant: TypeAlias = Union[
    CustomProfileSharedEntryPredefinedEntryVariantUnionMember0,
    CustomProfileSharedEntryPredefinedEntryVariantUnionMember1,
]


class CustomProfileSharedEntryPredefinedEntry(BaseModel):
    id: str

    confidence: CustomProfileSharedEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[CustomProfileSharedEntryPredefinedEntryVariant] = None
    """A Predefined AI prompt classification topic entry."""


class CustomProfileSharedEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomProfileSharedEntryExactDataEntry(BaseModel):
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


class CustomProfileSharedEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class CustomProfileSharedEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomProfileSharedEntry: TypeAlias = Union[
    CustomProfileSharedEntryCustomEntry,
    CustomProfileSharedEntryCustomPromptTopicEntry,
    CustomProfileSharedEntryPredefinedEntry,
    CustomProfileSharedEntryIntegrationEntry,
    CustomProfileSharedEntryExactDataEntry,
    CustomProfileSharedEntryDocumentFingerprintEntry,
    CustomProfileSharedEntryWordListEntry,
]


class CustomProfile(BaseModel):
    id: str
    """The id of the profile (uuid)."""

    allowed_match_count: int
    """Related DLP policies will trigger when the match count exceeds the number set."""

    created_at: datetime
    """When the profile was created."""

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

    data_classes: Optional[List[str]] = None
    """Data classes associated with this profile."""

    data_tags: Optional[List[str]] = None
    """Data tags associated with this profile."""

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[CustomProfileEntry]] = None

    sensitivity_levels: Optional[List[CustomProfileSensitivityLevel]] = None
    """Sensitivity levels associated with this profile."""

    shared_entries: Optional[List[CustomProfileSharedEntry]] = None


class PredefinedProfileEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None


class PredefinedProfileEntryCustomPromptTopicEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime


class PredefinedProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class PredefinedProfileEntryPredefinedEntryVariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class PredefinedProfileEntryPredefinedEntryVariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


PredefinedProfileEntryPredefinedEntryVariant: TypeAlias = Union[
    PredefinedProfileEntryPredefinedEntryVariantUnionMember0, PredefinedProfileEntryPredefinedEntryVariantUnionMember1
]


class PredefinedProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[PredefinedProfileEntryPredefinedEntryVariant] = None
    """A Predefined AI prompt classification topic entry."""


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
    PredefinedProfileEntryCustomPromptTopicEntry,
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

    description: Optional[str] = None

    profile_id: Optional[str] = None


class IntegrationProfileEntryCustomPromptTopicEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime


class IntegrationProfileEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class IntegrationProfileEntryPredefinedEntryVariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class IntegrationProfileEntryPredefinedEntryVariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


IntegrationProfileEntryPredefinedEntryVariant: TypeAlias = Union[
    IntegrationProfileEntryPredefinedEntryVariantUnionMember0, IntegrationProfileEntryPredefinedEntryVariantUnionMember1
]


class IntegrationProfileEntryPredefinedEntry(BaseModel):
    id: str

    confidence: IntegrationProfileEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[IntegrationProfileEntryPredefinedEntryVariant] = None
    """A Predefined AI prompt classification topic entry."""


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
    IntegrationProfileEntryCustomPromptTopicEntry,
    IntegrationProfileEntryPredefinedEntry,
    IntegrationProfileEntryIntegrationEntry,
    IntegrationProfileEntryExactDataEntry,
    IntegrationProfileEntryDocumentFingerprintEntry,
    IntegrationProfileEntryWordListEntry,
]


class IntegrationProfileSharedEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None


class IntegrationProfileSharedEntryCustomPromptTopicEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime


class IntegrationProfileSharedEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


IntegrationProfileSharedEntryPredefinedEntryVariant: TypeAlias = Union[
    IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember0,
    IntegrationProfileSharedEntryPredefinedEntryVariantUnionMember1,
]


class IntegrationProfileSharedEntryPredefinedEntry(BaseModel):
    id: str

    confidence: IntegrationProfileSharedEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[IntegrationProfileSharedEntryPredefinedEntryVariant] = None
    """A Predefined AI prompt classification topic entry."""


class IntegrationProfileSharedEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationProfileSharedEntryExactDataEntry(BaseModel):
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


class IntegrationProfileSharedEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class IntegrationProfileSharedEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


IntegrationProfileSharedEntry: TypeAlias = Union[
    IntegrationProfileSharedEntryCustomEntry,
    IntegrationProfileSharedEntryCustomPromptTopicEntry,
    IntegrationProfileSharedEntryPredefinedEntry,
    IntegrationProfileSharedEntryIntegrationEntry,
    IntegrationProfileSharedEntryExactDataEntry,
    IntegrationProfileSharedEntryDocumentFingerprintEntry,
    IntegrationProfileSharedEntryWordListEntry,
]


class IntegrationProfile(BaseModel):
    id: str

    created_at: datetime

    entries: List[IntegrationProfileEntry]

    name: str

    shared_entries: List[IntegrationProfileSharedEntry]

    type: Literal["integration"]

    updated_at: datetime

    description: Optional[str] = None
    """The description of the profile."""


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
    CustomProfileSharedEntryCustomEntry.model_rebuild()
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
    IntegrationProfileSharedEntryCustomEntry.model_rebuild()
else:
    CustomProfile.update_forward_refs()  # type: ignore
    CustomProfileEntryCustomEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryPredefinedEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryPredefinedEntryConfidence.update_forward_refs()  # type: ignore
    CustomProfileEntryIntegrationEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryExactDataEntry.update_forward_refs()  # type: ignore
    CustomProfileEntryWordListEntry.update_forward_refs()  # type: ignore
    CustomProfileSharedEntryCustomEntry.update_forward_refs()  # type: ignore
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
    IntegrationProfileSharedEntryCustomEntry.update_forward_refs()  # type: ignore
