# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "OperationBulkCreateResponse",
    "OperationBulkCreateResponseItem",
    "OperationBulkCreateResponseItemFeatures",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo",
    "OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema",
]


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds(BaseModel):
    auth_id_tokens: Optional[int] = None
    """The total number of auth-ids seen across this calculation."""

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


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds(BaseModel):
    thresholds: Optional[OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholdsThresholds] = None


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas(
    BaseModel
):
    parameters: Optional[List[object]] = None
    """An array containing the learned parameter schemas."""

    responses: Optional[object] = None
    """An empty response object.

    This field is required to yield a valid operation schema.
    """


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas(BaseModel):
    last_updated: Optional[datetime] = None

    parameter_schemas: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas
    ] = None
    """An operation schema object containing a response."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas(BaseModel):
    parameter_schemas: OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting(BaseModel):
    last_updated: Optional[datetime] = None

    route: Optional[str] = None
    """Target route."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting(BaseModel):
    api_routing: Optional[OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting] = None
    """API Routing settings on endpoint."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals(
    BaseModel
):
    p90: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90
    ] = None
    """Upper and lower bound for percentile estimate"""

    p95: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95
    ] = None
    """Upper and lower bound for percentile estimate"""

    p99: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99
    ] = None
    """Upper and lower bound for percentile estimate"""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold(
    BaseModel
):
    confidence_intervals: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals
    ] = None

    mean: Optional[float] = None
    """Suggested threshold."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals(BaseModel):
    last_updated: Optional[datetime] = None

    suggested_threshold: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold
    ] = None


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals(BaseModel):
    confidence_intervals: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals
    ] = None


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    is_learned: Optional[bool] = None
    """True if schema is Cloudflare-provided."""

    name: Optional[str] = None
    """Schema file name."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo(BaseModel):
    active_schema: Optional[
        OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema
    ] = None
    """Schema active on endpoint."""

    learned_available: Optional[bool] = None
    """True if a Cloudflare-provided learned schema is available for this endpoint."""

    mitigation_action: Optional[Literal["none", "log", "block"]] = None
    """Action taken on requests failing validation."""


class OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo(BaseModel):
    schema_info: Optional[OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo] = None


OperationBulkCreateResponseItemFeatures: TypeAlias = Union[
    OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureThresholds,
    OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureParameterSchemas,
    OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureAPIRouting,
    OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureConfidenceIntervals,
    OperationBulkCreateResponseItemFeaturesAPIShieldOperationFeatureSchemaInfo,
]


class OperationBulkCreateResponseItem(BaseModel):
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

    features: Optional[OperationBulkCreateResponseItemFeatures] = None


OperationBulkCreateResponse: TypeAlias = List[OperationBulkCreateResponseItem]
