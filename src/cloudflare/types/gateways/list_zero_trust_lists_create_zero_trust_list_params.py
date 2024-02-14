# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ListZeroTrustListsCreateZeroTrustListParams", "Item"]


class ListZeroTrustListsCreateZeroTrustListParams(TypedDict, total=False):
    name: Required[str]
    """The name of the list."""

    type: Required[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]]
    """The type of list."""

    description: str
    """The description of the list."""

    items: Iterable[Item]
    """The items in the list."""


class Item(TypedDict, total=False):
    value: str
    """The value of the item in a list."""
