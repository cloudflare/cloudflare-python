# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["LogGetResponse", "LogGetResponseItem"]


class LogGetResponseItem(BaseModel):
    id: str

    cached: bool

    created_at: datetime

    duration: int

    model: str

    path: str

    provider: str

    request: str

    response: str

    success: bool

    tokens_in: int

    tokens_out: int

    metadata: Optional[str] = None

    request_type: Optional[str] = None

    status_code: Optional[int] = None

    step: Optional[int] = None


LogGetResponse = List[LogGetResponseItem]
