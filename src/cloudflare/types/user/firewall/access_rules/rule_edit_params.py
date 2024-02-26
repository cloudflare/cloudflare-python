# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RuleEditParams"]


class RuleEditParams(TypedDict, total=False):
    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    notes: str
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """
