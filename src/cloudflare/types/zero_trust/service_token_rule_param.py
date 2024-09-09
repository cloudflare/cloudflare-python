# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ServiceTokenRuleParam", "ServiceToken"]


class ServiceToken(TypedDict, total=False):
    token_id: Required[str]
    """The ID of a Service Token."""


class ServiceTokenRuleParam(TypedDict, total=False):
    service_token: Required[ServiceToken]
