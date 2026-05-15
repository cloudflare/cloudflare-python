# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SpendingLimitCreateParams"]


class SpendingLimitCreateParams(TypedDict, total=False):
    account_id: Required[str]

    amount: Required[int]
    """Spending limit amount in cents (min 100)."""

    duration: Required[Literal["daily", "weekly", "monthly"]]
    """Spending limit duration."""

    strategy: Required[Literal["fixed", "sliding"]]
    """Spending limit strategy."""
