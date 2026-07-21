# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["IndicatorListParams", "Search"]


class IndicatorListParams(TypedDict, total=False):
    account_id: Required[str]
    """Account ID."""

    dataset_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="datasetIds")]
    """
    Dataset UUIDs to scope to (repeat the param for multiple), or 'all' / '\\**' for
    every readable indicator dataset. Omit to search all readable datasets.
    """

    indicator_type: Annotated[str, PropertyInfo(alias="indicatorType")]

    page: float

    page_size: Annotated[float, PropertyInfo(alias="pageSize")]

    related_event: Annotated[SequenceNotStr[str], PropertyInfo(alias="relatedEvent")]
    """Filter indicators by related event UUID(s).

    Multiple UUIDs can be provided by repeating the parameter.
    """

    search: Iterable[Search]
    """Structured search as a JSON array of {field, op, value} objects.

    Searchable fields: value, indicatorType. Multiple conditions are AND'd together.
    Max 10 conditions per request.
    """


class Search(TypedDict, total=False):
    field: Required[Literal["value", "indicatorType", "uuid"]]
    """The indicator field to search on. Allowed: value, indicatorType, uuid."""

    op: Required[
        Literal["equals", "not", "gt", "gte", "lt", "lte", "like", "contains", "startsWith", "endsWith", "in", "find"]
    ]
    """Search operator.

    Use 'in' for bulk lookup of up to 100 values at once, e.g. {field:'value',
    op:'in', value:['evil.com','bad.org']}.
    """

    value: Required[Union[str, SequenceNotStr[str]]]
    """Search value.

    String for most operators. Array of strings for 'in' operator (max 100 items).
    """
