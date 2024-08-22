# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ....._models import BaseModel
from ...dns_analytics_query import DNSAnalyticsQuery
from ...dns_analytics_nominal_metric import DNSAnalyticsNominalMetric

__all__ = ["ByTime", "Data"]


class Data(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[DNSAnalyticsNominalMetric]
    """Array with one item per requested metric.

    Each item is an array of values, broken down by time interval.
    """


class ByTime(BaseModel):
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

    query: DNSAnalyticsQuery

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
