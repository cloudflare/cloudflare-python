# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .pattern import Pattern
from ....._models import BaseModel

__all__ = [
    "PredefinedUpdateResponse",
    "Entry",
    "EntryCustomEntry",
    "EntryPredefinedEntry",
    "EntryPredefinedEntryConfidence",
    "EntryPredefinedEntryVariant",
    "EntryIntegrationEntry",
    "EntryExactDataEntry",
    "EntryDocumentFingerprintEntry",
    "EntryWordListEntry",
]


class EntryCustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class EntryPredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class EntryPredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class EntryPredefinedEntry(BaseModel):
    id: str

    confidence: EntryPredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    variant: Optional[EntryPredefinedEntryVariant] = None


class EntryIntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


class EntryExactDataEntry(BaseModel):
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


class EntryDocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime


class EntryWordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


Entry: TypeAlias = Union[
    EntryCustomEntry,
    EntryPredefinedEntry,
    EntryIntegrationEntry,
    EntryExactDataEntry,
    EntryDocumentFingerprintEntry,
    EntryWordListEntry,
]


class PredefinedUpdateResponse(BaseModel):
    id: str
    """The id of the predefined profile (uuid)."""

    allowed_match_count: int

    confidence_threshold: Optional[str] = None

    enabled_entries: List[str]

    entries: List[Entry]

    name: str
    """The name of the predefined profile."""

    ai_context_enabled: Optional[bool] = None

    ocr_enabled: Optional[bool] = None

    open_access: Optional[bool] = None
    """Whether this profile can be accessed by anyone."""
