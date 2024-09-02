# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ....._models import BaseModel

from datetime import datetime

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

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

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")

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
    access_rules: List[str] = FieldInfo(alias="ACCESS_RULES")

    api_shield: List[str] = FieldInfo(alias="API_SHIELD")

    bot_management: List[str] = FieldInfo(alias="BOT_MANAGEMENT")

    data_loss_prevention: List[str] = FieldInfo(alias="DATA_LOSS_PREVENTION")

    ddos: List[str] = FieldInfo(alias="DDOS")

    ip_reputation: List[str] = FieldInfo(alias="IP_REPUTATION")

    timestamps: List[datetime]

    waf: List[str] = FieldInfo(alias="WAF")


class TimeseriesGroupGetResponse(BaseModel):
    meta: Meta

    serie_0: Serie0
