# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel
from .firewall.delta import Delta

__all__ = ["DNSAnalyticsQuery"]


class DNSAnalyticsQuery(BaseModel):
    dimensions: List[str]
    """Array of dimension names."""

    limit: int
    """Limit number of returned metrics."""

    metrics: List[str]
    """Array of metric names."""

    since: datetime
    """Start date and time of requesting data period in ISO 8601 format."""

    time_delta: Delta
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
