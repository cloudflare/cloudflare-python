# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ItemDeleteParams", "Item"]


class ItemDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    items: Iterable[Item]


class Item(TypedDict, total=False):
    id: str
    """The unique ID of the item in the List."""
