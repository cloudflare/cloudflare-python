# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "TimeseriesGroupResponseCodesResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Serie0",
]


class MetaConfidenceInfoAnnotation(BaseModel):
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


class Serie0(BaseModel):
    timestamps: List[datetime]

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, List[str]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[str]: ...
    else:
        __pydantic_extra__: Dict[str, List[str]]


class TimeseriesGroupResponseCodesResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    serie_0: Serie0
