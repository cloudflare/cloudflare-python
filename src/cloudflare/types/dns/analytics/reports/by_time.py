# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ....._models import BaseModel
from ....unnamed_schema_ref_65be9614de145bf4a58d0fddf46df7ca import UnnamedSchemaRef65be9614de145bf4a58d0fddf46df7ca
from ....unnamed_schema_ref_85b45d163202bbab7456da6b346d9fe2 import UnnamedSchemaRef85b45d163202bbab7456da6b346d9fe2

__all__ = ["ByTime", "Data"]


class Data(BaseModel):
    dimensions: List[str]
    """
    Array of dimension values, representing the combination of dimension values
    corresponding to this row.
    """

    metrics: List[UnnamedSchemaRef65be9614de145bf4a58d0fddf46df7ca]
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

    query: UnnamedSchemaRef85b45d163202bbab7456da6b346d9fe2

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
