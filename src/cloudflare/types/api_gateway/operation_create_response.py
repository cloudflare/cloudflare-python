# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OperationCreateResponse",
    "Features",
    "FeaturesAPIShieldOperationFeatureThresholds",
    "FeaturesAPIShieldOperationFeatureThresholdsThresholds",
    "FeaturesAPIShieldOperationFeatureParameterSchemas",
    "FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas",
    "FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas",
    "FeaturesAPIShieldOperationFeatureAPIRouting",
    "FeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervals",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95",
    "FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99",
    "FeaturesAPIShieldOperationFeatureSchemaInfo",
    "FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo",
    "FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema",
    "Schemas",
    "SchemasLearned",
    "SchemasUploaded",
]


class FeaturesAPIShieldOperationFeatureThresholdsThresholds(BaseModel):
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


class FeaturesAPIShieldOperationFeatureThresholds(BaseModel):
    thresholds: Optional[FeaturesAPIShieldOperationFeatureThresholdsThresholds] = None


class FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas(BaseModel):
    """An operation schema object containing a response."""

    parameters: Optional[List[object]] = None
    """An array containing the learned parameter schemas."""

    responses: Optional[object] = None
    """An empty response object.

    This field is required to yield a valid operation schema.
    """


class FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas(BaseModel):
    last_updated: Optional[datetime] = None

    parameter_schemas: Optional[FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemasParameterSchemas] = (
        None
    )
    """An operation schema object containing a response."""


class FeaturesAPIShieldOperationFeatureParameterSchemas(BaseModel):
    parameter_schemas: FeaturesAPIShieldOperationFeatureParameterSchemasParameterSchemas


class FeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting(BaseModel):
    """API Routing settings on endpoint."""

    last_updated: Optional[datetime] = None

    route: Optional[str] = None
    """Target route."""


class FeaturesAPIShieldOperationFeatureAPIRouting(BaseModel):
    api_routing: Optional[FeaturesAPIShieldOperationFeatureAPIRoutingAPIRouting] = None
    """API Routing settings on endpoint."""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90(
    BaseModel
):
    """Upper and lower bound for percentile estimate"""

    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95(
    BaseModel
):
    """Upper and lower bound for percentile estimate"""

    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99(
    BaseModel
):
    """Upper and lower bound for percentile estimate"""

    lower: Optional[float] = None
    """Lower bound for percentile estimate"""

    upper: Optional[float] = None
    """Upper bound for percentile estimate"""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals(
    BaseModel
):
    p90: Optional[
        FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP90
    ] = None
    """Upper and lower bound for percentile estimate"""

    p95: Optional[
        FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP95
    ] = None
    """Upper and lower bound for percentile estimate"""

    p99: Optional[
        FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervalsP99
    ] = None
    """Upper and lower bound for percentile estimate"""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold(BaseModel):
    confidence_intervals: Optional[
        FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThresholdConfidenceIntervals
    ] = None

    mean: Optional[float] = None
    """Suggested threshold."""


class FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals(BaseModel):
    last_updated: Optional[datetime] = None

    suggested_threshold: Optional[
        FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervalsSuggestedThreshold
    ] = None


class FeaturesAPIShieldOperationFeatureConfidenceIntervals(BaseModel):
    confidence_intervals: Optional[FeaturesAPIShieldOperationFeatureConfidenceIntervalsConfidenceIntervals] = None


class FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema(BaseModel):
    """Schema active on endpoint."""

    id: Optional[str] = None
    """UUID."""

    created_at: Optional[datetime] = None

    is_learned: Optional[bool] = None
    """True if schema is Cloudflare-provided."""

    name: Optional[str] = None
    """Schema file name."""


class FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo(BaseModel):
    active_schema: Optional[FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfoActiveSchema] = None
    """Schema active on endpoint."""

    learned_available: Optional[bool] = None
    """True if a Cloudflare-provided learned schema is available for this endpoint."""

    mitigation_action: Optional[Literal["none", "log", "block"]] = None
    """Action taken on requests failing validation."""


class FeaturesAPIShieldOperationFeatureSchemaInfo(BaseModel):
    schema_info: Optional[FeaturesAPIShieldOperationFeatureSchemaInfoSchemaInfo] = None


Features: TypeAlias = Union[
    FeaturesAPIShieldOperationFeatureThresholds,
    FeaturesAPIShieldOperationFeatureParameterSchemas,
    FeaturesAPIShieldOperationFeatureAPIRouting,
    FeaturesAPIShieldOperationFeatureConfidenceIntervals,
    FeaturesAPIShieldOperationFeatureSchemaInfo,
]


class SchemasLearned(BaseModel):
    """
    An OpenAPI operation object fragment containing schema information for an operation. May include parameter definitions, request body specifications, and a component schema extension.
    """

    parameters: Optional[List[Dict[str, object]]] = None
    """OpenAPI parameter objects describing path, query, header, or cookie parameters."""

    request_body: Optional[Dict[str, object]] = FieldInfo(alias="requestBody", default=None)
    """OpenAPI request body object describing the expected request payload."""


class SchemasUploaded(BaseModel):
    """
    An OpenAPI operation object fragment containing schema information for an operation. May include parameter definitions, request body specifications, and a component schema extension.
    """

    parameters: Optional[List[Dict[str, object]]] = None
    """OpenAPI parameter objects describing path, query, header, or cookie parameters."""

    request_body: Optional[Dict[str, object]] = FieldInfo(alias="requestBody", default=None)
    """OpenAPI request body object describing the expected request payload."""


class Schemas(BaseModel):
    """
    OpenAPI JSON schemas for an operation, including both user-uploaded and Cloudflare-learned schemas.
    """

    learned: Optional[SchemasLearned] = None
    """
    An OpenAPI operation object fragment containing schema information for an
    operation. May include parameter definitions, request body specifications, and a
    component schema extension.
    """

    uploaded: Optional[SchemasUploaded] = None
    """
    An OpenAPI operation object fragment containing schema information for an
    operation. May include parameter definitions, request body specifications, and a
    component schema extension.
    """


class OperationCreateResponse(BaseModel):
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
    """UUID."""

    features: Optional[Features] = None

    schemas: Optional[Schemas] = None
    """
    OpenAPI JSON schemas for an operation, including both user-uploaded and
    Cloudflare-learned schemas.
    """
