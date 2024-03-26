# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ListEditParams", "Append"]


class ListEditParams(TypedDict, total=False):
    account_id: Required[str]

    append: Iterable[Append]
    """The items in the list."""

    remove: List[str]
    """A list of the item values you want to remove."""


class Append(TypedDict, total=False):
    value: str
    """The value of the item in a list."""
