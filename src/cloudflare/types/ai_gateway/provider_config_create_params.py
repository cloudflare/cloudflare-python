# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ProviderConfigCreateParams"]


class ProviderConfigCreateParams(TypedDict, total=False):
    account_id: Required[str]

    alias: Required[str]

    default_config: Required[bool]

    provider_slug: Required[str]

    secret: Required[str]

    secret_id: Required[str]

    rate_limit: float

    rate_limit_period: float
