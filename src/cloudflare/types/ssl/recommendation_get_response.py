# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RecommendationGetResponse"]


class RecommendationGetResponse(BaseModel):
    id: Optional[str] = None
    """Identifier of a recommedation result."""

    modified_on: Optional[datetime] = None

    value: Optional[Literal["flexible", "full", "strict"]] = None
