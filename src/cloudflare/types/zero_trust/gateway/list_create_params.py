# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ListCreateParams", "Item"]


class ListCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """Specify the list name."""

    type: Required[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]]
    """Specify the list type."""

    description: str
    """Provide the list description."""

    items: Iterable[Item]
    """Add items to the list."""


class Item(TypedDict, total=False):
    description: str
    """Provide the list item description (optional)."""

    value: str
    """Specify the item value."""
