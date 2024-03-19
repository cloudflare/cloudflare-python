# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["DNSDNSAnalyticsAPIReportBytime", "Data", "Query"]


class Data(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[List[object]]
    """Array with one item per requested metric.

    Each item is an array of values, broken down by time interval.
    """


class Query(BaseModel):
    dimensions: List[str]
    """Array of dimension names."""

    limit: int
    """Limit number of returned metrics."""

    metrics: List[str]
    """Array of metric names."""

    since: datetime
    """Start date and time of requesting data period in ISO 8601 format."""

    time_delta: Literal["all", "auto", "year", "quarter", "month", "week", "day", "hour", "dekaminute", "minute"]
    """Unit of time to group data by."""

    until: datetime
    """End date and time of requesting data period in ISO 8601 format."""

    filters: Optional[str] = None
    """Segmentation filter in 'attribute operator value' format."""

    sort: Optional[List[str]] = None
    """
    Array of dimensions to sort by, where each dimension may be prefixed by -
    (descending) or + (ascending).
    """


class DNSDNSAnalyticsAPIReportBytime(BaseModel):
    data: List[Data]
    """Array with one row per combination of dimension values."""

    data_lag: float
    """
    Number of seconds between current time and last processed event, in another
    words how many seconds of data could be missing.
    """

    max: object
    """Maximum results for each metric (object mapping metric names to values).

    Currently always an empty object.
    """

    min: object
    """Minimum results for each metric (object mapping metric names to values).

    Currently always an empty object.
    """

    query: Query

    rows: float
    """Total number of rows in the result."""

    time_intervals: List[List[datetime]]
    """Array of time intervals in the response data.

    Each interval is represented as an array containing two values: the start time,
    and the end time.
    """

    totals: object
    """
    Total results for metrics across all data (object mapping metric names to
    values).
    """
