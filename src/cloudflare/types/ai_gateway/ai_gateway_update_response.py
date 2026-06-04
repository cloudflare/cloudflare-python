# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "AIGatewayUpdateResponse",
    "DLP",
    "DLPUnionMember0",
    "DLPUnionMember1",
    "DLPUnionMember1Policy",
    "Guardrails",
    "GuardrailsPrompt",
    "GuardrailsResponse",
    "Otel",
    "SpendLimits",
    "SpendLimitsRule",
    "SpendLimitsRuleMetadata",
    "SpendLimitsRuleMetadataMode",
    "SpendLimitsRuleMetadataUnionMember1",
    "SpendLimitsRuleModel",
    "SpendLimitsRuleModelMatch",
    "SpendLimitsRuleProvider",
    "SpendLimitsRuleProviderMatch",
    "Stripe",
    "StripeUsageEvent",
]


class DLPUnionMember0(BaseModel):
    action: Literal["BLOCK", "FLAG"]

    enabled: bool

    profiles: List[str]


class DLPUnionMember1Policy(BaseModel):
    id: str

    action: Literal["FLAG", "BLOCK"]

    check: List[Literal["REQUEST", "RESPONSE"]]

    enabled: bool

    profiles: List[str]


class DLPUnionMember1(BaseModel):
    enabled: bool

    policies: List[DLPUnionMember1Policy]


DLP: TypeAlias = Union[DLPUnionMember0, DLPUnionMember1]


class GuardrailsPrompt(BaseModel):
    p1: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="P1", default=None)

    s1: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S1", default=None)

    s10: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S10", default=None)

    s11: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S11", default=None)

    s12: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S12", default=None)

    s13: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S13", default=None)

    s2: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S2", default=None)

    s3: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S3", default=None)

    s4: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S4", default=None)

    s5: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S5", default=None)

    s6: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S6", default=None)

    s7: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S7", default=None)

    s8: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S8", default=None)

    s9: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S9", default=None)


class GuardrailsResponse(BaseModel):
    p1: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="P1", default=None)

    s1: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S1", default=None)

    s10: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S10", default=None)

    s11: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S11", default=None)

    s12: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S12", default=None)

    s13: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S13", default=None)

    s2: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S2", default=None)

    s3: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S3", default=None)

    s4: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S4", default=None)

    s5: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S5", default=None)

    s6: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S6", default=None)

    s7: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S7", default=None)

    s8: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S8", default=None)

    s9: Optional[Literal["FLAG", "BLOCK"]] = FieldInfo(alias="S9", default=None)


class Guardrails(BaseModel):
    prompt: GuardrailsPrompt

    response: GuardrailsResponse


class Otel(BaseModel):
    headers: Dict[str, str]

    url: str

    authorization: Optional[str] = None

    content_type: Optional[Literal["json", "protobuf"]] = None


class SpendLimitsRuleMetadataMode(BaseModel):
    mode: Literal["partition"]


class SpendLimitsRuleMetadataUnionMember1(BaseModel):
    mode: Literal["match"]

    value: str


SpendLimitsRuleMetadata: TypeAlias = Union[SpendLimitsRuleMetadataMode, SpendLimitsRuleMetadataUnionMember1]


class SpendLimitsRuleModelMatch(BaseModel):
    match: str


SpendLimitsRuleModel: TypeAlias = Union[Literal["partition"], SpendLimitsRuleModelMatch]


class SpendLimitsRuleProviderMatch(BaseModel):
    match: str


SpendLimitsRuleProvider: TypeAlias = Union[Literal["partition"], SpendLimitsRuleProviderMatch]


class SpendLimitsRule(BaseModel):
    id: str

    limit: float

    limit_type: Literal["cost"] = FieldInfo(alias="limitType")

    window: int

    enabled: Optional[bool] = None

    metadata: Optional[Dict[str, SpendLimitsRuleMetadata]] = None

    model: Optional[SpendLimitsRuleModel] = None

    provider: Optional[SpendLimitsRuleProvider] = None

    technique: Optional[Literal["fixed", "sliding"]] = None


class SpendLimits(BaseModel):
    enabled: Optional[bool] = None

    rules: Optional[List[SpendLimitsRule]] = None


class StripeUsageEvent(BaseModel):
    payload: str


class Stripe(BaseModel):
    authorization: str

    usage_events: List[StripeUsageEvent]


class AIGatewayUpdateResponse(BaseModel):
    id: str
    """gateway id"""

    cache_invalidate_on_update: bool

    cache_ttl: Optional[int] = None

    collect_logs: bool

    created_at: datetime

    modified_at: datetime

    rate_limiting_interval: Optional[int] = None

    rate_limiting_limit: Optional[int] = None

    authentication: Optional[bool] = None

    dlp: Optional[DLP] = None

    guardrails: Optional[Guardrails] = None

    is_default: Optional[bool] = None

    log_management: Optional[int] = None

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] = None

    logpush: Optional[bool] = None

    logpush_public_key: Optional[str] = None

    otel: Optional[List[Otel]] = None

    rate_limiting_technique: Optional[Literal["fixed", "sliding"]] = None

    retry_backoff: Optional[Literal["constant", "linear", "exponential"]] = None
    """Backoff strategy for retry delays"""

    retry_delay: Optional[int] = None
    """Delay between retry attempts in milliseconds (0-5000)"""

    retry_max_attempts: Optional[int] = None
    """Maximum number of retry attempts for failed requests (1-5)"""

    spend_limits: Optional[SpendLimits] = None

    store_id: Optional[str] = None

    stripe: Optional[Stripe] = None

    workers_ai_billing_mode: Optional[Literal["postpaid"]] = None
    """Controls how Workers AI inference calls routed through this gateway are billed.

    Only 'postpaid' is currently supported.
    """

    zdr: Optional[bool] = None
