# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ..digital_experience_monitor import DigitalExperienceMonitor
from .http_tests.test_stat_over_time import TestStatOverTime

__all__ = [
    "HTTPDetails",
    "HTTPStats",
    "HTTPStatsAvailabilityPct",
    "HTTPStatsAvailabilityPctSlot",
    "HTTPStatsHTTPStatusCode",
    "HTTPStatsByColo",
    "HTTPStatsByColoAvailabilityPct",
    "HTTPStatsByColoAvailabilityPctSlot",
    "HTTPStatsByColoHTTPStatusCode",
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


class HTTPStatsHTTPStatusCode(BaseModel):
    status200: int

    status300: int

    status400: int

    status500: int

    timestamp: str


class HTTPStats(BaseModel):
    availability_pct: HTTPStatsAvailabilityPct = FieldInfo(alias="availabilityPct")

    dns_response_time_ms: TestStatOverTime = FieldInfo(alias="dnsResponseTimeMs")

    http_status_code: List[HTTPStatsHTTPStatusCode] = FieldInfo(alias="httpStatusCode")

    resource_fetch_time_ms: TestStatOverTime = FieldInfo(alias="resourceFetchTimeMs")

    server_response_time_ms: TestStatOverTime = FieldInfo(alias="serverResponseTimeMs")

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


class HTTPStatsByColoHTTPStatusCode(BaseModel):
    status200: int

    status300: int

    status400: int

    status500: int

    timestamp: str


class HTTPStatsByColo(BaseModel):
    availability_pct: HTTPStatsByColoAvailabilityPct = FieldInfo(alias="availabilityPct")

    colo: str

    dns_response_time_ms: TestStatOverTime = FieldInfo(alias="dnsResponseTimeMs")

    http_status_code: List[HTTPStatsByColoHTTPStatusCode] = FieldInfo(alias="httpStatusCode")

    resource_fetch_time_ms: TestStatOverTime = FieldInfo(alias="resourceFetchTimeMs")

    server_response_time_ms: TestStatOverTime = FieldInfo(alias="serverResponseTimeMs")

    unique_devices_total: int = FieldInfo(alias="uniqueDevicesTotal")
    """Count of unique devices that have run this test in the given time period"""


class HTTPDetails(BaseModel):
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

    target_policies: Optional[List[DigitalExperienceMonitor]] = None

    targeted: Optional[bool] = None
