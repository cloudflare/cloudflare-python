# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["LogListResponse"]


class LogListResponse(BaseModel):
    id: str

    cached: bool

    created_at: datetime

    duration: int

    model: str

    path: str

    provider: str

    success: bool

    tokens_in: Optional[int] = None

    tokens_out: Optional[int] = None

    cost: Optional[float] = None

    custom_cost: Optional[bool] = None

    metadata: Optional[str] = None

    ai_model_type: Optional[str] = FieldInfo(alias="model_type", default=None)

    request_content_type: Optional[str] = None

    request_type: Optional[str] = None

    response_content_type: Optional[str] = None

    status_code: Optional[int] = None

    step: Optional[int] = None
