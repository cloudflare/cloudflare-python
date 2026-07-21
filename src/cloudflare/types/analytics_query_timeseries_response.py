# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from .._models import BaseModel

__all__ = ["AnalyticsQueryTimeseriesResponse"]


class AnalyticsQueryTimeseriesResponse(BaseModel):
    resolution: str
    """The resolution used for time bucketing."""

    slots: List[Dict[str, object]]
    """Time-bucketed result rows.

    Each slot contains a `time_bucket` field plus the requested stats and group-by
    dimensions.
    """
