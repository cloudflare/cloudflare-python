# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel
from .digital_experience_monitoring_tests import DigitalExperienceMonitoringTests

__all__ = ["TestListResponse", "Error", "Message", "ResultInfo"]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


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
    errors: List[Error]

    messages: List[Message]

    result: DigitalExperienceMonitoringTests

    success: Literal[True]
    """Whether the API call was successful"""

    result_info: Optional[ResultInfo] = None
