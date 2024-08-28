# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "SummaryResponseTTLResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Summary0",
]


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    normalization: str

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Summary0(BaseModel):
    less_than_or_equal_to_zero_minute: str = FieldInfo(alias="<=0m")

    less_than_or_equal_to_fifteen_minutes: str = FieldInfo(alias="<=15m")

    less_than_or_equal_to_one_day: str = FieldInfo(alias="<=1d")

    less_than_or_equal_to_one_hour: str = FieldInfo(alias="<=1h")

    less_than_or_equal_to_one_minute: str = FieldInfo(alias="<=1m")

    less_than_or_equal_to_one_week: str = FieldInfo(alias="<=1w")

    less_than_or_equal_to_one_year: str = FieldInfo(alias="<=1y")

    less_than_or_equal_to_five_minutes: str = FieldInfo(alias="<=5m")

    greater_than_one_year: str = FieldInfo(alias=">1y")


class SummaryResponseTTLResponse(BaseModel):
    meta: Meta

    summary_0: Summary0