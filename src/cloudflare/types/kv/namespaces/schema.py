# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["Schema", "Data", "Query"]


class Data(BaseModel):
    metrics: List[List[float]]
    """List of metrics returned by the query."""

    dimensions: Optional[List[str]] = None


class Query(BaseModel):
    dimensions: Optional[List[str]] = None
    """Can be used to break down the data by given attributes."""

    filters: Optional[str] = None
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

    limit: Optional[int] = None
    """Limit number of returned metrics."""

    metrics: Optional[List[str]] = None
    """One or more metrics to compute."""

    since: Optional[datetime] = None
    """Start of time interval to query, defaults to 6 hours before request received."""

    sort: Optional[List[str]] = None
    """
    Array of dimensions or metrics to sort by, each dimension/metric may be prefixed
    by - (descending) or + (ascending).
    """

    until: Optional[datetime] = None
    """End of time interval to query, defaults to current time."""


class Schema(BaseModel):
    data: Optional[List[Data]] = None

    data_lag: float
    """Number of seconds between current time and last processed event, i.e.

    how many seconds of data could be missing.
    """

    max: Dict[str, float]
    """Maximum results for each metric."""

    min: Dict[str, float]
    """Minimum results for each metric."""

    query: Query
    """For specifying result metrics."""

    rows: float
    """Total number of rows in the result."""

    totals: Dict[str, float]
    """Total results for metrics across all data."""

    time_intervals: Optional[List[List[datetime]]] = None
    """Time interval buckets by beginning and ending"""
