# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from ...._models import BaseModel

__all__ = ["FindingTimeseriesResponse"]


class FindingTimeseriesResponse(BaseModel):
    """Merged CASB and CDE findings timeseries result."""

    slots: List[Dict[str, object]]
    """Contains time-bucketed result rows.

    Each slot includes a `timestamp` plus `content` and `posture` maps with `cloud`
    and `saas` keys.
    """

    resolution: Optional[str] = None
    """Always null for this endpoint."""
