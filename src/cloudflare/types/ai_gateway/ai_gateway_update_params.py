# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIGatewayUpdateParams", "DLP"]


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

    store_id: Optional[str]


class DLP(TypedDict, total=False):
    action: Required[Literal["BLOCK", "FLAG"]]

    enabled: Required[bool]

    profiles: Required[List[str]]
