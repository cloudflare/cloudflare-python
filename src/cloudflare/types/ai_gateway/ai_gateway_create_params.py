# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AIGatewayCreateParams"]


class AIGatewayCreateParams(TypedDict, total=False):
    account_id: Required[str]

    id: Required[str]
    """gateway slug"""

    cache_invalidate_on_update: Required[bool]

    cache_ttl: Required[int]

    collect_logs: Required[bool]

    rate_limiting_interval: int

    rate_limiting_limit: int

    rate_limiting_technique: str
