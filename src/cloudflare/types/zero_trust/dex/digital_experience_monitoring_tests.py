# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "DigitalExperienceMonitoringTests",
    "OverviewMetrics",
    "Test",
    "TestHTTPResults",
    "TestHTTPResultsResourceFetchTime",
    "TestHTTPResultsResourceFetchTimeHistory",
    "TestHTTPResultsResourceFetchTimeHistoryTimePeriod",
    "TestHTTPResultsResourceFetchTimeOverTime",
    "TestHTTPResultsResourceFetchTimeOverTimeTimePeriod",
    "TestHTTPResultsResourceFetchTimeOverTimeValue",
    "TestHTTPResultsByColo",
    "TestHTTPResultsByColoResourceFetchTime",
    "TestHTTPResultsByColoResourceFetchTimeHistory",
    "TestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod",
    "TestHTTPResultsByColoResourceFetchTimeOverTime",
    "TestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod",
    "TestHTTPResultsByColoResourceFetchTimeOverTimeValue",
    "TestTracerouteResults",
    "TestTracerouteResultsRoundTripTime",
    "TestTracerouteResultsRoundTripTimeHistory",
    "TestTracerouteResultsRoundTripTimeHistoryTimePeriod",
    "TestTracerouteResultsRoundTripTimeOverTime",
    "TestTracerouteResultsRoundTripTimeOverTimeTimePeriod",
    "TestTracerouteResultsRoundTripTimeOverTimeValue",
    "TestTracerouteResultsByColo",
    "TestTracerouteResultsByColoRoundTripTime",
    "TestTracerouteResultsByColoRoundTripTimeHistory",
    "TestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod",
    "TestTracerouteResultsByColoRoundTripTimeOverTime",
    "TestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod",
    "TestTracerouteResultsByColoRoundTripTimeOverTimeValue",
]


class OverviewMetrics(BaseModel):
    tests_total: int = FieldInfo(alias="testsTotal")
    """number of tests."""

    avg_traceroute_availability_pct: Optional[float] = FieldInfo(alias="avgTracerouteAvailabilityPct", default=None)
    """percentage availability for all traceroutes results in response"""


class TestHTTPResultsResourceFetchTimeHistoryTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestHTTPResultsResourceFetchTimeHistory(BaseModel):
    __test__ = False
    time_period: TestHTTPResultsResourceFetchTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class TestHTTPResultsResourceFetchTimeOverTimeTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestHTTPResultsResourceFetchTimeOverTimeValue(BaseModel):
    __test__ = False
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class TestHTTPResultsResourceFetchTimeOverTime(BaseModel):
    __test__ = False
    time_period: TestHTTPResultsResourceFetchTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[TestHTTPResultsResourceFetchTimeOverTimeValue]


class TestHTTPResultsResourceFetchTime(BaseModel):
    __test__ = False
    history: List[TestHTTPResultsResourceFetchTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[TestHTTPResultsResourceFetchTimeOverTime] = FieldInfo(alias="overTime", default=None)


class TestHTTPResults(BaseModel):
    __test__ = False
    resource_fetch_time: TestHTTPResultsResourceFetchTime = FieldInfo(alias="resourceFetchTime")


class TestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestHTTPResultsByColoResourceFetchTimeHistory(BaseModel):
    __test__ = False
    time_period: TestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class TestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestHTTPResultsByColoResourceFetchTimeOverTimeValue(BaseModel):
    __test__ = False
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class TestHTTPResultsByColoResourceFetchTimeOverTime(BaseModel):
    __test__ = False
    time_period: TestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[TestHTTPResultsByColoResourceFetchTimeOverTimeValue]


class TestHTTPResultsByColoResourceFetchTime(BaseModel):
    __test__ = False
    history: List[TestHTTPResultsByColoResourceFetchTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[TestHTTPResultsByColoResourceFetchTimeOverTime] = FieldInfo(alias="overTime", default=None)


class TestHTTPResultsByColo(BaseModel):
    __test__ = False
    colo: str
    """Cloudflare colo"""

    resource_fetch_time: TestHTTPResultsByColoResourceFetchTime = FieldInfo(alias="resourceFetchTime")


class TestTracerouteResultsRoundTripTimeHistoryTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestTracerouteResultsRoundTripTimeHistory(BaseModel):
    __test__ = False
    time_period: TestTracerouteResultsRoundTripTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class TestTracerouteResultsRoundTripTimeOverTimeTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestTracerouteResultsRoundTripTimeOverTimeValue(BaseModel):
    __test__ = False
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class TestTracerouteResultsRoundTripTimeOverTime(BaseModel):
    __test__ = False
    time_period: TestTracerouteResultsRoundTripTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[TestTracerouteResultsRoundTripTimeOverTimeValue]


class TestTracerouteResultsRoundTripTime(BaseModel):
    __test__ = False
    history: List[TestTracerouteResultsRoundTripTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[TestTracerouteResultsRoundTripTimeOverTime] = FieldInfo(alias="overTime", default=None)


class TestTracerouteResults(BaseModel):
    __test__ = False
    round_trip_time: TestTracerouteResultsRoundTripTime = FieldInfo(alias="roundTripTime")


class TestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestTracerouteResultsByColoRoundTripTimeHistory(BaseModel):
    __test__ = False
    time_period: TestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class TestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod(BaseModel):
    __test__ = False
    units: Literal["hours", "days", "testRuns"]

    value: int


class TestTracerouteResultsByColoRoundTripTimeOverTimeValue(BaseModel):
    __test__ = False
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class TestTracerouteResultsByColoRoundTripTimeOverTime(BaseModel):
    __test__ = False
    time_period: TestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[TestTracerouteResultsByColoRoundTripTimeOverTimeValue]


class TestTracerouteResultsByColoRoundTripTime(BaseModel):
    __test__ = False
    history: List[TestTracerouteResultsByColoRoundTripTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[TestTracerouteResultsByColoRoundTripTimeOverTime] = FieldInfo(alias="overTime", default=None)


class TestTracerouteResultsByColo(BaseModel):
    __test__ = False
    colo: str
    """Cloudflare colo"""

    round_trip_time: TestTracerouteResultsByColoRoundTripTime = FieldInfo(alias="roundTripTime")


class Test(BaseModel):
    __test__ = False
    id: str
    """API Resource UUID tag."""

    created: str
    """date the test was created."""

    description: str
    """the test description defined during configuration"""

    enabled: bool
    """if true, then the test will run on targeted devices.

    Else, the test will not run.
    """

    host: str

    interval: str
    """The interval at which the synthetic application test is set to run."""

    kind: Literal["http", "traceroute"]
    """test type, http or traceroute"""

    name: str
    """name given to this test"""

    updated: str

    http_results: Optional[TestHTTPResults] = FieldInfo(alias="httpResults", default=None)

    http_results_by_colo: Optional[List[TestHTTPResultsByColo]] = FieldInfo(alias="httpResultsByColo", default=None)

    method: Optional[str] = None
    """for HTTP, the method to use when running the test"""

    traceroute_results: Optional[TestTracerouteResults] = FieldInfo(alias="tracerouteResults", default=None)

    traceroute_results_by_colo: Optional[List[TestTracerouteResultsByColo]] = FieldInfo(
        alias="tracerouteResultsByColo", default=None
    )


class DigitalExperienceMonitoringTests(BaseModel):
    overview_metrics: OverviewMetrics = FieldInfo(alias="overviewMetrics")

    tests: List[Test]
    """array of test results objects."""
