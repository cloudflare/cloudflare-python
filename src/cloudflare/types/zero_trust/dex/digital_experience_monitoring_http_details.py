# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..unnamed_schema_ref_bf9e2abcf1b78a6cab8e6e29e2228a11 import UnnamedSchemaRefBf9e2abcf1b78a6cab8e6e29e2228a11

__all__ = [
    "DigitalExperienceMonitoringHTTPDetails",
    "HTTPStats",
    "HTTPStatsAvailabilityPct",
    "HTTPStatsAvailabilityPctSlot",
    "HTTPStatsDNSResponseTimeMs",
    "HTTPStatsDNSResponseTimeMsSlot",
    "HTTPStatsHTTPStatusCode",
    "HTTPStatsResourceFetchTimeMs",
    "HTTPStatsResourceFetchTimeMsSlot",
    "HTTPStatsServerResponseTimeMs",
    "HTTPStatsServerResponseTimeMsSlot",
    "HTTPStatsByColo",
    "HTTPStatsByColoAvailabilityPct",
    "HTTPStatsByColoAvailabilityPctSlot",
    "HTTPStatsByColoDNSResponseTimeMs",
    "HTTPStatsByColoDNSResponseTimeMsSlot",
    "HTTPStatsByColoHTTPStatusCode",
    "HTTPStatsByColoResourceFetchTimeMs",
    "HTTPStatsByColoResourceFetchTimeMsSlot",
    "HTTPStatsByColoServerResponseTimeMs",
    "HTTPStatsByColoServerResponseTimeMsSlot",
]


class HTTPStatsAvailabilityPctSlot(BaseModel):
    timestamp: str

    value: float


class HTTPStatsAvailabilityPct(BaseModel):
    slots: List[HTTPStatsAvailabilityPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class HTTPStatsDNSResponseTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsDNSResponseTimeMs(BaseModel):
    slots: List[HTTPStatsDNSResponseTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStatsHTTPStatusCode(BaseModel):
    status200: int

    status300: int

    status400: int

    status500: int

    timestamp: str


class HTTPStatsResourceFetchTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsResourceFetchTimeMs(BaseModel):
    slots: List[HTTPStatsResourceFetchTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStatsServerResponseTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsServerResponseTimeMs(BaseModel):
    slots: List[HTTPStatsServerResponseTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStats(BaseModel):
    availability_pct: HTTPStatsAvailabilityPct = FieldInfo(alias="availabilityPct")

    dns_response_time_ms: HTTPStatsDNSResponseTimeMs = FieldInfo(alias="dnsResponseTimeMs")

    http_status_code: List[HTTPStatsHTTPStatusCode] = FieldInfo(alias="httpStatusCode")

    resource_fetch_time_ms: HTTPStatsResourceFetchTimeMs = FieldInfo(alias="resourceFetchTimeMs")

    server_response_time_ms: HTTPStatsServerResponseTimeMs = FieldInfo(alias="serverResponseTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class HTTPStatsByColoAvailabilityPctSlot(BaseModel):
    timestamp: str

    value: float


class HTTPStatsByColoAvailabilityPct(BaseModel):
    slots: List[HTTPStatsByColoAvailabilityPctSlot]

    avg: Optional[float] = None
    """average observed in the time period"""

    max: Optional[float] = None
    """highest observed in the time period"""

    min: Optional[float] = None
    """lowest observed in the time period"""


class HTTPStatsByColoDNSResponseTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsByColoDNSResponseTimeMs(BaseModel):
    slots: List[HTTPStatsByColoDNSResponseTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStatsByColoHTTPStatusCode(BaseModel):
    status200: int

    status300: int

    status400: int

    status500: int

    timestamp: str


class HTTPStatsByColoResourceFetchTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsByColoResourceFetchTimeMs(BaseModel):
    slots: List[HTTPStatsByColoResourceFetchTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStatsByColoServerResponseTimeMsSlot(BaseModel):
    timestamp: str

    value: int


class HTTPStatsByColoServerResponseTimeMs(BaseModel):
    slots: List[HTTPStatsByColoServerResponseTimeMsSlot]

    avg: Optional[int] = None
    """average observed in the time period"""

    max: Optional[int] = None
    """highest observed in the time period"""

    min: Optional[int] = None
    """lowest observed in the time period"""


class HTTPStatsByColo(BaseModel):
    availability_pct: HTTPStatsByColoAvailabilityPct = FieldInfo(alias="availabilityPct")

    colo: str

    dns_response_time_ms: HTTPStatsByColoDNSResponseTimeMs = FieldInfo(alias="dnsResponseTimeMs")

    http_status_code: List[HTTPStatsByColoHTTPStatusCode] = FieldInfo(alias="httpStatusCode")

    resource_fetch_time_ms: HTTPStatsByColoResourceFetchTimeMs = FieldInfo(alias="resourceFetchTimeMs")

    server_response_time_ms: HTTPStatsByColoServerResponseTimeMs = FieldInfo(alias="serverResponseTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class DigitalExperienceMonitoringHTTPDetails(BaseModel):
    host: Optional[str] = None
    """The url of the HTTP synthetic application test"""

    http_stats: Optional[HTTPStats] = FieldInfo(alias="httpStats", default=None)

    http_stats_by_colo: Optional[List[HTTPStatsByColo]] = FieldInfo(alias="httpStatsByColo", default=None)

    interval: Optional[str] = None
    """The interval at which the HTTP synthetic application test is set to run."""

    kind: Optional[Literal["http"]] = None

    method: Optional[str] = None
    """The HTTP method to use when running the test"""

    name: Optional[str] = None
    """The name of the HTTP synthetic application test"""

    target_policies: Optional[List[UnnamedSchemaRefBf9e2abcf1b78a6cab8e6e29e2228a11]] = None

    targeted: Optional[bool] = None
