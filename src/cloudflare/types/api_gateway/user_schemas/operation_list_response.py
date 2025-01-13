# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "OperationListResponse",
    "APIShieldOperation",
    "APIShieldOperationFeatures",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureThresholds",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRouting",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervals",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfo",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo",
    "APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema",
    "APIShieldBasicOperation",
]


class APIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds(BaseModel):
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


class APIShieldOperationFeaturesAPIShieldOperationFeatureThresholds(BaseModel):
    thresholds: Optional[APIShieldOperationFeaturesAPIShieldOperationFeatureThresholdsThresholds] = None


class APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas(BaseModel):
    parameters: Optional[List[object]] = None
    """An array containing the learned parameter schemas."""

    responses: Optional[object] = None
    """An empty response object.

    This field is required to yield a valid operation schema.
    """


class APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas(BaseModel):
    last_updated: Optional[datetime] = None

    parameter_schemas: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas
    ] = None
    """An operation schema object containing a response."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas(BaseModel):
    parameter_schemas: APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas


class APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting(BaseModel):
    last_updated: Optional[datetime] = None

    route: Optional[str] = None
    """Target route."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRouting(BaseModel):
    api_routing: Optional[APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting] = None
    """API Routing settings on endpoint."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99(
    BaseModel
):
    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals(
    BaseModel
):
    p90: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90
    ] = None
    """Upper and lower bound for percentile estimate"""

    p95: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95
    ] = None
    """Upper and lower bound for percentile estimate"""

    p99: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99
    ] = None
    """Upper and lower bound for percentile estimate"""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold(
    BaseModel
):
    confidence_intervals: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals
    ] = None

    mean: Optional[float] = None
    """Suggested threshold."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals(BaseModel):
    last_updated: Optional[datetime] = None

    suggested_threshold: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold
    ] = None


class APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervals(BaseModel):
    confidence_intervals: Optional[
        APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals
    ] = None


class APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema(BaseModel):
    id: Optional[str] = None
    """UUID"""

    created_at: Optional[datetime] = None

    is_learned: Optional[bool] = None
    """True if schema is Cloudflare-provided."""

    name: Optional[str] = None
    """Schema file name."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo(BaseModel):
    active_schema: Optional[APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema] = None
    """Schema active on endpoint."""

    learned_available: Optional[bool] = None
    """True if a Cloudflare-provided learned schema is available for this endpoint."""

    mitigation_action: Optional[Literal["none", "log", "block"]] = None
    """Action taken on requests failing validation."""


class APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfo(BaseModel):
    schema_info: Optional[APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo] = None


APIShieldOperationFeatures: TypeAlias = Union[
    APIShieldOperationFeaturesAPIShieldOperationFeatureThresholds,
    APIShieldOperationFeaturesAPIShieldOperationFeatureParameterSchemas,
    APIShieldOperationFeaturesAPIShieldOperationFeatureAPIRouting,
    APIShieldOperationFeaturesAPIShieldOperationFeatureConfidenceIntervals,
    APIShieldOperationFeaturesAPIShieldOperationFeatureSchemaInfo,
]


class APIShieldOperation(BaseModel):
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

    features: Optional[APIShieldOperationFeatures] = None


class APIShieldBasicOperation(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""


OperationListResponse: TypeAlias = Union[APIShieldOperation, APIShieldBasicOperation]
