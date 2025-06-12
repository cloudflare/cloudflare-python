# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "SummaryDurationResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Summary0",
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
    confidence_info: Optional[MetaConfidenceInfo] = FieldInfo(alias="confidenceInfo", default=None)

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


class Summary0(BaseModel):
    one_hour_to_three_hours: str = FieldInfo(alias="_1_HOUR_TO_3_HOURS")
    """A numeric string."""

    ten_mins_to_twenty_mins: str = FieldInfo(alias="_10_MINS_TO_20_MINS")
    """A numeric string."""

    twenty_mins_to_forty_mins: str = FieldInfo(alias="_20_MINS_TO_40_MINS")
    """A numeric string."""

    forty_mins_to_one_hour: str = FieldInfo(alias="_40_MINS_TO_1_HOUR")
    """A numeric string."""

    over_3_hours: str = FieldInfo(alias="OVER_3_HOURS")
    """A numeric string."""

    under_10_mins: str = FieldInfo(alias="UNDER_10_MINS")
    """A numeric string."""


class SummaryDurationResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    summary_0: Summary0
