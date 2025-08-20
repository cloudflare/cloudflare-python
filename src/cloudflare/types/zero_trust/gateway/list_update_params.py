# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ListUpdateParams", "Item"]


class ListUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the list."""

    description: str
    """The description of the list."""

    items: Iterable[Item]
    """items to add to the list."""


class Item(TypedDict, total=False):
    description: str
    """The description of the list item, if present."""

    value: str
    """The value of the item in a list."""
