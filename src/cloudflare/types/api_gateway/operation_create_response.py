# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "OperationCreateResponse",
    "OperationCreateResponseItem",
    "OperationCreateResponseItemFeatures",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo",
    "OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema",
]


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds(BaseModel):
    auth_id_tokens: Optional[int] = None
    """The total number of auth-ids seen across this calculation foo."""

    data_points: Optional[int] = None
    """The number of data points used for the threshold suggestion calculation."""

    last_updated: Optional[datetime] = None

    p50: Optional[int] = None
    """The p50 quantile of requests (in period_seconds)."""

    p90: Optional[int] = None
    """The p90 quantile of requests (in period_seconds)."""

    p99: Optional[int] = None
    """The p99 quantile of requests (in period_seconds)."""

    period_seconds: Optional[int] = None
    """The period over which this threshold is suggested."""

    requests: Optional[int] = None
    """The estimated number of requests covered by these calculations."""

    suggested_threshold: Optional[int] = None
    """The suggested threshold in requests done by the same auth_id or period_seconds."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds(BaseModel):
    thresholds: Optional[OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds] = None


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas(
    BaseModel
):
    parameters: Optional[List[object]] = None
    """An array containing the learned parameter schemas."""

    responses: Optional[object] = None
    """An empty response object.

    This field is required to yield a valid operation schema.
    """


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas(BaseModel):
    last_updated: Optional[datetime] = None

    parameter_schemas: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas
    ] = None
    """An operation schema object containing a response."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas(BaseModel):
    parameter_schemas: OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting(BaseModel):
    last_updated: Optional[datetime] = None

    route: Optional[str] = None
    """Target route."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting(BaseModel):
    api_routing: Optional[OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting] = None
    """API Routing settings on endpoint."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals(
    BaseModel
):
    p90: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90
    ] = None
    """Upper and lower bound for percentile estimate"""

    p95: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95
    ] = None
    """Upper and lower bound for percentile estimate"""

    p99: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99
    ] = None
    """Upper and lower bound for percentile estimate"""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold(
    BaseModel
):
    confidence_intervals: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals
    ] = None

    mean: Optional[float] = None
    """Suggested threshold."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals(BaseModel):
    last_updated: Optional[datetime] = None

    suggested_threshold: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold
    ] = None


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals(BaseModel):
    confidence_intervals: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals
    ] = None


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    is_learned: Optional[bool] = None
    """True if schema is Cloudflare-provided."""

    name: Optional[str] = None
    """Schema file name."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo(BaseModel):
    active_schema: Optional[
        OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema
    ] = None
    """Schema active on endpoint."""

    learned_available: Optional[bool] = None
    """True if a Cloudflare-provided learned schema is available for this endpoint."""

    mitigation_action: Optional[Literal["none", "log", "block"]] = None
    """Action taken on requests failing validation."""


class OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo(BaseModel):
    schema_info: Optional[OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo] = None


OperationCreateResponseItemFeatures: TypeAlias = Union[
    OperationCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds,
    OperationCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas,
    OperationCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting,
    OperationCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals,
    OperationCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo,
]


class OperationCreateResponseItem(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    last_updated: datetime

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""

    operation_id: str
    """UUID"""

    features: Optional[OperationCreateResponseItemFeatures] = None


OperationCreateResponse: TypeAlias = List[OperationCreateResponseItem]
