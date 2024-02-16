# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["RecommendationListResponse"]


class RecommendationListResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of a recommedation result."""

    modified_on: Optional[datetime] = None

    value: Optional[Literal["flexible", "full", "strict"]] = None
