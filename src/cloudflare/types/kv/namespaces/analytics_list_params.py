# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["AnalyticsListParams", "Query"]


class AnalyticsListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    query: Query
    """For specifying result metrics."""


class Query(TypedDict, total=False):
    dimensions: List[Literal["accountId", "responseCode", "requestType"]]
    """Can be used to break down the data by given attributes."""

    filters: str
    """Used to filter rows by one or more dimensions.

    Filters can be combined using OR and AND boolean logic. AND takes precedence
    over OR in all the expressions. The OR operator is defined using a comma (,) or
    OR keyword surrounded by whitespace. The AND operator is defined using a
    semicolon (;) or AND keyword surrounded by whitespace. Note that the semicolon
    is a reserved character in URLs (rfc1738) and needs to be percent-encoded as
    %3B. Comparison options are:

    | Operator | Name                     | URL Encoded |
    | -------- | ------------------------ | ----------- |
    | ==       | Equals                   | %3D%3D      |
    | !=       | Does not equals          | !%3D        |
    | >        | Greater Than             | %3E         |
    | <        | Less Than                | %3C         |
    | >=       | Greater than or equal to | %3E%3D      |
    | <=       | Less than or equal to    | %3C%3D .    |
    """

    limit: int
    """Limit number of returned metrics."""

    metrics: List[Literal["requests", "writeKiB", "readKiB"]]
    """One or more metrics to compute."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Start of time interval to query, defaults to 6 hours before request received."""

    sort: List[str]
    """
    Array of dimensions or metrics to sort by, each dimension/metric may be prefixed
    by - (descending) or + (ascending).
    """

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of time interval to query, defaults to current time."""
