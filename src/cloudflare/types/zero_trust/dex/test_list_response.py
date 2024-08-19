# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .tests.tests import Tests
from ...shared.response_info import ResponseInfo

__all__ = ["TestListResponse", "ResultInfo"]


class ResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""


class TestListResponse(BaseModel):
    __test__ = False
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[Tests] = None

    result_info: Optional[ResultInfo] = None
