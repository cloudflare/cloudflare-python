# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ListEditParams", "Append"]


class ListEditParams(TypedDict, total=False):
    account_id: Required[str]

    append: Iterable[Append]
    """Add items to the list."""

    remove: SequenceNotStr[str]
    """Lists of item values you want to remove."""


class Append(TypedDict, total=False):
    description: str
    """Provide the list item description (optional)."""

    value: str
    """Specify the item value."""
