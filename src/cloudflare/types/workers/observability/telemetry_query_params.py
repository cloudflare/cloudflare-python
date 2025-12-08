# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "TelemetryQueryParams",
    "Timeframe",
    "Parameters",
    "ParametersCalculation",
    "ParametersFilter",
    "ParametersGroupBy",
    "ParametersHaving",
    "ParametersNeedle",
    "ParametersOrderBy",
]


class TelemetryQueryParams(TypedDict, total=False):
    account_id: Required[str]

    query_id: Required[Annotated[str, PropertyInfo(alias="queryId")]]
    """Unique identifier for the query to execute"""

    timeframe: Required[Timeframe]
    """Time range for the query execution"""

    chart: bool
    """Whether to include timeseties data in the response"""

    compare: bool
    """Whether to include comparison data with previous time periods"""

    dry: bool
    """Whether to perform a dry run without saving the results of the query.

    Useful for validation
    """

    granularity: float
    """Time granularity for aggregating results (in milliseconds).

    Controls the bucketing of time-series data
    """

    ignore_series: Annotated[bool, PropertyInfo(alias="ignoreSeries")]
    """
    Whether to ignore time-series data in the results and return only aggregated
    values
    """

    limit: float
    """Maximum number of events to return."""

    offset: str
    """Cursor for pagination to retrieve the next set of results"""

    offset_by: Annotated[float, PropertyInfo(alias="offsetBy")]
    """Number of events to skip for pagination. Used in conjunction with offset"""

    offset_direction: Annotated[str, PropertyInfo(alias="offsetDirection")]
    """Direction for offset-based pagination (e.g., 'next', 'prev')"""

    parameters: Parameters
    """Optional parameters to pass to the query execution"""

    pattern_type: Annotated[Literal["message", "error"], PropertyInfo(alias="patternType")]
    """Type of pattern to search for when using pattern-based views"""

    view: Literal["traces", "events", "calculations", "invocations", "requests", "patterns"]
    """View type for presenting the query results."""


_TimeframeReservedKeywords = TypedDict(
    "_TimeframeReservedKeywords",
    {
        "from": float,
    },
    total=False,
)


class Timeframe(_TimeframeReservedKeywords, total=False):
    """Time range for the query execution"""

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

    alias: str

    key: str

    key_type: Annotated[Literal["string", "number", "boolean"], PropertyInfo(alias="keyType")]


class ParametersFilter(TypedDict, total=False):
    key: Required[str]

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

    type: Required[Literal["string", "number", "boolean"]]

    value: Union[str, float, bool]


class ParametersGroupBy(TypedDict, total=False):
    type: Required[Literal["string", "number", "boolean"]]

    value: Required[str]


class ParametersHaving(TypedDict, total=False):
    key: Required[str]

    operation: Required[Literal["eq", "neq", "gt", "gte", "lt", "lte"]]

    value: Required[float]


class ParametersNeedle(TypedDict, total=False):
    """Define an expression to search using full-text search."""

    value: Required[Union[str, float, bool]]

    is_regex: Annotated[bool, PropertyInfo(alias="isRegex")]

    match_case: Annotated[bool, PropertyInfo(alias="matchCase")]


class ParametersOrderBy(TypedDict, total=False):
    """Configure the order of the results returned by the query."""

    value: Required[str]
    """Configure which Calculation to order the results by."""

    order: Literal["asc", "desc"]
    """Set the order of the results"""


class Parameters(TypedDict, total=False):
    """Optional parameters to pass to the query execution"""

    calculations: Iterable[ParametersCalculation]
    """Create Calculations to compute as part of the query."""

    datasets: SequenceNotStr[str]
    """Set the Datasets to query. Leave it empty to query all the datasets."""

    filter_combination: Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]
    """Set a Flag to describe how to combine the filters on the query."""

    filters: Iterable[ParametersFilter]
    """Configure the Filters to apply to the query."""

    group_bys: Annotated[Iterable[ParametersGroupBy], PropertyInfo(alias="groupBys")]
    """Define how to group the results of the query."""

    havings: Iterable[ParametersHaving]
    """Configure the Having clauses that filter on calculations in the query result."""

    limit: int
    """Set a limit on the number of results / records returned by the query"""

    needle: ParametersNeedle
    """Define an expression to search using full-text search."""

    order_by: Annotated[ParametersOrderBy, PropertyInfo(alias="orderBy")]
    """Configure the order of the results returned by the query."""
