# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["AnyValidServiceTokenRuleParam"]


class AnyValidServiceTokenRuleParam(TypedDict, total=False):
    any_valid_service_token: Required[object]
    """An empty object which matches on all service tokens."""
