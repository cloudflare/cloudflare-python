# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SubscriptionComponentParam"]


class SubscriptionComponentParam(TypedDict, total=False):
    default: float
    """The default amount assigned."""

    name: str
    """The name of the component value."""

    price: float
    """The unit price for the component value."""

    value: float
    """The amount of the component value assigned."""
