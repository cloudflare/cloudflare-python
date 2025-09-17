# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ListUpdateParams", "Item"]


class ListUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """Specify the list name."""

    description: str
    """Provide the list description."""

    items: Iterable[Item]
    """Add items to the list."""


class Item(TypedDict, total=False):
    description: str
    """Provide the list item description (optional)."""

    value: str
    """Specify the item value."""
