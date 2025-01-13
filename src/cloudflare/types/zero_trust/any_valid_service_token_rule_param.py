# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AnyValidServiceTokenRuleParam", "AnyValidServiceToken"]


class AnyValidServiceToken(TypedDict, total=False):
    pass


class AnyValidServiceTokenRuleParam(TypedDict, total=False):
    any_valid_service_token: Required[AnyValidServiceToken]
    """An empty object which matches on all service tokens."""
