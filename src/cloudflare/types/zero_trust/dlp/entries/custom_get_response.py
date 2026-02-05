# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from ..profiles.pattern import Pattern

__all__ = [
    "CustomGetResponse",
    "UnionMember0",
    "UnionMember0Profile",
    "UnionMember1",
    "UnionMember1Confidence",
    "UnionMember1Profile",
    "UnionMember1Variant",
    "UnionMember2",
    "UnionMember2Profile",
    "UnionMember3",
    "UnionMember3Profile",
    "UnionMember4",
    "UnionMember4Profile",
    "UnionMember5",
    "UnionMember5Profile",
]


class UnionMember0Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember0(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    profile_id: Optional[str] = None

    profiles: Optional[List[UnionMember0Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember1Confidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class UnionMember1Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember1Variant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None


class UnionMember1(BaseModel):
    id: str

    confidence: UnionMember1Confidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    profiles: Optional[List[UnionMember1Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None

    variant: Optional[UnionMember1Variant] = None


class UnionMember2Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember2(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None

    profiles: Optional[List[UnionMember2Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember3Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember3(BaseModel):
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

    profiles: Optional[List[UnionMember3Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember4Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember4(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime

    profiles: Optional[List[UnionMember4Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember5Profile(BaseModel):
    """Computed entry field for a profile that an entry is shared into."""

    id: str

    name: str


class UnionMember5(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None

    profiles: Optional[List[UnionMember5Profile]] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


CustomGetResponse: TypeAlias = Union[UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5]
