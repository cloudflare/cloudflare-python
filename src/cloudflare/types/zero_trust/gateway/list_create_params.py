# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .lists import ListsParam

__all__ = ["ListCreateParams"]


class ListCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the list."""

    type: Required[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]]
    """The type of list."""

    description: str
    """The description of the list."""

    items: Iterable[ListsParam]
    """The items in the list."""
