# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .dns_record import DNSRecord
from ..shared.response_info import ResponseInfo

__all__ = [
    "DNSDeleteResponse",
    "EmailAPIResponseCommon",
    "EmailDNSSettingsResponseCollection",
    "EmailDNSSettingsResponseCollectionResultInfo",
]


class EmailAPIResponseCommon(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""


class EmailDNSSettingsResponseCollectionResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""


class EmailDNSSettingsResponseCollection(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[List[DNSRecord]] = None

    result_info: Optional[EmailDNSSettingsResponseCollectionResultInfo] = None


DNSDeleteResponse: TypeAlias = Union[EmailAPIResponseCommon, EmailDNSSettingsResponseCollection]
