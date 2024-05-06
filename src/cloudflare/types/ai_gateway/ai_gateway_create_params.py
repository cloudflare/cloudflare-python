# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AIGatewayCreateParams"]


class AIGatewayCreateParams(TypedDict, total=False):
    account_id: Required[str]

    cache_invalidate_on_update: Required[bool]

    cache_ttl: Required[int]

    collect_logs: Required[bool]

    name: Required[str]

    slug: Required[str]

    rate_limiting_interval: int

    rate_limiting_limit: int

    rate_limiting_technique: str
