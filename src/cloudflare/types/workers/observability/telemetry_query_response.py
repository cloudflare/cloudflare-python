# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TelemetryQueryResponse",
    "Run",
    "RunQuery",
    "RunQueryParameters",
    "RunQueryParametersCalculation",
    "RunQueryParametersFilter",
    "RunQueryParametersGroupBy",
    "RunQueryParametersHaving",
    "RunQueryParametersNeedle",
    "RunQueryParametersOrderBy",
    "RunTimeframe",
    "RunStatistics",
    "Statistics",
    "Calculation",
    "CalculationAggregate",
    "CalculationAggregateGroup",
    "CalculationSeries",
    "CalculationSeriesData",
    "CalculationSeriesDataGroup",
    "Compare",
    "CompareAggregate",
    "CompareAggregateGroup",
    "CompareSeries",
    "CompareSeriesData",
    "CompareSeriesDataGroup",
    "Events",
    "EventsEvent",
    "EventsEventMetadata",
    "EventsEventWorkers",
    "EventsEventWorkersUnionMember0",
    "EventsEventWorkersUnionMember0ScriptVersion",
    "EventsEventWorkersUnionMember1",
    "EventsEventWorkersUnionMember1DiagnosticsChannelEvent",
    "EventsEventWorkersUnionMember1ScriptVersion",
    "EventsField",
    "EventsSeries",
    "EventsSeriesData",
    "EventsSeriesDataAggregates",
    "Invocation",
    "InvocationMetadata",
    "InvocationWorkers",
    "InvocationWorkersUnionMember0",
    "InvocationWorkersUnionMember0ScriptVersion",
    "InvocationWorkersUnionMember1",
    "InvocationWorkersUnionMember1DiagnosticsChannelEvent",
    "InvocationWorkersUnionMember1ScriptVersion",
    "Pattern",
    "PatternSeries",
    "PatternSeriesData",
    "PatternSeriesDataGroup",
    "Trace",
]


class RunQueryParametersCalculation(BaseModel):
    operator: Literal[
        "uniq",
        "count",
        "max",
        "min",
        "sum",
        "avg",
        "median",
        "p001",
        "p01",
        "p05",
        "p10",
        "p25",
        "p75",
        "p90",
        "p95",
        "p99",
        "p999",
        "stddev",
        "variance",
        "COUNT_DISTINCT",
        "COUNT",
        "MAX",
        "MIN",
        "SUM",
        "AVG",
        "MEDIAN",
        "P001",
        "P01",
        "P05",
        "P10",
        "P25",
        "P75",
        "P90",
        "P95",
        "P99",
        "P999",
        "STDDEV",
        "VARIANCE",
    ]

    alias: Optional[str] = None

    key: Optional[str] = None

    key_type: Optional[Literal["string", "number", "boolean"]] = FieldInfo(alias="keyType", default=None)


class RunQueryParametersFilter(BaseModel):
    key: str

    operation: Literal[
        "includes",
        "not_includes",
        "starts_with",
        "regex",
        "exists",
        "is_null",
        "in",
        "not_in",
        "eq",
        "neq",
        "gt",
        "gte",
        "lt",
        "lte",
        "=",
        "!=",
        ">",
        ">=",
        "<",
        "<=",
        "INCLUDES",
        "DOES_NOT_INCLUDE",
        "MATCH_REGEX",
        "EXISTS",
        "DOES_NOT_EXIST",
        "IN",
        "NOT_IN",
        "STARTS_WITH",
    ]

    type: Literal["string", "number", "boolean"]

    value: Union[str, float, bool, None] = None


class RunQueryParametersGroupBy(BaseModel):
    type: Literal["string", "number", "boolean"]

    value: str


class RunQueryParametersHaving(BaseModel):
    key: str

    operation: Literal["eq", "neq", "gt", "gte", "lt", "lte"]

    value: float


class RunQueryParametersNeedle(BaseModel):
    """Define an expression to search using full-text search."""

    value: Union[str, float, bool]

    is_regex: Optional[bool] = FieldInfo(alias="isRegex", default=None)

    match_case: Optional[bool] = FieldInfo(alias="matchCase", default=None)


class RunQueryParametersOrderBy(BaseModel):
    """Configure the order of the results returned by the query."""

    value: str
    """Configure which Calculation to order the results by."""

    order: Optional[Literal["asc", "desc"]] = None
    """Set the order of the results"""


class RunQueryParameters(BaseModel):
    calculations: Optional[List[RunQueryParametersCalculation]] = None
    """Create Calculations to compute as part of the query."""

    datasets: Optional[List[str]] = None
    """Set the Datasets to query. Leave it empty to query all the datasets."""

    filter_combination: Optional[Literal["and", "or", "AND", "OR"]] = FieldInfo(alias="filterCombination", default=None)
    """Set a Flag to describe how to combine the filters on the query."""

    filters: Optional[List[RunQueryParametersFilter]] = None
    """Configure the Filters to apply to the query."""

    group_bys: Optional[List[RunQueryParametersGroupBy]] = FieldInfo(alias="groupBys", default=None)
    """Define how to group the results of the query."""

    havings: Optional[List[RunQueryParametersHaving]] = None
    """Configure the Having clauses that filter on calculations in the query result."""

    limit: Optional[int] = None
    """Set a limit on the number of results / records returned by the query"""

    needle: Optional[RunQueryParametersNeedle] = None
    """Define an expression to search using full-text search."""

    order_by: Optional[RunQueryParametersOrderBy] = FieldInfo(alias="orderBy", default=None)
    """Configure the order of the results returned by the query."""


class RunQuery(BaseModel):
    id: str
    """ID of the query"""

    created: str

    description: Optional[str] = None

    environment_id: str = FieldInfo(alias="environmentId")
    """ID of your environment"""

    generated: Optional[bool] = None
    """Flag for alerts automatically created"""

    name: Optional[str] = None
    """Query name"""

    parameters: RunQueryParameters

    updated: str

    user_id: str = FieldInfo(alias="userId")

    workspace_id: str = FieldInfo(alias="workspaceId")
    """ID of your workspace"""


class RunTimeframe(BaseModel):
    """Time range for the query execution"""

    from_: float = FieldInfo(alias="from")
    """Start timestamp for the query timeframe (Unix timestamp in milliseconds)"""

    to: float
    """End timestamp for the query timeframe (Unix timestamp in milliseconds)"""


class RunStatistics(BaseModel):
    bytes_read: float
    """Number of uncompressed bytes read from the table."""

    elapsed: float
    """Time in seconds for the query to run."""

    rows_read: float
    """Number of rows scanned from the table."""

    abr_level: Optional[float] = None
    """The level of Adaptive Bit Rate (ABR) sampling used for the query.

    If empty the ABR level is 1
    """


class Run(BaseModel):
    """A Workers Observability Query Object"""

    id: str

    account_id: str = FieldInfo(alias="accountId")

    dry: bool

    environment_id: str = FieldInfo(alias="environmentId")

    granularity: float

    query: RunQuery

    status: Literal["STARTED", "COMPLETED"]

    timeframe: RunTimeframe
    """Time range for the query execution"""

    user_id: str = FieldInfo(alias="userId")

    workspace_id: str = FieldInfo(alias="workspaceId")

    created: Optional[str] = None

    statistics: Optional[RunStatistics] = None

    updated: Optional[str] = None


class Statistics(BaseModel):
    """
    The statistics object contains information about query performance from the database, it does not include any network latency
    """

    bytes_read: float
    """Number of uncompressed bytes read from the table."""

    elapsed: float
    """Time in seconds for the query to run."""

    rows_read: float
    """Number of rows scanned from the table."""

    abr_level: Optional[float] = None
    """The level of Adaptive Bit Rate (ABR) sampling used for the query.

    If empty the ABR level is 1
    """


class CalculationAggregateGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CalculationAggregate(BaseModel):
    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CalculationAggregateGroup]] = None


class CalculationSeriesDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CalculationSeriesData(BaseModel):
    count: float

    first_seen: str = FieldInfo(alias="firstSeen")

    interval: float

    last_seen: str = FieldInfo(alias="lastSeen")

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CalculationSeriesDataGroup]] = None


class CalculationSeries(BaseModel):
    data: List[CalculationSeriesData]

    time: str


class Calculation(BaseModel):
    aggregates: List[CalculationAggregate]

    calculation: str

    series: List[CalculationSeries]

    alias: Optional[str] = None


class CompareAggregateGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CompareAggregate(BaseModel):
    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CompareAggregateGroup]] = None


class CompareSeriesDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CompareSeriesData(BaseModel):
    count: float

    first_seen: str = FieldInfo(alias="firstSeen")

    interval: float

    last_seen: str = FieldInfo(alias="lastSeen")

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CompareSeriesDataGroup]] = None


class CompareSeries(BaseModel):
    data: List[CompareSeriesData]

    time: str


class Compare(BaseModel):
    aggregates: List[CompareAggregate]

    calculation: str

    series: List[CompareSeries]

    alias: Optional[str] = None


class EventsEventMetadata(BaseModel):
    id: str

    account: Optional[str] = None

    cloud_service: Optional[str] = FieldInfo(alias="cloudService", default=None)

    cold_start: Optional[int] = FieldInfo(alias="coldStart", default=None)

    cost: Optional[int] = None

    duration: Optional[int] = None

    end_time: Optional[int] = FieldInfo(alias="endTime", default=None)

    error: Optional[str] = None

    error_template: Optional[str] = FieldInfo(alias="errorTemplate", default=None)

    fingerprint: Optional[str] = None

    level: Optional[str] = None

    message: Optional[str] = None

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)

    origin: Optional[str] = None

    parent_span_id: Optional[str] = FieldInfo(alias="parentSpanId", default=None)

    provider: Optional[str] = None

    region: Optional[str] = None

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)

    service: Optional[str] = None

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    span_name: Optional[str] = FieldInfo(alias="spanName", default=None)

    stack_id: Optional[str] = FieldInfo(alias="stackId", default=None)

    start_time: Optional[int] = FieldInfo(alias="startTime", default=None)

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    trace_duration: Optional[int] = FieldInfo(alias="traceDuration", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

    transaction_name: Optional[str] = FieldInfo(alias="transactionName", default=None)

    trigger: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


class EventsEventWorkersUnionMember0ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class EventsEventWorkersUnionMember0(BaseModel):
    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "unknown"
    ] = FieldInfo(alias="eventType")

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, Dict[str, Union[List[Union[str, float, bool]], str, float, bool]]]],
            ],
        ]
    ] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    outcome: Optional[str] = None

    script_version: Optional[EventsEventWorkersUnionMember0ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


class EventsEventWorkersUnionMember1DiagnosticsChannelEvent(BaseModel):
    channel: str

    message: str

    timestamp: float


class EventsEventWorkersUnionMember1ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class EventsEventWorkersUnionMember1(BaseModel):
    cpu_time_ms: float = FieldInfo(alias="cpuTimeMs")

    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "unknown"
    ] = FieldInfo(alias="eventType")

    outcome: str

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    wall_time_ms: float = FieldInfo(alias="wallTimeMs")

    diagnostics_channel_events: Optional[List[EventsEventWorkersUnionMember1DiagnosticsChannelEvent]] = FieldInfo(
        alias="diagnosticsChannelEvents", default=None
    )

    dispatch_namespace: Optional[str] = FieldInfo(alias="dispatchNamespace", default=None)

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, Union[str, float, bool]]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[EventsEventWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


EventsEventWorkers: TypeAlias = Union[EventsEventWorkersUnionMember0, EventsEventWorkersUnionMember1]


class EventsEvent(BaseModel):
    """The data structure of a telemetry event"""

    metadata: EventsEventMetadata = FieldInfo(alias="$metadata")

    dataset: str

    source: Union[str, object]

    timestamp: int

    containers: Optional[object] = FieldInfo(alias="$containers", default=None)
    """
    Cloudflare Containers event information enriches your logs so you can easily
    identify and debug issues.
    """

    workers: Optional[EventsEventWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information enriches your logs so you can easily
    identify and debug issues.
    """


class EventsField(BaseModel):
    key: str

    type: str


class EventsSeriesDataAggregates(BaseModel):
    api_count: int = FieldInfo(alias="_count")

    api_first_seen: str = FieldInfo(alias="_firstSeen")

    api_interval: int = FieldInfo(alias="_interval")

    api_last_seen: str = FieldInfo(alias="_lastSeen")

    bin: Optional[object] = None


class EventsSeriesData(BaseModel):
    aggregates: EventsSeriesDataAggregates

    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    errors: Optional[float] = None

    groups: Optional[Dict[str, Union[str, float, bool]]] = None
    """Groups in the query results."""


class EventsSeries(BaseModel):
    data: List[EventsSeriesData]

    time: str


class Events(BaseModel):
    count: Optional[float] = None

    events: Optional[List[EventsEvent]] = None

    fields: Optional[List[EventsField]] = None

    series: Optional[List[EventsSeries]] = None


class InvocationMetadata(BaseModel):
    id: str

    account: Optional[str] = None

    cloud_service: Optional[str] = FieldInfo(alias="cloudService", default=None)

    cold_start: Optional[int] = FieldInfo(alias="coldStart", default=None)

    cost: Optional[int] = None

    duration: Optional[int] = None

    end_time: Optional[int] = FieldInfo(alias="endTime", default=None)

    error: Optional[str] = None

    error_template: Optional[str] = FieldInfo(alias="errorTemplate", default=None)

    fingerprint: Optional[str] = None

    level: Optional[str] = None

    message: Optional[str] = None

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)

    origin: Optional[str] = None

    parent_span_id: Optional[str] = FieldInfo(alias="parentSpanId", default=None)

    provider: Optional[str] = None

    region: Optional[str] = None

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)

    service: Optional[str] = None

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    span_name: Optional[str] = FieldInfo(alias="spanName", default=None)

    stack_id: Optional[str] = FieldInfo(alias="stackId", default=None)

    start_time: Optional[int] = FieldInfo(alias="startTime", default=None)

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)

    trace_duration: Optional[int] = FieldInfo(alias="traceDuration", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

    transaction_name: Optional[str] = FieldInfo(alias="transactionName", default=None)

    trigger: Optional[str] = None

    type: Optional[str] = None

    url: Optional[str] = None


class InvocationWorkersUnionMember0ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class InvocationWorkersUnionMember0(BaseModel):
    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "unknown"
    ] = FieldInfo(alias="eventType")

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[
        Dict[
            str,
            Union[
                str,
                float,
                bool,
                Dict[str, Union[str, float, bool, Dict[str, Union[List[Union[str, float, bool]], str, float, bool]]]],
            ],
        ]
    ] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    outcome: Optional[str] = None

    script_version: Optional[InvocationWorkersUnionMember0ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


class InvocationWorkersUnionMember1DiagnosticsChannelEvent(BaseModel):
    channel: str

    message: str

    timestamp: float


class InvocationWorkersUnionMember1ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class InvocationWorkersUnionMember1(BaseModel):
    cpu_time_ms: float = FieldInfo(alias="cpuTimeMs")

    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "unknown"
    ] = FieldInfo(alias="eventType")

    outcome: str

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    wall_time_ms: float = FieldInfo(alias="wallTimeMs")

    diagnostics_channel_events: Optional[List[InvocationWorkersUnionMember1DiagnosticsChannelEvent]] = FieldInfo(
        alias="diagnosticsChannelEvents", default=None
    )

    dispatch_namespace: Optional[str] = FieldInfo(alias="dispatchNamespace", default=None)

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, Union[str, float, bool]]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[InvocationWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


InvocationWorkers: TypeAlias = Union[InvocationWorkersUnionMember0, InvocationWorkersUnionMember1]


class Invocation(BaseModel):
    """The data structure of a telemetry event"""

    metadata: InvocationMetadata = FieldInfo(alias="$metadata")

    dataset: str

    source: Union[str, object]

    timestamp: int

    containers: Optional[object] = FieldInfo(alias="$containers", default=None)
    """
    Cloudflare Containers event information enriches your logs so you can easily
    identify and debug issues.
    """

    workers: Optional[InvocationWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information enriches your logs so you can easily
    identify and debug issues.
    """


class PatternSeriesDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class PatternSeriesData(BaseModel):
    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[PatternSeriesDataGroup]] = None


class PatternSeries(BaseModel):
    data: PatternSeriesData

    time: str


class Pattern(BaseModel):
    count: float

    pattern: str

    series: List[PatternSeries]

    service: str


class Trace(BaseModel):
    root_span_name: str = FieldInfo(alias="rootSpanName")

    root_transaction_name: str = FieldInfo(alias="rootTransactionName")

    service: List[str]

    spans: float

    trace_duration_ms: float = FieldInfo(alias="traceDurationMs")

    trace_end_ms: float = FieldInfo(alias="traceEndMs")

    trace_id: str = FieldInfo(alias="traceId")

    trace_start_ms: float = FieldInfo(alias="traceStartMs")

    errors: Optional[List[str]] = None


class TelemetryQueryResponse(BaseModel):
    run: Run
    """A Workers Observability Query Object"""

    statistics: Statistics
    """
    The statistics object contains information about query performance from the
    database, it does not include any network latency
    """

    calculations: Optional[List[Calculation]] = None

    compare: Optional[List[Compare]] = None

    events: Optional[Events] = None

    invocations: Optional[Dict[str, List[Invocation]]] = None

    patterns: Optional[List[Pattern]] = None

    traces: Optional[List[Trace]] = None
