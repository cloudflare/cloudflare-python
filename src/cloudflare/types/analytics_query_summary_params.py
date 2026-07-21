# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AnalyticsQuerySummaryParams", "Filter"]


class AnalyticsQuerySummaryParams(TypedDict, total=False):
    account_id: Required[str]

    filters: Required[Iterable[Filter]]
    """Filters to apply before aggregating results."""

    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """The start of the query time range (inclusive).

    RFC3339 format with timezone is required (e.g. `2024-11-05T00:00:00Z`).
    """

    group_by: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="groupBy")]]
    """Specifies the column names to group results by.

    Requires valid columns for the target dataset.
    """

    stats: Required[SequenceNotStr[str]]
    """Specifies the stat names to include in results.

    Requires valid stats for the target dataset (e.g. `attemptsTotal`,
    `bytesTotal`).
    """

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """Specifies the end of the query time range (exclusive).

    Requires RFC3339 format with timezone.
    """


class Filter(TypedDict, total=False):
    """A filter to apply to the query."""

    name: Required[str]
    """Specifies the column name to filter on.

    Requires a valid column for the target dataset (e.g. `country`, `allowed`,
    `appId`).
    """

    op: Required[str]
    """Filter operator.

    Common values: `eq`, `neq`, `in`, `not_in`, `gt`, `lt`, `gte`, `lte`.
    """

    values: Required[SequenceNotStr[Union[str, bool, float]]]
    """Values to match against. Type depends on the column."""
