# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SpeedAPITestsListResponse", "Error", "Message", "ResultInfo"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class ResultInfo(BaseModel):
    count: Optional[int] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total_count: Optional[int] = None


class SpeedAPITestsListResponse(BaseModel):
    errors: List[Error]

    messages: List[Message]

    success: bool
    """Whether the API call was successful."""

    result_info: Optional[ResultInfo] = None
