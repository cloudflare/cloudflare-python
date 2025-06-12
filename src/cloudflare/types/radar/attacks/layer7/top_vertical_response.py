# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = [
    "TopVerticalResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Top0",
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


class Top0(BaseModel):
    name: str

    value: str


class TopVerticalResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    top_0: List[Top0]
