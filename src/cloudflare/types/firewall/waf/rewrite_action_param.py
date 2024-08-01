# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["RewriteActionParam"]


class RewriteActionParam(TypedDict, total=False):
    block: Literal["challenge", "block", "simulate", "disable", "default"]
    """The WAF rule action to apply."""

    challenge: Literal["challenge", "block", "simulate", "disable", "default"]
    """The WAF rule action to apply."""

    default: Literal["challenge", "block", "simulate", "disable", "default"]
    """The WAF rule action to apply."""

    disable: Literal["challenge", "block", "simulate", "disable", "default"]
    """The WAF rule action to apply."""

    simulate: Literal["challenge", "block", "simulate", "disable", "default"]
    """The WAF rule action to apply."""
