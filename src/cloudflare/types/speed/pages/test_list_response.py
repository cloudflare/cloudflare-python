# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from ...shared.response_info import ResponseInfo

__all__ = ["TestListResponse", "ResultInfo"]


class ResultInfo(BaseModel):
    count: Optional[int] = None

    page: Optional[int] = None

    per_page: Optional[int] = None

    total_count: Optional[int] = None


class TestListResponse(BaseModel):
    __test__ = False
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: bool
    """Whether the API call was successful."""

    result_info: Optional[ResultInfo] = None
