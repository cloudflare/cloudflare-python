# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import Iterable, List

from .gateway_item_param import GatewayItemParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ListEditParams"]


class ListEditParams(TypedDict, total=False):
    account_id: Required[str]

    append: Iterable[GatewayItemParam]
    """The items in the list."""

    remove: List[str]
    """A list of the item values you want to remove."""
