# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from ..shared.response_info import ResponseInfo

__all__ = ["CustomNameserverGetResponse", "ResultInfo"]


class ResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""


class CustomNameserverGetResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    enabled: Optional[bool] = None
    """Whether zone uses account-level custom nameservers."""

    ns_set: Optional[float] = None
    """The number of the name server set to assign to the zone."""

    result_info: Optional[ResultInfo] = None
