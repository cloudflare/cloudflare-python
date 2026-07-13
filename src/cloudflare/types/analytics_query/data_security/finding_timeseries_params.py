# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["FindingTimeseriesParams", "Filter"]


class FindingTimeseriesParams(TypedDict, total=False):
    account_id: Required[str]

    filters: Required[Iterable[Filter]]
    """Filters to apply."""

    from_: Required[Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]]
    """Start of the query time range (inclusive). RFC3339."""

    to: Required[Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]]
    """End of the query time range (exclusive). RFC3339."""


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
