# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AnalyticsQuerySummaryResponse"]


class AnalyticsQuerySummaryResponse(BaseModel):
    current_total: List[Dict[str, object]] = FieldInfo(alias="currentTotal")
    """Aggregated stats for the requested time range."""

    previous_total: List[Dict[str, object]] = FieldInfo(alias="previousTotal")
    """Aggregated stats for the equivalent preceding time range, for trend comparison."""
