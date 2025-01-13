# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["EveryoneRuleParam", "Everyone"]


class Everyone(TypedDict, total=False):
    pass


class EveryoneRuleParam(TypedDict, total=False):
    everyone: Required[Everyone]
    """An empty object which matches on all users."""
