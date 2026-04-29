# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = ["PredefinedUpdateResponse", "Confidence", "Variant", "VariantUnionMember0", "VariantUnionMember1"]


class Confidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class VariantUnionMember0(BaseModel):
    """A Predefined AI prompt classification topic entry."""

    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]

    description: Optional[str] = None
    """
    A customer-facing explanation of what this predefined AI prompt topic
    represents.
    """


class VariantUnionMember1(BaseModel):
    """A general predefined entry."""

    type: Literal["General"]

    description: Optional[str] = None
    """A customer-facing explanation of what this predefined entry represents."""


Variant: TypeAlias = Union[VariantUnionMember0, VariantUnionMember1]


class PredefinedUpdateResponse(BaseModel):
    id: str

    confidence: Confidence

    enabled: bool

    name: str

    profile_id: Optional[str] = None

    variant: Optional[Variant] = None
    """A Predefined AI prompt classification topic entry."""
