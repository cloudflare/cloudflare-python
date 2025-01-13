# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel
from .profiles.pattern import Pattern

__all__ = [
    "EntryUpdateResponse",
    "CustomEntry",
    "PredefinedEntry",
    "PredefinedEntryConfidence",
    "IntegrationEntry",
    "ExactDataEntry",
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
    available: bool
    """
    Indicates whether this entry can be made more or less sensitive by setting a
    confidence threshold. Profiles that use an entry with `available` set to true
    can use confidence thresholds
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

    created_at: datetime

    enabled: bool

    name: str

    secret: bool

    type: Literal["exact_data"]

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


EntryUpdateResponse: TypeAlias = Union[CustomEntry, PredefinedEntry, IntegrationEntry, ExactDataEntry, WordListEntry]
