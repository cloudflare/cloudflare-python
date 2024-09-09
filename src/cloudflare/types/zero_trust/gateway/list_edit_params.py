# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Iterable
from typing_extensions import Required, TypedDict

from .gateway_item_param import GatewayItemParam

__all__ = ["ListEditParams"]


class ListEditParams(TypedDict, total=False):
    account_id: Required[str]

    append: Iterable[GatewayItemParam]
    """The items in the list."""

    remove: List[str]
    """A list of the item values you want to remove."""
