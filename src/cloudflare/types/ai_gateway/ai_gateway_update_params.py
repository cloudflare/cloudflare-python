# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "AIGatewayUpdateParams",
    "DLP",
    "DLPUnionMember0",
    "DLPUnionMember1",
    "DLPUnionMember1Policy",
    "Otel",
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

    rate_limiting_technique: Required[Literal["fixed", "sliding"]]

    authentication: bool

    dlp: DLP

    log_management: Optional[int]

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]]

    logpush: bool

    logpush_public_key: Optional[str]

    otel: Optional[Iterable[Otel]]

    store_id: Optional[str]

    stripe: Optional[Stripe]


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


class Otel(TypedDict, total=False):
    authorization: Required[str]

    headers: Required[Dict[str, str]]

    url: Required[str]


class StripeUsageEvent(TypedDict, total=False):
    payload: Required[str]


class Stripe(TypedDict, total=False):
    authorization: Required[str]

    usage_events: Required[Iterable[StripeUsageEvent]]
