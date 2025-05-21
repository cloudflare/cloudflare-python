# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel
from .dns_record import DNSRecord

__all__ = [
    "DNSGetResponse",
    "EmailEmailRoutingDNSQueryResponse",
    "EmailEmailRoutingDNSQueryResponseError",
    "EmailEmailRoutingDNSQueryResponseErrorSource",
    "EmailEmailRoutingDNSQueryResponseMessage",
    "EmailEmailRoutingDNSQueryResponseMessageSource",
    "EmailEmailRoutingDNSQueryResponseResult",
    "EmailEmailRoutingDNSQueryResponseResultError",
    "EmailEmailRoutingDNSQueryResponseResultInfo",
    "EmailDNSSettingsResponseCollection",
    "EmailDNSSettingsResponseCollectionError",
    "EmailDNSSettingsResponseCollectionErrorSource",
    "EmailDNSSettingsResponseCollectionMessage",
    "EmailDNSSettingsResponseCollectionMessageSource",
    "EmailDNSSettingsResponseCollectionResultInfo",
]


class EmailEmailRoutingDNSQueryResponseErrorSource(BaseModel):
    pointer: Optional[str] = None


class EmailEmailRoutingDNSQueryResponseError(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[EmailEmailRoutingDNSQueryResponseErrorSource] = None


class EmailEmailRoutingDNSQueryResponseMessageSource(BaseModel):
    pointer: Optional[str] = None


class EmailEmailRoutingDNSQueryResponseMessage(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[EmailEmailRoutingDNSQueryResponseMessageSource] = None


class EmailEmailRoutingDNSQueryResponseResultError(BaseModel):
    code: Optional[str] = None

    missing: Optional[DNSRecord] = None
    """List of records needed to enable an Email Routing zone."""


class EmailEmailRoutingDNSQueryResponseResult(BaseModel):
    errors: Optional[List[EmailEmailRoutingDNSQueryResponseResultError]] = None

    record: Optional[List[DNSRecord]] = None


class EmailEmailRoutingDNSQueryResponseResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    total_count: Optional[float] = None
    """Total results available without any search parameters."""


class EmailEmailRoutingDNSQueryResponse(BaseModel):
    errors: List[EmailEmailRoutingDNSQueryResponseError]

    messages: List[EmailEmailRoutingDNSQueryResponseMessage]

    success: Literal[True]
    """Whether the API call was successful."""

    result: Optional[EmailEmailRoutingDNSQueryResponseResult] = None

    result_info: Optional[EmailEmailRoutingDNSQueryResponseResultInfo] = None


class EmailDNSSettingsResponseCollectionErrorSource(BaseModel):
    pointer: Optional[str] = None


class EmailDNSSettingsResponseCollectionError(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[EmailDNSSettingsResponseCollectionErrorSource] = None


class EmailDNSSettingsResponseCollectionMessageSource(BaseModel):
    pointer: Optional[str] = None


class EmailDNSSettingsResponseCollectionMessage(BaseModel):
    code: int

    message: str

    documentation_url: Optional[str] = None

    source: Optional[EmailDNSSettingsResponseCollectionMessageSource] = None


class EmailDNSSettingsResponseCollectionResultInfo(BaseModel):
    count: Optional[float] = None
    """Total number of results for the requested service."""

    page: Optional[float] = None
    """Current page within paginated list of results."""

    per_page: Optional[float] = None
    """Number of results per page of results."""

    total_count: Optional[float] = None
    """Total results available without any search parameters."""


class EmailDNSSettingsResponseCollection(BaseModel):
    errors: List[EmailDNSSettingsResponseCollectionError]

    messages: List[EmailDNSSettingsResponseCollectionMessage]

    success: Literal[True]
    """Whether the API call was successful."""

    result: Optional[List[DNSRecord]] = None

    result_info: Optional[EmailDNSSettingsResponseCollectionResultInfo] = None


DNSGetResponse: TypeAlias = Union[EmailEmailRoutingDNSQueryResponse, EmailDNSSettingsResponseCollection]
