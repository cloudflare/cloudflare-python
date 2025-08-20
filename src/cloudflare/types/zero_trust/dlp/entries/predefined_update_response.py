# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["PredefinedUpdateResponse", "Confidence", "Variant"]


class Confidence(BaseModel):
    ai_context_available: bool
    """Indicates whether this entry has AI remote service validation."""

    available: bool
    """
    Indicates whether this entry has any form of validation that is not an AI remote
    service.
    """


class Variant(BaseModel):
    topic_type: Literal["Intent", "Content"]

    type: Literal["PromptTopic"]


class PredefinedUpdateResponse(BaseModel):
    id: str

    confidence: Confidence

    enabled: bool

    name: str

    profile_id: Optional[str] = None

    variant: Optional[Variant] = None
