# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel
from ...radar_email_series import RadarEmailSeries

__all__ = [
    "TimeseriesGroupSPFResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
]


class MetaConfidenceInfoAnnotation(BaseModel):
    data_source: str = FieldInfo(alias="dataSource")

    description: str

    end_date: datetime = FieldInfo(alias="endDate")

    event_type: str = FieldInfo(alias="eventType")

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
        "RATIO",
    ]
    """Normalization method applied to the results.

    Refer to
    [Normalization methods](https://developers.cloudflare.com/radar/concepts/normalization/).
    """

    units: List[MetaUnit]
    """Measurement units for the results."""


class TimeseriesGroupSPFResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    serie_0: RadarEmailSeries
