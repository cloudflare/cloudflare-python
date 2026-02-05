# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from .profiles.pattern import Pattern
from .context_awareness import ContextAwareness

__all__ = [
    "ProfileGetResponse",
    "Custom",
    "CustomEntry",
    "CustomEntryCustomEntry",
    "CustomEntryPredefinedEntry",
    "CustomEntryPredefinedEntryConfidence",
    "CustomEntryPredefinedEntryVariant",
    "CustomEntryIntegrationEntry",
    "CustomEntryExactDataEntry",
    "CustomEntryDocumentFingerprintEntry",
    "CustomEntryWordListEntry",
    "Predefined",
    "PredefinedEntry",
    "PredefinedEntryCustomEntry",
    "PredefinedEntryPredefinedEntry",
    "PredefinedEntryPredefinedEntryConfidence",
    "PredefinedEntryPredefinedEntryVariant",
    "PredefinedEntryIntegrationEntry",
    "PredefinedEntryExactDataEntry",
    "PredefinedEntryDocumentFingerprintEntry",
    "PredefinedEntryWordListEntry",
    "Integration",
    "IntegrationEntry",
    "IntegrationEntryCustomEntry",
    "IntegrationEntryPredefinedEntry",
    "IntegrationEntryPredefinedEntryConfidence",
    "IntegrationEntryPredefinedEntryVariant",
    "IntegrationEntryIntegrationEntry",
    "IntegrationEntryExactDataEntry",
    "IntegrationEntryDocumentFingerprintEntry",
    "IntegrationEntryWordListEntry",
]


class CustomEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class CustomEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class CustomEntryPredefinedEntry(BaseModel):
    id: str

    confidence: CustomEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[CustomEntryPredefinedEntryVariant] = None


class CustomEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class CustomEntryExactDataEntry(BaseModel):
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


class CustomEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class CustomEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


CustomEntry: TypeAlias = Union[
    CustomEntryCustomEntry,
    CustomEntryPredefinedEntry,
    CustomEntryIntegrationEntry,
    CustomEntryExactDataEntry,
    CustomEntryDocumentFingerprintEntry,
    CustomEntryWordListEntry,
]


class Custom(BaseModel):
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

    description: Optional[str] = None
    """The description of the profile."""

    entries: Optional[List[CustomEntry]] = None


class PredefinedEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class PredefinedEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class PredefinedEntryPredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[PredefinedEntryPredefinedEntryVariant] = None


class PredefinedEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedEntryExactDataEntry(BaseModel):
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


class PredefinedEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class PredefinedEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


PredefinedEntry: TypeAlias = Union[
    PredefinedEntryCustomEntry,
    PredefinedEntryPredefinedEntry,
    PredefinedEntryIntegrationEntry,
    PredefinedEntryExactDataEntry,
    PredefinedEntryDocumentFingerprintEntry,
    PredefinedEntryWordListEntry,
]


class Predefined(BaseModel):
    id: str
    """The id of the predefined profile (uuid)."""

    allowed_match_count: int

    entries: List[PredefinedEntry]

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


class IntegrationEntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationEntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class IntegrationEntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class IntegrationEntryPredefinedEntry(BaseModel):
    id: str

    confidence: IntegrationEntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[IntegrationEntryPredefinedEntryVariant] = None


class IntegrationEntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class IntegrationEntryExactDataEntry(BaseModel):
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


class IntegrationEntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class IntegrationEntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


IntegrationEntry: TypeAlias = Union[
    IntegrationEntryCustomEntry,
    IntegrationEntryPredefinedEntry,
    IntegrationEntryIntegrationEntry,
    IntegrationEntryExactDataEntry,
    IntegrationEntryDocumentFingerprintEntry,
    IntegrationEntryWordListEntry,
]


class Integration(BaseModel):
    id: str

    created_at: datetime

    entries: List[IntegrationEntry]

    name: str

    type: Literal["integration"]

    updated_at: datetime

    description: Optional[str] = None
    """The description of the profile."""


ProfileGetResponse: TypeAlias = Annotated[Union[Custom, Predefined, Integration], PropertyInfo(discriminator="type")]
