# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "HTTPMethodGetResponse",
    "Meta",
    "MetaDateRange",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "Top0",
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
    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: str = FieldInfo(alias="lastUpdated")

    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)


class Top0(BaseModel):
    client_asn: int = FieldInfo(alias="clientASN")

    client_as_name: str = FieldInfo(alias="clientASName")

    value: str


class HTTPMethodGetResponse(BaseModel):
    meta: Meta

    top_0: List[Top0]
