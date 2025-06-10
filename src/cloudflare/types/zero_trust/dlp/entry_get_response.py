# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .profiles.pattern import Pattern

__all__ = [
    "EntryGetResponse",
    "CustomEntry",
    "PredefinedEntry",
    "PredefinedEntryConfidence",
    "IntegrationEntry",
    "ExactDataEntry",
    "DocumentTemplateEntry",
    "WordListEntry",
]


class CustomEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None


class PredefinedEntryConfidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class PredefinedEntry(BaseModel):
    id: str

    confidence: PredefinedEntryConfidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None


class IntegrationEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None


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


class DocumentTemplateEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_template"]

    updated_at: datetime


class WordListEntry(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None


EntryGetResponse: TypeAlias = Union[
    CustomEntry, PredefinedEntry, IntegrationEntry, ExactDataEntry, DocumentTemplateEntry, WordListEntry
]
