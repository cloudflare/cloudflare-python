# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "TelemetryQueryParams",
    "Timeframe",
    "Parameters",
    "ParametersCalculation",
    "ParametersFilter",
    "ParametersFilterUnionMember0",
    "ParametersFilterUnionMember0Filter",
    "ParametersFilterUnionMember0FilterUnionMember0",
    "ParametersFilterUnionMember0FilterWorkersObservabilityFilterLeaf",
    "ParametersFilterWorkersObservabilityFilterLeaf",
    "ParametersGroupBy",
    "ParametersHaving",
    "ParametersNeedle",
    "ParametersOrderBy",
]


class TelemetryQueryParams(TypedDict, total=False):
    account_id: Required[str]

    query_id: Required[Annotated[str, PropertyInfo(alias="queryId")]]
    """Identifier for the query.

    When parameters are omitted, this ID is used to load a previously saved query's
    parameters. When providing parameters inline, pass any identifier (e.g. an
    ad-hoc ID).
    """

    timeframe: Required[Timeframe]
    """Timeframe for the query using Unix timestamps in milliseconds.

    Narrower timeframes produce faster responses and more specific results.
    """

    chart: bool
    """When true, includes time-series data in the response."""

    compare: bool
    """
    When true, includes a comparison dataset from the previous time period of equal
    length.
    """

    dry: bool
    """When true, executes the query without persisting the results.

    Useful for validation or previewing.
    """

    granularity: float
    """Number of time-series buckets.

    Only used when view is 'calculations'. Omit to let the system auto-detect an
    appropriate granularity.
    """

    ignore_series: Annotated[bool, PropertyInfo(alias="ignoreSeries")]
    """
    When true, omits time-series data from the response and returns only aggregated
    values. Reduces response size when series are not needed.
    """

    limit: float
    """Maximum number of events to return when view is 'events'.

    Also controls the number of group-by rows when view is 'calculations'.
    """

    offset: str
    """Cursor for pagination in event, trace, and invocation views.

    Pass the $metadata.id of the last returned item to fetch the next page.
    """

    offset_by: Annotated[float, PropertyInfo(alias="offsetBy")]
    """Numeric offset for paginating grouped/pattern results (top-N lists).

    Use together with limit. Not used by cursor-based pagination.
    """

    offset_direction: Annotated[str, PropertyInfo(alias="offsetDirection")]
    """Pagination direction: 'next' for forward, 'prev' for backward."""

    parameters: Parameters
    """
    Query parameters defining what data to retrieve — filters, calculations,
    group-bys, and ordering. In practice this should always be provided for ad-hoc
    queries. Only omit when executing a previously saved query by queryId. Use the
    keys and values endpoints to discover available fields before building filters.
    """

    view: Literal["traces", "events", "calculations", "invocations", "requests", "agents"]
    """Controls the shape of the response.

    'events': individual log lines matching the query. 'calculations': aggregated
    metrics (count, avg, p99, etc.) with optional group-by breakdowns and
    time-series. 'invocations': events grouped by request ID. 'traces': distributed
    trace summaries. 'agents': Durable Object agent summaries.
    """


_TimeframeReservedKeywords = TypedDict(
    "_TimeframeReservedKeywords",
    {
        "from": float,
    },
    total=False,
)


class Timeframe(_TimeframeReservedKeywords, total=False):
    """Timeframe for the query using Unix timestamps in milliseconds.

    Narrower timeframes produce faster responses and more specific results.
    """

    to: Required[float]
    """End timestamp for the query timeframe (Unix timestamp in milliseconds)"""


class ParametersCalculation(TypedDict, total=False):
    operator: Required[
        Literal[
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
    ]
    """Aggregation operator to apply.

    Examples: count, avg, sum, min, max, p50, p90, p95, p99, uniq, stddev, variance.
    """

    alias: str
    """Custom label for this calculation in the results.

    Useful for distinguishing multiple calculations.
    """

    key: str
    """Field name to calculate over.

    Must exist in the data — verify with the keys endpoint. Omit for operators that
    don't require a key (e.g. count).
    """

    key_type: Annotated[Literal["string", "number", "boolean"], PropertyInfo(alias="keyType")]
    """Data type of the key.

    Required when key is provided to ensure correct aggregation.
    """


class ParametersFilterUnionMember0FilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[object]]

    kind: Required[Literal["group"]]


class ParametersFilterUnionMember0FilterWorkersObservabilityFilterLeaf(TypedDict, total=False):
    """A filter condition applied to query results.

    Use the keys and values endpoints to discover available fields and their values before constructing filters.
    """

    key: Required[str]
    """Filter field name.

    Use verified keys from previous query results or the keys endpoint. Common keys
    include $metadata.service, $metadata.origin, $metadata.trigger,
    $metadata.message, and $metadata.error.
    """

    operation: Required[
        Literal[
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
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, regex. Existence: exists,
    is_null. Set membership: in, not_in (comma-separated values). Numeric: eq, neq,
    gt, gte, lt, lte.
    """

    type: Required[Literal["string", "number", "boolean"]]
    """Data type of the filter field.

    Must match the actual type of the key being filtered.
    """

    kind: Literal["filter"]
    """Discriminator for leaf filter nodes.

    Always 'filter' when present; may be omitted.
    """

    value: Union[str, float, bool]
    """Comparison value.

    Must match actual values in your data — verify with the values endpoint. Ensure
    the value type (string/number/boolean) matches the field type. String
    comparisons are case-sensitive. Regex uses RE2 syntax (no
    lookaheads/lookbehinds).
    """


ParametersFilterUnionMember0Filter: TypeAlias = Union[
    ParametersFilterUnionMember0FilterUnionMember0, ParametersFilterUnionMember0FilterWorkersObservabilityFilterLeaf
]


class ParametersFilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[ParametersFilterUnionMember0Filter]]

    kind: Required[Literal["group"]]


class ParametersFilterWorkersObservabilityFilterLeaf(TypedDict, total=False):
    """A filter condition applied to query results.

    Use the keys and values endpoints to discover available fields and their values before constructing filters.
    """

    key: Required[str]
    """Filter field name.

    Use verified keys from previous query results or the keys endpoint. Common keys
    include $metadata.service, $metadata.origin, $metadata.trigger,
    $metadata.message, and $metadata.error.
    """

    operation: Required[
        Literal[
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
    ]
    """Comparison operator.

    String operators: includes, not_includes, starts_with, regex. Existence: exists,
    is_null. Set membership: in, not_in (comma-separated values). Numeric: eq, neq,
    gt, gte, lt, lte.
    """

    type: Required[Literal["string", "number", "boolean"]]
    """Data type of the filter field.

    Must match the actual type of the key being filtered.
    """

    kind: Literal["filter"]
    """Discriminator for leaf filter nodes.

    Always 'filter' when present; may be omitted.
    """

    value: Union[str, float, bool]
    """Comparison value.

    Must match actual values in your data — verify with the values endpoint. Ensure
    the value type (string/number/boolean) matches the field type. String
    comparisons are case-sensitive. Regex uses RE2 syntax (no
    lookaheads/lookbehinds).
    """


ParametersFilter: TypeAlias = Union[ParametersFilterUnionMember0, ParametersFilterWorkersObservabilityFilterLeaf]


class ParametersGroupBy(TypedDict, total=False):
    type: Required[Literal["string", "number", "boolean"]]
    """Data type of the group-by field."""

    value: Required[str]
    """Field name to group results by (e.g. $metadata.service, $metadata.statusCode)."""


class ParametersHaving(TypedDict, total=False):
    key: Required[str]
    """Calculation alias or operator to filter on after aggregation."""

    operation: Required[Literal["eq", "neq", "gt", "gte", "lt", "lte"]]
    """Numeric comparison operator: eq, neq, gt, gte, lt, lte."""

    value: Required[float]
    """Threshold value to compare the calculation result against."""


class ParametersNeedle(TypedDict, total=False):
    """Full-text search expression applied across all event fields.

    Matches events containing the specified text.
    """

    value: Required[Union[str, float, bool]]
    """The text or pattern to search for."""

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]
    """When true, treats the value as a regular expression (RE2 syntax)."""

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]
    """When true, performs a case-sensitive search. Defaults to case-insensitive."""


class ParametersOrderBy(TypedDict, total=False):
    """Ordering for grouped calculation results.

    Only effective when a group-by is present.
    """

    value: Required[str]
    """Alias of the calculation to order results by.

    Must match the alias (or operator) of a calculation in the query.
    """

    order: Literal["asc", "desc"]
    """Sort direction: 'asc' for ascending, 'desc' for descending."""


class Parameters(TypedDict, total=False):
    """
    Query parameters defining what data to retrieve — filters, calculations, group-bys, and ordering. In practice this should always be provided for ad-hoc queries. Only omit when executing a previously saved query by queryId. Use the keys and values endpoints to discover available fields before building filters.
    """

    calculations: Iterable[ParametersCalculation]
    """Aggregation calculations to compute (e.g.

    count, avg, p99). Each calculation produces aggregate values and optional
    time-series data.
    """

    datasets: SequenceNotStr[str]
    """Datasets to query. Leave empty to query all available datasets."""

    filter_combination: Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]
    """
    Logical operator for combining top-level filters: 'and' (all must match) or 'or'
    (any must match). Defaults to 'and'.
    """

    filters: Iterable[ParametersFilter]
    """Filters to narrow query results.

    Use the keys and values endpoints to discover available fields before building
    filters. Supports nested groups via kind: 'group'. Maximum nesting depth is 4.
    """

    group_bys: Annotated[Iterable[ParametersGroupBy], PropertyInfo(alias="groupBys")]
    """Fields to group calculation results by.

    Only applicable when the query view is 'calculations'. Produces per-group
    aggregate values.
    """

    havings: Iterable[ParametersHaving]
    """Post-aggregation filters applied to calculation results.

    Use to filter groups after aggregation (e.g. only groups where count > 100).
    """

    limit: int
    """Maximum number of group-by rows to return in calculation results.

    A value of 10 is a sensible default for most use cases.
    """

    needle: ParametersNeedle
    """Full-text search expression applied across all event fields.

    Matches events containing the specified text.
    """

    order_by: Annotated[ParametersOrderBy, PropertyInfo(alias="orderBy")]
    """Ordering for grouped calculation results.

    Only effective when a group-by is present.
    """
