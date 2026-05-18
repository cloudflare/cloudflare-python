# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "QueryListResponse",
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


class ParametersCalculation(BaseModel):
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


class ParametersFilterUnionMember0(BaseModel):
    filter_combination: Literal["and", "or", "AND", "OR"] = FieldInfo(alias="filterCombination")

    filters: List[object]

    kind: Literal["group"]


class ParametersFilterWorkersObservabilityFilterLeaf(BaseModel):
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


ParametersFilter: TypeAlias = Union[ParametersFilterUnionMember0, ParametersFilterWorkersObservabilityFilterLeaf]


class ParametersGroupBy(BaseModel):
    type: Literal["string", "number", "boolean"]

    value: str


class ParametersHaving(BaseModel):
    key: str

    operation: Literal["eq", "neq", "gt", "gte", "lt", "lte"]

    value: float


class ParametersNeedle(BaseModel):
    """Define an expression to search using full-text search."""

    value: Union[str, float, bool]

    is_regex: Optional[bool] = FieldInfo(alias="isRegex", default=None)

    match_case: Optional[bool] = FieldInfo(alias="matchCase", default=None)


class ParametersOrderBy(BaseModel):
    """Configure the order of the results returned by the query."""

    value: str
    """Configure which Calculation to order the results by."""

    order: Optional[Literal["asc", "desc"]] = None
    """Set the order of the results"""


class Parameters(BaseModel):
    calculations: Optional[List[ParametersCalculation]] = None
    """Create Calculations to compute as part of the query."""

    datasets: Optional[List[str]] = None
    """Set the Datasets to query. Leave it empty to query all the datasets."""

    filter_combination: Optional[Literal["and", "or", "AND", "OR"]] = FieldInfo(alias="filterCombination", default=None)
    """Set a Flag to describe how to combine the filters on the query."""

    filters: Optional[List[ParametersFilter]] = None
    """Configure the Filters to apply to the query.

    Supports nested groups via kind: 'group'.
    """

    group_bys: Optional[List[ParametersGroupBy]] = FieldInfo(alias="groupBys", default=None)
    """Define how to group the results of the query."""

    havings: Optional[List[ParametersHaving]] = None
    """Configure the Having clauses that filter on calculations in the query result."""

    limit: Optional[int] = None
    """Set a limit on the number of results / records returned by the query"""

    needle: Optional[ParametersNeedle] = None
    """Define an expression to search using full-text search."""

    order_by: Optional[ParametersOrderBy] = FieldInfo(alias="orderBy", default=None)
    """Configure the order of the results returned by the query."""


class QueryListResponse(BaseModel):
    id: str

    adhoc: bool
    """If the query wasn't explcitly saved"""

    created: str

    created_by: str = FieldInfo(alias="createdBy")

    description: Optional[str] = None

    name: str
    """Query name"""

    parameters: Parameters

    updated: str

    updated_by: str = FieldInfo(alias="updatedBy")
