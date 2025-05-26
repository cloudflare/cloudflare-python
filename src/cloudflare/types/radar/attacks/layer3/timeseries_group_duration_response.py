# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "TimeseriesGroupDurationResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Serie0",
]


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    end_time: datetime = FieldInfo(alias="endTime")

    event_type: str = FieldInfo(alias="eventType")

    is_instantaneous: bool = FieldInfo(alias="isInstantaneous")
    """Whether event is a single point in time or a time range."""

    linked_url: str = FieldInfo(alias="linkedUrl")

    start_time: datetime = FieldInfo(alias="startTime")


class MetaConfidenceInfo(BaseModel):
    annotations: List[MetaConfidenceInfoAnnotation]

    level: int
    """Provides an indication of how much confidence Cloudflare has in the data."""


class MetaDateRange(BaseModel):
    end_time: datetime = FieldInfo(alias="endTime")
    """Adjusted end of date range."""

    start_time: datetime = FieldInfo(alias="startTime")
    """Adjusted start of date range."""


class MetaUnit(BaseModel):
    name: str

    value: str


class Meta(BaseModel):
    agg_interval: Literal["FIFTEEN_MINUTES", "ONE_HOUR", "ONE_DAY", "ONE_WEEK", "ONE_MONTH"] = FieldInfo(
        alias="aggInterval"
    )
    """Aggregation interval of the results (e.g., in 15 minutes or 1 hour intervals).

    Refer to
    [Aggregation intervals](https://developers.cloudflare.com/radar/concepts/aggregation-intervals/).
    """

    confidence_info: MetaConfidenceInfo = FieldInfo(alias="confidenceInfo")

    date_range: List[MetaDateRange] = FieldInfo(alias="dateRange")

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp of the last dataset update."""

    normalization: Literal[
        "PERCENTAGE",
        "MIN0_MAX",
        "MIN_MAX",
        "RAW_VALUES",
        "PERCENTAGE_CHANGE",
        "ROLLING_AVERAGE",
        "OVERLAPPED_PERCENTAGE",
    ]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    units: List[MetaUnit]
    """Measurement units for the results."""


class Serie0(BaseModel):
    one_hour_to_three_hours: List[str] = FieldInfo(alias="_1_HOUR_TO_3_HOURS")

    ten_mins_to_twenty_mins: List[str] = FieldInfo(alias="_10_MINS_TO_20_MINS")

    twenty_mins_to_forty_mins: List[str] = FieldInfo(alias="_20_MINS_TO_40_MINS")

    forty_mins_to_one_hour: List[str] = FieldInfo(alias="_40_MINS_TO_1_HOUR")

    over_3_hours: List[str] = FieldInfo(alias="OVER_3_HOURS")

    timestamps: List[datetime]

    under_10_mins: List[str] = FieldInfo(alias="UNDER_10_MINS")


class TimeseriesGroupDurationResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    serie_0: Serie0
