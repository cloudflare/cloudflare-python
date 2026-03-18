# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIGatewayCreateParams"]


class AIGatewayCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """gateway id"""

    cache_invalidate_on_update: Required[bool]

    cache_ttl: Required[Optional[int]]

    collect_logs: Required[bool]

    rate_limiting_interval: Required[Optional[int]]

    rate_limiting_limit: Required[Optional[int]]

    authentication: bool

    log_management: Optional[int]

    log_management_strategy: Optional[Literal["STOP_INSERTING", "DELETE_OLDEST"]]

    logpush: bool

    logpush_public_key: Optional[str]

    rate_limiting_technique: Optional[Literal["fixed", "sliding"]]

    workers_ai_billing_mode: Literal["postpaid", "unified"]
    """Controls how Workers AI inference calls routed through this gateway are billed"""

    zdr: bool
