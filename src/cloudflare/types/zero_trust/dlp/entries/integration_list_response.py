# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel
from ..profiles.pattern import Pattern

__all__ = [
    "IntegrationListResponse",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember2Confidence",
    "UnionMember2Variant",
    "UnionMember2VariantUnionMember0",
    "UnionMember2VariantUnionMember1",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    pattern: Pattern

    type: Literal["custom"]

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember1(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["custom_prompt_topic"]

    updated_at: datetime

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember2Confidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class UnionMember2VariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class UnionMember2VariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


UnionMember2Variant: TypeAlias = Union[UnionMember2VariantUnionMember0, UnionMember2VariantUnionMember1]


class UnionMember2(BaseModel):
    id: str

    confidence: UnionMember2Confidence

    enabled: bool

    name: str

    type: Literal["predefined"]

    profile_id: Optional[str] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None

    variant: Optional[UnionMember2Variant] = None
    """A Predefined AI prompt classification topic entry."""


class UnionMember3(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["integration"]

    updated_at: datetime

    profile_id: Optional[str] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember4(BaseModel):
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

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember5(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["document_fingerprint"]

    updated_at: datetime

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


class UnionMember6(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    type: Literal["word_list"]

    updated_at: datetime

    word_list: object

    profile_id: Optional[str] = None

    upload_status: Optional[Literal["empty", "uploading", "pending", "processing", "failed", "complete"]] = None


IntegrationListResponse: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
