# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

__all__ = ["EveryoneRuleParam"]


class EveryoneRuleParam(TypedDict, total=False):
    everyone: Required[object]
    """An empty object which matches on all users."""
