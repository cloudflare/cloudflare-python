# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["PercentileListResponse", "DNSResponseTimeMs", "ResourceFetchTimeMs", "ServerResponseTimeMs"]


class DNSResponseTimeMs(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class ResourceFetchTimeMs(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class ServerResponseTimeMs(BaseModel):
    p50: Optional[float] = None
    """p50 observed in the time period"""

    p90: Optional[float] = None
    """p90 observed in the time period"""

    p95: Optional[float] = None
    """p95 observed in the time period"""

    p99: Optional[float] = None
    """p99 observed in the time period"""


class PercentileListResponse(BaseModel):
    dns_response_time_ms: Optional[DNSResponseTimeMs] = FieldInfo(alias="dnsResponseTimeMs", default=None)

    resource_fetch_time_ms: Optional[ResourceFetchTimeMs] = FieldInfo(alias="resourceFetchTimeMs", default=None)

    server_response_time_ms: Optional[ServerResponseTimeMs] = FieldInfo(alias="serverResponseTimeMs", default=None)
