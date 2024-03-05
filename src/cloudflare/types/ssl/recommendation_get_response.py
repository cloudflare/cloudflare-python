# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RecommendationGetResponse"]


class RecommendationGetResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of a recommedation result."""

    modified_on: Optional[datetime] = None

    value: Optional[Literal["flexible", "full", "strict"]] = None
