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
    "CalculationSery",
    "CalculationSeryData",
    "CalculationSeryDataGroup",
    "Compare",
    "CompareAggregate",
    "CompareAggregateGroup",
    "CompareSery",
    "CompareSeryData",
    "CompareSeryDataGroup",
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
    "EventsSery",
    "EventsSeryData",
    "EventsSeryDataAggregates",
    "Invocation",
    "InvocationMetadata",
    "InvocationWorkers",
    "InvocationWorkersUnionMember0",
    "InvocationWorkersUnionMember0ScriptVersion",
    "InvocationWorkersUnionMember1",
    "InvocationWorkersUnionMember1DiagnosticsChannelEvent",
    "InvocationWorkersUnionMember1ScriptVersion",
    "Pattern",
    "PatternSery",
    "PatternSeryData",
    "PatternSeryDataGroup",
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
    value: Union[str, float, bool]

    is_regex: Optional[bool] = FieldInfo(alias="isRegex", default=None)

    match_case: Optional[bool] = FieldInfo(alias="matchCase", default=None)


class RunQueryParametersOrderBy(BaseModel):
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
    from_: float = FieldInfo(alias="from")
    """Set the start time for your query using UNIX time in milliseconds."""

    to: float
    """Set the end time for your query using UNIX time in milliseconds."""


class RunStatistics(BaseModel):
    bytes_read: float
    """Number of uncompressed bytes read from the table."""

    elapsed: float
    """Time in seconds for the query to run."""

    rows_read: float
    """Number of rows scanned from the table."""


class Run(BaseModel):
    id: str

    account_id: str = FieldInfo(alias="accountId")

    dry: bool

    environment_id: str = FieldInfo(alias="environmentId")

    granularity: float

    query: RunQuery

    status: Literal["STARTED", "COMPLETED"]

    timeframe: RunTimeframe

    user_id: str = FieldInfo(alias="userId")

    workspace_id: str = FieldInfo(alias="workspaceId")

    created: Optional[str] = None

    statistics: Optional[RunStatistics] = None

    updated: Optional[str] = None


class Statistics(BaseModel):
    bytes_read: float
    """Number of uncompressed bytes read from the table."""

    elapsed: float
    """Time in seconds for the query to run."""

    rows_read: float
    """Number of rows scanned from the table."""


class CalculationAggregateGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CalculationAggregate(BaseModel):
    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CalculationAggregateGroup]] = None


class CalculationSeryDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CalculationSeryData(BaseModel):
    count: float

    first_seen: str = FieldInfo(alias="firstSeen")

    interval: float

    last_seen: str = FieldInfo(alias="lastSeen")

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CalculationSeryDataGroup]] = None


class CalculationSery(BaseModel):
    data: List[CalculationSeryData]

    time: str


class Calculation(BaseModel):
    aggregates: List[CalculationAggregate]

    calculation: str

    series: List[CalculationSery]

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


class CompareSeryDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class CompareSeryData(BaseModel):
    count: float

    first_seen: str = FieldInfo(alias="firstSeen")

    interval: float

    last_seen: str = FieldInfo(alias="lastSeen")

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[CompareSeryDataGroup]] = None


class CompareSery(BaseModel):
    data: List[CompareSeryData]

    time: str


class Compare(BaseModel):
    aggregates: List[CompareAggregate]

    calculation: str

    series: List[CompareSery]

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

    outcome: str

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

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

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, Union[str, float, bool]]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[EventsEventWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


EventsEventWorkers: TypeAlias = Union[EventsEventWorkersUnionMember0, EventsEventWorkersUnionMember1]


class EventsEvent(BaseModel):
    metadata: EventsEventMetadata = FieldInfo(alias="$metadata")

    dataset: str

    source: Union[str, object]

    timestamp: int

    workers: Optional[EventsEventWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information enriches your logs so you can easily
    identify and debug issues.
    """


class EventsField(BaseModel):
    key: str

    type: str


class EventsSeryDataAggregates(BaseModel):
    api_count: int = FieldInfo(alias="_count")

    api_first_seen: str = FieldInfo(alias="_firstSeen")

    api_interval: int = FieldInfo(alias="_interval")

    api_last_seen: str = FieldInfo(alias="_lastSeen")

    bin: Optional[object] = None


class EventsSeryData(BaseModel):
    aggregates: EventsSeryDataAggregates

    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    errors: Optional[float] = None

    groups: Optional[Dict[str, Union[str, float, bool]]] = None
    """Groups in the query results."""


class EventsSery(BaseModel):
    data: List[EventsSeryData]

    time: str


class Events(BaseModel):
    count: Optional[float] = None

    events: Optional[List[EventsEvent]] = None

    fields: Optional[List[EventsField]] = None

    series: Optional[List[EventsSery]] = None


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

    outcome: str

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

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

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, Union[str, float, bool]]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[InvocationWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    truncated: Optional[bool] = None


InvocationWorkers: TypeAlias = Union[InvocationWorkersUnionMember0, InvocationWorkersUnionMember1]


class Invocation(BaseModel):
    metadata: InvocationMetadata = FieldInfo(alias="$metadata")

    dataset: str

    source: Union[str, object]

    timestamp: int

    workers: Optional[InvocationWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information enriches your logs so you can easily
    identify and debug issues.
    """


class PatternSeryDataGroup(BaseModel):
    key: str

    value: Union[str, float, bool]


class PatternSeryData(BaseModel):
    count: float

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    groups: Optional[List[PatternSeryDataGroup]] = None


class PatternSery(BaseModel):
    data: PatternSeryData

    time: str


class Pattern(BaseModel):
    count: float

    pattern: str

    series: List[PatternSery]

    service: str


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
