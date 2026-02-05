# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CtSummaryResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Summary0",
    "Summary0UnionMember1",
    "Summary0UnionMember2",
    "Summary0UnionMember3",
    "Summary0UnionMember4",
    "Summary0UnionMember5",
    "Summary0UnionMember6",
    "Summary0UnionMember7",
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


class MetaUnit(BaseModel):
    name: str

    value: str


class Meta(BaseModel):
    """Metadata for the results."""

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


class Summary0UnionMember1(BaseModel):
    rfc6962: str

    static: str


class Summary0UnionMember2(BaseModel):
    gt_121d: str

    gt_16d_lte_31d: str

    gt_31d_lte_91d: str

    gt_3d_lte_16d: str

    gt_91d_lte_121d: str

    lte_3d: str


class Summary0UnionMember3(BaseModel):
    certificate: str = FieldInfo(alias="CERTIFICATE")

    precertificate: str = FieldInfo(alias="PRECERTIFICATE")


class Summary0UnionMember4(BaseModel):
    expired: str = FieldInfo(alias="EXPIRED")

    valid: str = FieldInfo(alias="VALID")


class Summary0UnionMember5(BaseModel):
    negative: str = FieldInfo(alias="NEGATIVE")

    positive: str = FieldInfo(alias="POSITIVE")


class Summary0UnionMember6(BaseModel):
    dsa: str = FieldInfo(alias="DSA")

    ecdsa: str = FieldInfo(alias="ECDSA")

    rsa: str = FieldInfo(alias="RSA")


class Summary0UnionMember7(BaseModel):
    domain: str

    extended: str

    organization: str

    unknown: str


Summary0: TypeAlias = Union[
    Dict[str, str],
    Summary0UnionMember1,
    Summary0UnionMember2,
    Summary0UnionMember3,
    Summary0UnionMember4,
    Summary0UnionMember5,
    Summary0UnionMember6,
    Summary0UnionMember7,
]


class CtSummaryResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    summary_0: Summary0
