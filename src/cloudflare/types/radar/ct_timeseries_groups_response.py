# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "CtTimeseriesGroupsResponse",
    "Meta",
    "MetaConfidenceInfo",
    "MetaConfidenceInfoAnnotation",
    "MetaDateRange",
    "MetaUnit",
    "Serie0",
    "Serie0UnnamedSchemaRef7826220e105d84352ba1108d9ed88e55",
    "Serie0UnionMember1",
    "Serie0UnionMember2",
    "Serie0UnionMember3",
    "Serie0UnionMember4",
    "Serie0UnionMember5",
    "Serie0UnionMember6",
    "Serie0UnionMember7",
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


class Serie0UnnamedSchemaRef7826220e105d84352ba1108d9ed88e55(BaseModel):
    timestamps: List[datetime]

    __pydantic_extra__: Dict[str, List[str]] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> List[str]: ...


class Serie0UnionMember1(BaseModel):
    rfc6962: List[str]

    static: List[str]


class Serie0UnionMember2(BaseModel):
    gt_121d: List[str]

    gt_16d_lte_31d: List[str]

    gt_31d_lte_91d: List[str]

    gt_3d_lte_16d: List[str]

    gt_91d_lte_121d: List[str]

    lte_3d: List[str]


class Serie0UnionMember3(BaseModel):
    certificate: List[str] = FieldInfo(alias="CERTIFICATE")

    precertificate: List[str] = FieldInfo(alias="PRECERTIFICATE")


class Serie0UnionMember4(BaseModel):
    expired: List[str] = FieldInfo(alias="EXPIRED")

    valid: List[str] = FieldInfo(alias="VALID")


class Serie0UnionMember5(BaseModel):
    negative: List[str] = FieldInfo(alias="NEGATIVE")

    positive: List[str] = FieldInfo(alias="POSITIVE")


class Serie0UnionMember6(BaseModel):
    dsa: List[str] = FieldInfo(alias="DSA")

    ecdsa: List[str] = FieldInfo(alias="ECDSA")

    rsa: List[str] = FieldInfo(alias="RSA")


class Serie0UnionMember7(BaseModel):
    domain: List[str]

    extended: List[str]

    organization: List[str]

    unknown: List[str]


Serie0: TypeAlias = Union[
    Serie0UnnamedSchemaRef7826220e105d84352ba1108d9ed88e55,
    Serie0UnionMember1,
    Serie0UnionMember2,
    Serie0UnionMember3,
    Serie0UnionMember4,
    Serie0UnionMember5,
    Serie0UnionMember6,
    Serie0UnionMember7,
]


class CtTimeseriesGroupsResponse(BaseModel):
    meta: Meta
    """Metadata for the results."""

    serie_0: Serie0
