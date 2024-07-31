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

    improved_logs: Required[bool]

    logpush: Required[bool]

    rate_limiting_interval: Required[Optional[int]]

    rate_limiting_limit: Required[Optional[int]]

    rate_limiting_technique: Required[Literal["fixed", "sliding"]]

    logpush_public_key: str
