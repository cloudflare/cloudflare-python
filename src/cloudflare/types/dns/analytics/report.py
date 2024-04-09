# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from ...unnamed_schema_ref_6595695ff25b0614667b25f66b7bbaba import UnnamedSchemaRef6595695ff25b0614667b25f66b7bbaba

__all__ = ["Report", "Query"]


class Query(BaseModel):
    dimensions: List[str]
    """Array of dimension names."""

    limit: int
    """Limit number of returned metrics."""

    metrics: List[str]
    """Array of metric names."""

    since: datetime
    """Start date and time of requesting data period in ISO 8601 format."""

    until: datetime
    """End date and time of requesting data period in ISO 8601 format."""

    filters: Optional[str] = None
    """Segmentation filter in 'attribute operator value' format."""

    sort: Optional[List[str]] = None
    """
    Array of dimensions to sort by, where each dimension may be prefixed by -
    (descending) or + (ascending).
    """


class Report(BaseModel):
    data: List[UnnamedSchemaRef6595695ff25b0614667b25f66b7bbaba]
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

    totals: object
    """
    Total results for metrics across all data (object mapping metric names to
    values).
    """
