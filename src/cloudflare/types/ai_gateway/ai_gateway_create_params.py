# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["AIGatewayCreateParams"]


class AIGatewayCreateParams(TypedDict, total=False):
    account_id: str

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

    retry_backoff: Optional[Literal["constant", "linear", "exponential"]]
    """Backoff strategy for retry delays"""

    retry_delay: Optional[int]
    """Delay between retry attempts in milliseconds (0-5000)"""

    retry_max_attempts: Optional[int]
    """Maximum number of retry attempts for failed requests (1-5)"""

    workers_ai_billing_mode: Literal["postpaid"]
    """Controls how Workers AI inference calls routed through this gateway are billed.

    Only 'postpaid' is currently supported.
    """

    zdr: bool
