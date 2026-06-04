# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "AIGatewayUpdateParams",
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


class AIGatewayUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    cache_invalidate_on_update: Required[bool]

    cache_ttl: Required[Optional[int]]

    collect_logs: Required[bool]

    rate_limiting_interval: Required[Optional[int]]

    rate_limiting_limit: Required[Optional[int]]

    authentication: bool

    dlp: DLP

    guardrails: Optional[Guardrails]

    log_management: Optional[int]

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]]

    logpush: bool

    logpush_public_key: Optional[str]

    otel: Optional[Iterable[Otel]]

    rate_limiting_technique: Optional[Literal["fixed", "sliding"]]

    retry_backoff: Optional[Literal["constant", "linear", "exponential"]]
    """Backoff strategy for retry delays"""

    retry_delay: Optional[int]
    """Delay between retry attempts in milliseconds (0-5000)"""

    retry_max_attempts: Optional[int]
    """Maximum number of retry attempts for failed requests (1-5)"""

    spend_limits: Optional[SpendLimits]

    store_id: Optional[str]

    stripe: Optional[Stripe]

    workers_ai_billing_mode: Literal["postpaid"]
    """Controls how Workers AI inference calls routed through this gateway are billed.

    Only 'postpaid' is currently supported.
    """

    zdr: bool


class DLPUnionMember0(TypedDict, total=False):
    action: Required[Literal["BLOCK", "FLAG"]]

    enabled: Required[bool]

    profiles: Required[SequenceNotStr[str]]


class DLPUnionMember1Policy(TypedDict, total=False):
    id: Required[str]

    action: Required[Literal["FLAG", "BLOCK"]]

    check: Required[List[Literal["REQUEST", "RESPONSE"]]]

    enabled: Required[bool]

    profiles: Required[SequenceNotStr[str]]


class DLPUnionMember1(TypedDict, total=False):
    enabled: Required[bool]

    policies: Required[Iterable[DLPUnionMember1Policy]]


DLP: TypeAlias = Union[DLPUnionMember0, DLPUnionMember1]


class GuardrailsPrompt(TypedDict, total=False):
    p1: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="P1")]

    s1: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S1")]

    s10: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S10")]

    s11: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S11")]

    s12: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S12")]

    s13: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S13")]

    s2: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S2")]

    s3: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S3")]

    s4: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S4")]

    s5: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S5")]

    s6: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S6")]

    s7: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S7")]

    s8: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S8")]

    s9: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S9")]


class GuardrailsResponse(TypedDict, total=False):
    p1: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="P1")]

    s1: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S1")]

    s10: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S10")]

    s11: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S11")]

    s12: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S12")]

    s13: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S13")]

    s2: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S2")]

    s3: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S3")]

    s4: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S4")]

    s5: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S5")]

    s6: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S6")]

    s7: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S7")]

    s8: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S8")]

    s9: Annotated[Literal["FLAG", "BLOCK"], PropertyInfo(alias="S9")]


class Guardrails(TypedDict, total=False):
    prompt: Required[GuardrailsPrompt]

    response: Required[GuardrailsResponse]


class Otel(TypedDict, total=False):
    headers: Required[Dict[str, str]]

    url: Required[str]

    authorization: str

    content_type: Literal["json", "protobuf"]


class SpendLimitsRuleMetadataMode(TypedDict, total=False):
    mode: Required[Literal["partition"]]


class SpendLimitsRuleMetadataUnionMember1(TypedDict, total=False):
    mode: Required[Literal["match"]]

    value: Required[str]


SpendLimitsRuleMetadata: TypeAlias = Union[SpendLimitsRuleMetadataMode, SpendLimitsRuleMetadataUnionMember1]


class SpendLimitsRuleModelMatch(TypedDict, total=False):
    match: Required[str]


SpendLimitsRuleModel: TypeAlias = Union[Literal["partition"], SpendLimitsRuleModelMatch]


class SpendLimitsRuleProviderMatch(TypedDict, total=False):
    match: Required[str]


SpendLimitsRuleProvider: TypeAlias = Union[Literal["partition"], SpendLimitsRuleProviderMatch]


class SpendLimitsRule(TypedDict, total=False):
    id: Required[str]

    limit: Required[float]

    limit_type: Required[Annotated[Literal["cost"], PropertyInfo(alias="limitType")]]

    window: Required[int]

    enabled: bool

    metadata: Dict[str, SpendLimitsRuleMetadata]

    model: SpendLimitsRuleModel

    provider: SpendLimitsRuleProvider

    technique: Literal["fixed", "sliding"]


class SpendLimits(TypedDict, total=False):
    enabled: bool

    rules: Iterable[SpendLimitsRule]


class StripeUsageEvent(TypedDict, total=False):
    payload: Required[str]


class Stripe(TypedDict, total=False):
    authorization: Required[str]

    usage_events: Required[Iterable[StripeUsageEvent]]
