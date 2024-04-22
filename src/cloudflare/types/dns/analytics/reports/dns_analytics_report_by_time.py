# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ....shared import UnnamedSchemaRef23, UnnamedSchemaRef24
from ....._models import BaseModel

__all__ = ["DNSAnalyticsReportByTime", "Data"]


class Data(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[UnnamedSchemaRef23]
    """Array with one item per requested metric.

    Each item is an array of values, broken down by time interval.
    """


class DNSAnalyticsReportByTime(BaseModel):
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

    query: UnnamedSchemaRef24

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
