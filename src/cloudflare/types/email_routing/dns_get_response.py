# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .dns_record import DNSRecord

__all__ = [
    "DNSGetResponse",
    "EmailEmailRoutingDNSQueryResponse",
    "EmailEmailRoutingDNSQueryResponseResult",
    "EmailEmailRoutingDNSQueryResponseResultError",
    "EmailEmailRoutingDNSQueryResponseResultInfo",
    "EmailDNSSettingsResponseCollection",
    "EmailDNSSettingsResponseCollectionResultInfo",
]


class EmailEmailRoutingDNSQueryResponseResultError(BaseModel):
    code: Optional[str] = None

    missing: Optional[DNSRecord] = None
    """List of records needed to enable an Email Routing zone."""


class EmailEmailRoutingDNSQueryResponseResult(BaseModel):
    errors: Optional[List[EmailEmailRoutingDNSQueryResponseResultError]] = None

    record: Optional[List[DNSRecord]] = None


class EmailEmailRoutingDNSQueryResponseResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service"""

    page: Optional[float] = None
    """Current page within paginated list of results"""

    per_page: Optional[float] = None
    """Number of results per page of results"""

    total_count: Optional[float] = None
    """Total results available without any search parameters"""


class EmailEmailRoutingDNSQueryResponse(BaseModel):
    errors: List[object]

    messages: List[object]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[EmailEmailRoutingDNSQueryResponseResult] = None

    result_info: Optional[EmailEmailRoutingDNSQueryResponseResultInfo] = None


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
    errors: List[object]

    messages: List[object]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[List[DNSRecord]] = None

    result_info: Optional[EmailDNSSettingsResponseCollectionResultInfo] = None


DNSGetResponse: TypeAlias = Union[EmailEmailRoutingDNSQueryResponse, EmailDNSSettingsResponseCollection]
