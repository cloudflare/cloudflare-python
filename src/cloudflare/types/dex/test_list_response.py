# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "TestListResponse",
    "Error",
    "Message",
    "Result",
    "ResultOverviewMetrics",
    "ResultTest",
    "ResultTestHTTPResults",
    "ResultTestHTTPResultsResourceFetchTime",
    "ResultTestHTTPResultsResourceFetchTimeHistory",
    "ResultTestHTTPResultsResourceFetchTimeHistoryTimePeriod",
    "ResultTestHTTPResultsResourceFetchTimeOverTime",
    "ResultTestHTTPResultsResourceFetchTimeOverTimeTimePeriod",
    "ResultTestHTTPResultsResourceFetchTimeOverTimeValue",
    "ResultTestHTTPResultsByColo",
    "ResultTestHTTPResultsByColoResourceFetchTime",
    "ResultTestHTTPResultsByColoResourceFetchTimeHistory",
    "ResultTestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod",
    "ResultTestHTTPResultsByColoResourceFetchTimeOverTime",
    "ResultTestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod",
    "ResultTestHTTPResultsByColoResourceFetchTimeOverTimeValue",
    "ResultTestTracerouteResults",
    "ResultTestTracerouteResultsRoundTripTime",
    "ResultTestTracerouteResultsRoundTripTimeHistory",
    "ResultTestTracerouteResultsRoundTripTimeHistoryTimePeriod",
    "ResultTestTracerouteResultsRoundTripTimeOverTime",
    "ResultTestTracerouteResultsRoundTripTimeOverTimeTimePeriod",
    "ResultTestTracerouteResultsRoundTripTimeOverTimeValue",
    "ResultTestTracerouteResultsByColo",
    "ResultTestTracerouteResultsByColoRoundTripTime",
    "ResultTestTracerouteResultsByColoRoundTripTimeHistory",
    "ResultTestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod",
    "ResultTestTracerouteResultsByColoRoundTripTimeOverTime",
    "ResultTestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod",
    "ResultTestTracerouteResultsByColoRoundTripTimeOverTimeValue",
    "ResultInfo",
]


class Error(BaseModel):
    code: int

    message: str


class Message(BaseModel):
    code: int

    message: str


class ResultOverviewMetrics(BaseModel):
    tests_total: int = FieldInfo(alias="testsTotal")
    """number of tests."""

    avg_traceroute_availability_pct: Optional[float] = FieldInfo(alias="avgTracerouteAvailabilityPct", default=None)
    """percentage availability for all traceroutes results in response"""


class ResultTestHTTPResultsResourceFetchTimeHistoryTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestHTTPResultsResourceFetchTimeHistory(BaseModel):
    time_period: ResultTestHTTPResultsResourceFetchTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class ResultTestHTTPResultsResourceFetchTimeOverTimeTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestHTTPResultsResourceFetchTimeOverTimeValue(BaseModel):
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class ResultTestHTTPResultsResourceFetchTimeOverTime(BaseModel):
    time_period: ResultTestHTTPResultsResourceFetchTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[ResultTestHTTPResultsResourceFetchTimeOverTimeValue]


class ResultTestHTTPResultsResourceFetchTime(BaseModel):
    history: List[ResultTestHTTPResultsResourceFetchTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[ResultTestHTTPResultsResourceFetchTimeOverTime] = FieldInfo(alias="overTime", default=None)


class ResultTestHTTPResults(BaseModel):
    resource_fetch_time: ResultTestHTTPResultsResourceFetchTime = FieldInfo(alias="resourceFetchTime")


class ResultTestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestHTTPResultsByColoResourceFetchTimeHistory(BaseModel):
    time_period: ResultTestHTTPResultsByColoResourceFetchTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class ResultTestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestHTTPResultsByColoResourceFetchTimeOverTimeValue(BaseModel):
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class ResultTestHTTPResultsByColoResourceFetchTimeOverTime(BaseModel):
    time_period: ResultTestHTTPResultsByColoResourceFetchTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[ResultTestHTTPResultsByColoResourceFetchTimeOverTimeValue]


class ResultTestHTTPResultsByColoResourceFetchTime(BaseModel):
    history: List[ResultTestHTTPResultsByColoResourceFetchTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[ResultTestHTTPResultsByColoResourceFetchTimeOverTime] = FieldInfo(
        alias="overTime", default=None
    )


class ResultTestHTTPResultsByColo(BaseModel):
    colo: str
    """Cloudflare colo"""

    resource_fetch_time: ResultTestHTTPResultsByColoResourceFetchTime = FieldInfo(alias="resourceFetchTime")


class ResultTestTracerouteResultsRoundTripTimeHistoryTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestTracerouteResultsRoundTripTimeHistory(BaseModel):
    time_period: ResultTestTracerouteResultsRoundTripTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class ResultTestTracerouteResultsRoundTripTimeOverTimeTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestTracerouteResultsRoundTripTimeOverTimeValue(BaseModel):
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class ResultTestTracerouteResultsRoundTripTimeOverTime(BaseModel):
    time_period: ResultTestTracerouteResultsRoundTripTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[ResultTestTracerouteResultsRoundTripTimeOverTimeValue]


class ResultTestTracerouteResultsRoundTripTime(BaseModel):
    history: List[ResultTestTracerouteResultsRoundTripTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[ResultTestTracerouteResultsRoundTripTimeOverTime] = FieldInfo(alias="overTime", default=None)


class ResultTestTracerouteResults(BaseModel):
    round_trip_time: ResultTestTracerouteResultsRoundTripTime = FieldInfo(alias="roundTripTime")


class ResultTestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestTracerouteResultsByColoRoundTripTimeHistory(BaseModel):
    time_period: ResultTestTracerouteResultsByColoRoundTripTimeHistoryTimePeriod = FieldInfo(alias="timePeriod")

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    delta_pct: Optional[float] = FieldInfo(alias="deltaPct", default=None)


class ResultTestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod(BaseModel):
    units: Literal["hours", "days", "testRuns"]

    value: int


class ResultTestTracerouteResultsByColoRoundTripTimeOverTimeValue(BaseModel):
    avg_ms: int = FieldInfo(alias="avgMs")

    timestamp: str


class ResultTestTracerouteResultsByColoRoundTripTimeOverTime(BaseModel):
    time_period: ResultTestTracerouteResultsByColoRoundTripTimeOverTimeTimePeriod = FieldInfo(alias="timePeriod")

    values: List[ResultTestTracerouteResultsByColoRoundTripTimeOverTimeValue]


class ResultTestTracerouteResultsByColoRoundTripTime(BaseModel):
    history: List[ResultTestTracerouteResultsByColoRoundTripTimeHistory]

    avg_ms: Optional[int] = FieldInfo(alias="avgMs", default=None)

    over_time: Optional[ResultTestTracerouteResultsByColoRoundTripTimeOverTime] = FieldInfo(
        alias="overTime", default=None
    )


class ResultTestTracerouteResultsByColo(BaseModel):
    colo: str
    """Cloudflare colo"""

    round_trip_time: ResultTestTracerouteResultsByColoRoundTripTime = FieldInfo(alias="roundTripTime")


class ResultTest(BaseModel):
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

    http_results: Optional[ResultTestHTTPResults] = FieldInfo(alias="httpResults", default=None)

    http_results_by_colo: Optional[List[ResultTestHTTPResultsByColo]] = FieldInfo(
        alias="httpResultsByColo", default=None
    )

    method: Optional[str] = None
    """for HTTP, the method to use when running the test"""

    traceroute_results: Optional[ResultTestTracerouteResults] = FieldInfo(alias="tracerouteResults", default=None)

    traceroute_results_by_colo: Optional[List[ResultTestTracerouteResultsByColo]] = FieldInfo(
        alias="tracerouteResultsByColo", default=None
    )


class Result(BaseModel):
    overview_metrics: ResultOverviewMetrics = FieldInfo(alias="overviewMetrics")

    tests: List[ResultTest]
    """array of test results objects."""


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

    result: Result

    success: Literal[True]
    """Whether the API call was successful"""

    result_info: Optional[ResultInfo] = None
