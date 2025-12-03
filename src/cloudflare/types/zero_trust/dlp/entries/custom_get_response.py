# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from ..profiles.pattern import Pattern

__all__ = [
    "CustomGetResponse",
    "CustomEntry",
    "CustomEntryProfile",
    "PredefinedEntry",
    "PredefinedEntryConfidence",
    "PredefinedEntryProfile",
    "PredefinedEntryVariant",
    "IntegrationEntry",
    "IntegrationEntryProfile",
    "ExactDataEntry",
    "ExactDataEntryProfile",
    "DocumentFingerprintEntry",
    "DocumentFingerprintEntryProfile",
    "WordListEntry",
    "WordListEntryProfile",
]


class CustomEntryProfile(BaseModel):
    id: str

    name: str


class CustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None

    profiles: Optional[List[CustomEntryProfile]] = None


class PredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class PredefinedEntryProfile(BaseModel):
    id: str

    name: str


class PredefinedEntryVariant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class PredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    profiles: Optional[List[PredefinedEntryProfile]] = None

    variant: Optional[PredefinedEntryVariant] = None


class IntegrationEntryProfile(BaseModel):
    id: str

    name: str


class IntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None

    profiles: Optional[List[IntegrationEntryProfile]] = None


class ExactDataEntryProfile(BaseModel):
    id: str

    name: str


class ExactDataEntry(BaseModel):
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

    profiles: Optional[List[ExactDataEntryProfile]] = None


class DocumentFingerprintEntryProfile(BaseModel):
    id: str

    name: str


class DocumentFingerprintEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime

    profiles: Optional[List[DocumentFingerprintEntryProfile]] = None


class WordListEntryProfile(BaseModel):
    id: str

    name: str


class WordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None

    profiles: Optional[List[WordListEntryProfile]] = None


CustomGetResponse: TypeAlias = Union[
    CustomEntry, PredefinedEntry, IntegrationEntry, ExactDataEntry, DocumentFingerprintEntry, WordListEntry
]
