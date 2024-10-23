# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["VersionListResponse", "Error", "Message", "Result", "ResultInfo"]


class Error(BaseModel):
    code: float

    message: str


class Message(BaseModel):
    code: float

    message: str


class Result(BaseModel):
    id: str

    class_name: str

    created_on: datetime

    modified_on: datetime

    workflow_id: str


class ResultInfo(BaseModel):
    count: float

    page: float

    per_page: float

    total_count: float


class VersionListResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    result: Result

    success: Literal[True]

    result_info: Optional[ResultInfo] = None
