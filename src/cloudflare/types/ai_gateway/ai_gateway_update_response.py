# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "AIGatewayUpdateResponse",
    "DLP",
    "DLPUnionMember0",
    "DLPUnionMember1",
    "DLPUnionMember1Policy",
    "Otel",
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


class Otel(BaseModel):
    authorization: str

    headers: Dict[str, str]

    url: str


class StripeUsageEvent(BaseModel):
    payload: str


class Stripe(BaseModel):
    authorization: str

    usage_events: List[StripeUsageEvent]


class AIGatewayUpdateResponse(BaseModel):
    id: str
    """gateway id"""

    account_id: str

    account_tag: str

    cache_invalidate_on_update: bool

    cache_ttl: Optional[int] = None

    collect_logs: bool

    created_at: datetime

    internal_id: str

    modified_at: datetime

    rate_limiting_interval: Optional[int] = None

    rate_limiting_limit: Optional[int] = None

    rate_limiting_technique: Literal["fixed", "sliding"]

    authentication: Optional[bool] = None

    dlp: Optional[DLP] = None

    log_management: Optional[int] = None

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]] = None

    logpush: Optional[bool] = None

    logpush_public_key: Optional[str] = None

    otel: Optional[List[Otel]] = None

    store_id: Optional[str] = None

    stripe: Optional[Stripe] = None
