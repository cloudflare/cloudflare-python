# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "SummaryDurationResponse",
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
    one_hour_to_three_hours: str = FieldInfo(alias="_1_HOUR_TO_3_HOURS")

    ten_mins_to_twenty_mins: str = FieldInfo(alias="_10_MINS_TO_20_MINS")

    twenty_mins_to_forty_mins: str = FieldInfo(alias="_20_MINS_TO_40_MINS")

    forty_mins_to_one_hour: str = FieldInfo(alias="_40_MINS_TO_1_HOUR")

    over_3_hours: str = FieldInfo(alias="OVER_3_HOURS")

    under_10_mins: str = FieldInfo(alias="UNDER_10_MINS")


class SummaryDurationResponse(BaseModel):
    meta: Meta

    summary_0: Summary0
