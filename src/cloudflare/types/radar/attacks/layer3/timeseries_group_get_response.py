# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "TimeseriesGroupGetResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Serie0",
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

    is_instantaneous: object = FieldInfo(alias="isInstantaneous")

    end_time: Optional[datetime] = FieldInfo(alias="endTime", default=None)

    linked_url: Optional[str] = FieldInfo(alias="linkedUrl", default=None)

    start_time: Optional[datetime] = FieldInfo(alias="startTime", default=None)


class MetaConfidenceInfo(BaseModel):
    annotations: Optional[List[MetaConfidenceInfoAnnotation]] = None

    level: Optional[int] = None


class Meta(BaseModel):
    agg_interval: str = FieldInfo(alias="aggInterval")

    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Serie0(BaseModel):
    gre: List[str]

    icmp: List[str]

    tcp: List[str]

    timestamps: List[str]

    udp: List[str]


class TimeseriesGroupGetResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
