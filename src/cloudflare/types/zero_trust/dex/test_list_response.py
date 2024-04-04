# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...shared import UnnamedSchemaRef3248f24329456e19dfa042fff9986f72
from ...._models import BaseModel
from .digital_experience_monitoring_tests import DigitalExperienceMonitoringTests

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
    errors: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    messages: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    result: DigitalExperienceMonitoringTests

    success: Literal[True]
    """Whether the API call was successful"""

    result_info: Optional[ResultInfo] = None
