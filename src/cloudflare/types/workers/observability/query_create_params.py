# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = [
    "QueryCreateParams",
    "Parameters",
    "ParametersCalculation",
    "ParametersFilter",
    "ParametersFilterUnionMember0",
    "ParametersFilterWorkersObservabilityFilterLeaf",
    "ParametersGroupBy",
    "ParametersHaving",
    "ParametersNeedle",
    "ParametersOrderBy",
]


class QueryCreateParams(TypedDict, total=False):
    account_id: Required[str]

    description: Required[Optional[str]]

    name: Required[str]
    """Query name"""

    parameters: Required[Parameters]


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


class ParametersFilterUnionMember0(TypedDict, total=False):
    filter_combination: Required[Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]]

    filters: Required[Iterable[object]]

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
    calculations: Iterable[ParametersCalculation]
    """Create Calculations to compute as part of the query."""

    datasets: SequenceNotStr[str]
    """Set the Datasets to query. Leave it empty to query all the datasets."""

    filter_combination: Annotated[Literal["and", "or", "AND", "OR"], PropertyInfo(alias="filterCombination")]
    """Set a Flag to describe how to combine the filters on the query."""

    filters: Iterable[ParametersFilter]
    """Configure the Filters to apply to the query.

    Supports nested groups via kind: 'group'.
    """

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
