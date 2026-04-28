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
    "RunQueryParametersFilterUnionMember0",
    "RunQueryParametersFilterWorkersObservabilityFilterLeaf",
    "RunQueryParametersGroupBy",
    "RunQueryParametersHaving",
    "RunQueryParametersNeedle",
    "RunQueryParametersNeedleValue",
    "RunQueryParametersOrderBy",
    "RunTimeframe",
    "RunStatistics",
    "Statistics",
    "Agent",
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


class RunQueryParametersFilterUnionMember0(BaseModel):
    filter_combination: Literal["and", "or", "AND", "OR"] = FieldInfo(alias="filterCombination")

    filters: List[object]

    kind: Literal["group"]


class RunQueryParametersFilterWorkersObservabilityFilterLeaf(BaseModel):
    """A filter condition applied to query results.

    Use the keys and values endpoints to discover available fields and their values before constructing filters.
    """

    key: str
    """Filter field name.

    Use verified keys from previous query results or the keys endpoint. Common keys
    include $metadata.service, $metadata.origin, $metadata.trigger,
    $metadata.message, and $metadata.error.
    """

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
    """Comparison operator.

    String operators: includes, not_includes, starts_with, regex. Existence: exists,
    is_null. Set membership: in, not_in (comma-separated values). Numeric: eq, neq,
    gt, gte, lt, lte.
    """

    type: Literal["string", "number", "boolean"]
    """Data type of the filter field.

    Must match the actual type of the key being filtered.
    """

    kind: Optional[Literal["filter"]] = None
    """Discriminator for leaf filter nodes.

    Always 'filter' when present; may be omitted.
    """

    value: Union[str, float, bool, None] = None
    """Comparison value.

    Must match actual values in your data — verify with the values endpoint. Ensure
    the value type (string/number/boolean) matches the field type. String
    comparisons are case-sensitive. Regex uses RE2 syntax (no
    lookaheads/lookbehinds).
    """


RunQueryParametersFilter: TypeAlias = Union[
    RunQueryParametersFilterUnionMember0, RunQueryParametersFilterWorkersObservabilityFilterLeaf
]


class RunQueryParametersGroupBy(BaseModel):
    type: Literal["string", "number", "boolean"]

    value: str


class RunQueryParametersHaving(BaseModel):
    key: str

    operation: Literal["eq", "neq", "gt", "gte", "lt", "lte"]

    value: float


class RunQueryParametersNeedleValue(BaseModel):
    model_config = {"arbitrary_types_allowed": True}


class RunQueryParametersNeedle(BaseModel):
    """Define an expression to search using full-text search."""

    value: RunQueryParametersNeedleValue

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
    """Configure the Filters to apply to the query.

    Supports nested groups via kind: 'group'.
    """

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
    """
    A saved query definition with its parameters, metadata, and ownership information.
    """

    id: str

    adhoc: bool
    """If the query wasn't explcitly saved"""

    created: str

    created_by: str = FieldInfo(alias="createdBy")

    description: Optional[str] = None

    name: str
    """Query name"""

    parameters: RunQueryParameters

    updated: str

    updated_by: str = FieldInfo(alias="updatedBy")


class RunTimeframe(BaseModel):
    """Time range for the query execution"""

    from_: float = FieldInfo(alias="from")
    """Start timestamp for the query timeframe (Unix timestamp in milliseconds)"""

    to: float
    """End timestamp for the query timeframe (Unix timestamp in milliseconds)"""


class RunStatistics(BaseModel):
    """
    Query performance statistics from the database (does not include network latency).
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


class Run(BaseModel):
    """
    The query run metadata including the query definition, execution status, and timeframe.
    """

    id: str
    """Unique identifier for this query run."""

    account_id: str = FieldInfo(alias="accountId")
    """Cloudflare account ID that owns this query run."""

    dry: bool
    """Whether this was a dry run (results not persisted)."""

    granularity: float
    """Number of time-series buckets used for the query.

    Higher values produce more detailed series data.
    """

    query: RunQuery
    """
    A saved query definition with its parameters, metadata, and ownership
    information.
    """

    status: Literal["STARTED", "COMPLETED"]
    """Current execution status of the query run."""

    timeframe: RunTimeframe
    """Time range for the query execution"""

    user_id: str = FieldInfo(alias="userId")
    """ID of the user who initiated the query run."""

    created: Optional[str] = None
    """ISO-8601 timestamp when the query run was created."""

    statistics: Optional[RunStatistics] = None
    """
    Query performance statistics from the database (does not include network
    latency).
    """

    updated: Optional[str] = None
    """ISO-8601 timestamp when the query run was last updated."""


class Statistics(BaseModel):
    """Query performance statistics from the database.

    Includes execution time, rows scanned, and bytes read. Does not include network latency.
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


class Agent(BaseModel):
    agent_class: str = FieldInfo(alias="agentClass")
    """Class name of the Durable Object agent."""

    event_type_counts: Dict[str, float] = FieldInfo(alias="eventTypeCounts")
    """Breakdown of event counts by event type."""

    first_event_ms: float = FieldInfo(alias="firstEventMs")
    """
    Timestamp of the earliest event from this agent in the queried window (Unix
    epoch ms).
    """

    has_errors: bool = FieldInfo(alias="hasErrors")
    """Whether the agent emitted any error events in the queried window."""

    last_event_ms: float = FieldInfo(alias="lastEventMs")
    """Timestamp of the most recent event from this agent (Unix epoch ms)."""

    namespace: str
    """Durable Object namespace the agent belongs to."""

    service: str
    """Worker service name that hosts this agent."""

    total_events: float = FieldInfo(alias="totalEvents")
    """Total number of events emitted by this agent in the queried window."""


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

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    first_seen: Optional[str] = FieldInfo(alias="firstSeen", default=None)

    groups: Optional[List[CalculationSeriesDataGroup]] = None

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)


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

    interval: float

    sample_interval: float = FieldInfo(alias="sampleInterval")

    value: float

    first_seen: Optional[str] = FieldInfo(alias="firstSeen", default=None)

    groups: Optional[List[CompareSeriesDataGroup]] = None

    last_seen: Optional[str] = FieldInfo(alias="lastSeen", default=None)


class CompareSeries(BaseModel):
    data: List[CompareSeriesData]

    time: str


class Compare(BaseModel):
    aggregates: List[CompareAggregate]

    calculation: str

    series: List[CompareSeries]

    alias: Optional[str] = None


class EventsEventMetadata(BaseModel):
    """Structured metadata extracted from the event.

    These fields are indexed and available for filtering and aggregation.
    """

    id: str
    """Unique event ID. Use as the cursor value for offset-based pagination."""

    account: Optional[str] = None
    """Cloudflare account identifier."""

    cloud_service: Optional[str] = FieldInfo(alias="cloudService", default=None)
    """Cloudflare product that generated this event (e.g. workers, pages)."""

    cold_start: Optional[int] = FieldInfo(alias="coldStart", default=None)
    """Whether this was a cold start (1) or warm invocation (0)."""

    cost: Optional[int] = None
    """Estimated cost units for this invocation."""

    duration: Optional[int] = None
    """Span duration in milliseconds."""

    end_time: Optional[int] = FieldInfo(alias="endTime", default=None)
    """Span end time as a Unix epoch in milliseconds."""

    error: Optional[str] = None
    """Error message, present when the log represents an error."""

    error_template: Optional[str] = FieldInfo(alias="errorTemplate", default=None)
    """Templatized version of the error message used for grouping similar errors."""

    fingerprint: Optional[str] = None
    """Content-based fingerprint used to group similar events."""

    level: Optional[str] = None
    """Log level (e.g. log, debug, info, warn, error)."""

    message: Optional[str] = None
    """Log message text."""

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)
    """Templatized version of the log message used for grouping similar messages."""

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """Metric name when the event represents a metric data point."""

    origin: Optional[str] = None
    """Origin of the event (e.g. fetch, scheduled, queue)."""

    parent_span_id: Optional[str] = FieldInfo(alias="parentSpanId", default=None)
    """Span ID of the parent span in the trace hierarchy."""

    provider: Optional[str] = None
    """Infrastructure provider identifier."""

    region: Optional[str] = None
    """Cloudflare data center / region that handled the request."""

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)
    """Cloudflare request ID that ties all logs from a single invocation together."""

    service: Optional[str] = None
    """Worker script name that produced this event."""

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)
    """Span ID for this individual unit of work within a trace."""

    span_name: Optional[str] = FieldInfo(alias="spanName", default=None)
    """Human-readable name for this span."""

    stack_id: Optional[str] = FieldInfo(alias="stackId", default=None)
    """Stack / deployment identifier."""

    start_time: Optional[int] = FieldInfo(alias="startTime", default=None)
    """Span start time as a Unix epoch in milliseconds."""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP response status code returned by the Worker."""

    trace_duration: Optional[int] = FieldInfo(alias="traceDuration", default=None)
    """Total duration of the entire trace in milliseconds."""

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)
    """Distributed trace ID linking spans across services."""

    transaction_name: Optional[str] = FieldInfo(alias="transactionName", default=None)
    """Logical transaction name for this request."""

    trigger: Optional[str] = None
    """What triggered the invocation (e.g. GET /users, POST /orders, queue message)."""

    type: Optional[str] = None
    """Event type classifier (e.g. cf-worker-event, cf-worker-log)."""

    url: Optional[str] = None
    """Request URL that triggered the Worker invocation."""


class EventsEventWorkersUnionMember0ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class EventsEventWorkersUnionMember0(BaseModel):
    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "workflow", "unknown"
    ] = FieldInfo(alias="eventType")

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, object]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    outcome: Optional[str] = None

    script_version: Optional[EventsEventWorkersUnionMember0ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

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
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "workflow", "unknown"
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

    event: Optional[Dict[str, object]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[EventsEventWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

    truncated: Optional[bool] = None


EventsEventWorkers: TypeAlias = Union[EventsEventWorkersUnionMember0, EventsEventWorkersUnionMember1]


class EventsEvent(BaseModel):
    """
    A single telemetry event representing a log line, span, or metric data point emitted by a Worker.
    """

    metadata: EventsEventMetadata = FieldInfo(alias="$metadata")
    """Structured metadata extracted from the event.

    These fields are indexed and available for filtering and aggregation.
    """

    dataset: str
    """The dataset this event belongs to (e.g. cloudflare-workers)."""

    source: Union[str, object]
    """Raw log payload.

    May be a string or a structured object depending on how the log was emitted.
    """

    timestamp: int
    """Event timestamp as a Unix epoch in milliseconds."""

    containers: Optional[object] = FieldInfo(alias="$containers", default=None)
    """
    Cloudflare Containers event information that enriches your logs for identifying
    and debugging issues.
    """

    workers: Optional[EventsEventWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information that enriches your logs for identifying and
    debugging issues.
    """


class EventsField(BaseModel):
    key: str
    """Field name present in the matched events."""

    type: str
    """Data type of the field (string, number, or boolean)."""


class EventsSeriesDataAggregates(BaseModel):
    api_count: int = FieldInfo(alias="_count")

    api_interval: float = FieldInfo(alias="_interval")

    api_first_seen: Optional[str] = FieldInfo(alias="_firstSeen", default=None)

    api_last_seen: Optional[str] = FieldInfo(alias="_lastSeen", default=None)

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
    """Individual event results.

    Present when the query view is 'events'. Contains the matching log lines and their metadata.
    """

    count: Optional[float] = None
    """
    Total number of events matching the query (may exceed the number returned due to
    limits).
    """

    events: Optional[List[EventsEvent]] = None
    """List of individual telemetry events matching the query."""

    fields: Optional[List[EventsField]] = None
    """List of fields discovered in the matched events.

    Useful for building dynamic UIs.
    """

    series: Optional[List[EventsSeries]] = None
    """Time-series data for the matched events, bucketed by the query granularity."""


class InvocationMetadata(BaseModel):
    """Structured metadata extracted from the event.

    These fields are indexed and available for filtering and aggregation.
    """

    id: str
    """Unique event ID. Use as the cursor value for offset-based pagination."""

    account: Optional[str] = None
    """Cloudflare account identifier."""

    cloud_service: Optional[str] = FieldInfo(alias="cloudService", default=None)
    """Cloudflare product that generated this event (e.g. workers, pages)."""

    cold_start: Optional[int] = FieldInfo(alias="coldStart", default=None)
    """Whether this was a cold start (1) or warm invocation (0)."""

    cost: Optional[int] = None
    """Estimated cost units for this invocation."""

    duration: Optional[int] = None
    """Span duration in milliseconds."""

    end_time: Optional[int] = FieldInfo(alias="endTime", default=None)
    """Span end time as a Unix epoch in milliseconds."""

    error: Optional[str] = None
    """Error message, present when the log represents an error."""

    error_template: Optional[str] = FieldInfo(alias="errorTemplate", default=None)
    """Templatized version of the error message used for grouping similar errors."""

    fingerprint: Optional[str] = None
    """Content-based fingerprint used to group similar events."""

    level: Optional[str] = None
    """Log level (e.g. log, debug, info, warn, error)."""

    message: Optional[str] = None
    """Log message text."""

    message_template: Optional[str] = FieldInfo(alias="messageTemplate", default=None)
    """Templatized version of the log message used for grouping similar messages."""

    metric_name: Optional[str] = FieldInfo(alias="metricName", default=None)
    """Metric name when the event represents a metric data point."""

    origin: Optional[str] = None
    """Origin of the event (e.g. fetch, scheduled, queue)."""

    parent_span_id: Optional[str] = FieldInfo(alias="parentSpanId", default=None)
    """Span ID of the parent span in the trace hierarchy."""

    provider: Optional[str] = None
    """Infrastructure provider identifier."""

    region: Optional[str] = None
    """Cloudflare data center / region that handled the request."""

    request_id: Optional[str] = FieldInfo(alias="requestId", default=None)
    """Cloudflare request ID that ties all logs from a single invocation together."""

    service: Optional[str] = None
    """Worker script name that produced this event."""

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)
    """Span ID for this individual unit of work within a trace."""

    span_name: Optional[str] = FieldInfo(alias="spanName", default=None)
    """Human-readable name for this span."""

    stack_id: Optional[str] = FieldInfo(alias="stackId", default=None)
    """Stack / deployment identifier."""

    start_time: Optional[int] = FieldInfo(alias="startTime", default=None)
    """Span start time as a Unix epoch in milliseconds."""

    status_code: Optional[int] = FieldInfo(alias="statusCode", default=None)
    """HTTP response status code returned by the Worker."""

    trace_duration: Optional[int] = FieldInfo(alias="traceDuration", default=None)
    """Total duration of the entire trace in milliseconds."""

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)
    """Distributed trace ID linking spans across services."""

    transaction_name: Optional[str] = FieldInfo(alias="transactionName", default=None)
    """Logical transaction name for this request."""

    trigger: Optional[str] = None
    """What triggered the invocation (e.g. GET /users, POST /orders, queue message)."""

    type: Optional[str] = None
    """Event type classifier (e.g. cf-worker-event, cf-worker-log)."""

    url: Optional[str] = None
    """Request URL that triggered the Worker invocation."""


class InvocationWorkersUnionMember0ScriptVersion(BaseModel):
    id: Optional[str] = None

    message: Optional[str] = None

    tag: Optional[str] = None


class InvocationWorkersUnionMember0(BaseModel):
    event_type: Literal[
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "workflow", "unknown"
    ] = FieldInfo(alias="eventType")

    request_id: str = FieldInfo(alias="requestId")

    script_name: str = FieldInfo(alias="scriptName")

    durable_object_id: Optional[str] = FieldInfo(alias="durableObjectId", default=None)

    entrypoint: Optional[str] = None

    event: Optional[Dict[str, object]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    outcome: Optional[str] = None

    script_version: Optional[InvocationWorkersUnionMember0ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

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
        "fetch", "scheduled", "alarm", "cron", "queue", "email", "tail", "rpc", "websocket", "workflow", "unknown"
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

    event: Optional[Dict[str, object]] = None

    execution_model: Optional[Literal["durableObject", "stateless"]] = FieldInfo(alias="executionModel", default=None)

    script_version: Optional[InvocationWorkersUnionMember1ScriptVersion] = FieldInfo(
        alias="scriptVersion", default=None
    )

    span_id: Optional[str] = FieldInfo(alias="spanId", default=None)

    trace_id: Optional[str] = FieldInfo(alias="traceId", default=None)

    truncated: Optional[bool] = None


InvocationWorkers: TypeAlias = Union[InvocationWorkersUnionMember0, InvocationWorkersUnionMember1]


class Invocation(BaseModel):
    """
    A single telemetry event representing a log line, span, or metric data point emitted by a Worker.
    """

    metadata: InvocationMetadata = FieldInfo(alias="$metadata")
    """Structured metadata extracted from the event.

    These fields are indexed and available for filtering and aggregation.
    """

    dataset: str
    """The dataset this event belongs to (e.g. cloudflare-workers)."""

    source: Union[str, object]
    """Raw log payload.

    May be a string or a structured object depending on how the log was emitted.
    """

    timestamp: int
    """Event timestamp as a Unix epoch in milliseconds."""

    containers: Optional[object] = FieldInfo(alias="$containers", default=None)
    """
    Cloudflare Containers event information that enriches your logs for identifying
    and debugging issues.
    """

    workers: Optional[InvocationWorkers] = FieldInfo(alias="$workers", default=None)
    """
    Cloudflare Workers event information that enriches your logs for identifying and
    debugging issues.
    """


class Trace(BaseModel):
    root_span_name: str = FieldInfo(alias="rootSpanName")
    """Name of the root span that initiated the trace."""

    root_transaction_name: str = FieldInfo(alias="rootTransactionName")
    """Logical transaction name for the root span."""

    service: List[str]
    """List of Worker services involved in the trace."""

    spans: float
    """Total number of spans in the trace."""

    trace_duration_ms: float = FieldInfo(alias="traceDurationMs")
    """Total duration of the trace in milliseconds."""

    trace_end_ms: float = FieldInfo(alias="traceEndMs")
    """Trace end time as a Unix epoch in milliseconds."""

    trace_id: str = FieldInfo(alias="traceId")
    """Unique identifier for the distributed trace."""

    trace_start_ms: float = FieldInfo(alias="traceStartMs")
    """Trace start time as a Unix epoch in milliseconds."""

    errors: Optional[List[str]] = None
    """Error messages encountered during the trace, if any."""


class TelemetryQueryResponse(BaseModel):
    """Complete results of a query run.

    The populated fields depend on the requested view type (events, calculations, invocations, traces, or agents).
    """

    run: Run
    """
    The query run metadata including the query definition, execution status, and
    timeframe.
    """

    statistics: Statistics
    """Query performance statistics from the database.

    Includes execution time, rows scanned, and bytes read. Does not include network
    latency.
    """

    agents: Optional[List[Agent]] = None
    """Durable Object agent summaries.

    Present when the query view is 'agents'. Each entry represents an agent with its
    event counts and status.
    """

    calculations: Optional[List[Calculation]] = None
    """Aggregated calculation results.

    Present when the query view is 'calculations'. Contains computed metrics (count,
    avg, p99, etc.) with optional group-by breakdowns and time-series data.
    """

    compare: Optional[List[Compare]] = None
    """Comparison calculation results from the previous time period.

    Present when the compare option is enabled. Same structure as calculations.
    """

    events: Optional[Events] = None
    """Individual event results.

    Present when the query view is 'events'. Contains the matching log lines and
    their metadata.
    """

    invocations: Optional[Dict[str, List[Invocation]]] = None
    """Events grouped by invocation (request ID).

    Present when the query view is 'invocations'. Each key is a request ID mapping
    to all events from that invocation.
    """

    traces: Optional[List[Trace]] = None
    """Trace summaries matching the query.

    Present when the query view is 'traces'. Each entry represents a distributed
    trace with its spans, duration, and services involved.
    """
