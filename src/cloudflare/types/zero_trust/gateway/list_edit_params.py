# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .lists import ListsParam

__all__ = ["ListEditParams"]


class ListEditParams(TypedDict, total=False):
    account_id: Required[str]

    append: Iterable[ListsParam]
    """The items in the list."""

    remove: List[str]
    """A list of the item values you want to remove."""
