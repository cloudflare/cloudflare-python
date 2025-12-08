# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "BGPTimeseriesResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "Serie0",
]


class MetaConfidenceInfoAnnotation(BaseModel):
    """Annotation associated with the result (e.g. outage or other type of event)."""

    data_source: Literal[
        "ALL",
        "AI_BOTS",
        "AI_GATEWAY",
        "BGP",
        "BOTS",
        "CONNECTION_ANOMALY",
        "CT",
        "DNS",
        "DNS_MAGNITUDE",
        "DNS_AS112",
        "DOS",
        "EMAIL_ROUTING",
        "EMAIL_SECURITY",
        "FW",
        "FW_PG",
        "HTTP",
        "HTTP_CONTROL",
        "HTTP_CRAWLER_REFERER",
        "HTTP_ORIGINS",
        "IQI",
        "LEAKED_CREDENTIALS",
        "NET",
        "ROBOTS_TXT",
        "SPEED",
        "WORKERS_AI",
    ] = FieldInfo(alias="dataSource")
    """Data source for annotations."""

    description: str

    end_date: datetime = FieldInfo(alias="endDate")

    event_type: Literal["EVENT", "GENERAL", "OUTAGE", "PARTIAL_PROJECTION", "PIPELINE", "TRAFFIC_ANOMALY"] = FieldInfo(
        alias="eventType"
    )
    """Event type for annotations."""

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")
    """Whether event is a single point in time or a time range."""

    linked_url: str = FieldInfo(alias="linkedUrl")

    start_date: datetime = FieldInfo(alias="startDate")


class MetaConfidenceInfo(BaseModel):
    annotations: List[MetaConfidenceInfoAnnotation]

    level: int
    """Provides an indication of how much confidence Cloudflare has in the data."""


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class Meta(BaseModel):
    agg_interval: Literal["15m", "1h", "1d", "1w"] = FieldInfo(alias="aggInterval")

    confidence_info: MetaConfidenceInfo = FieldInfo(alias="confidenceInfo")

    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")


class Serie0(BaseModel):
    timestamps: List[datetime]

    values: List[str]


class BGPTimeseriesResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
