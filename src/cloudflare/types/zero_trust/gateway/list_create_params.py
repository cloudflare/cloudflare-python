# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Literal

from typing import Iterable

from .gateway_item_param import GatewayItemParam

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ListCreateParams"]

class ListCreateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the list."""

    type: Required[Literal["SERIAL", "URL", "DOMAIN", "EMAIL", "IP"]]
    """The type of list."""

    description: str
    """The description of the list."""

    items: Iterable[GatewayItemParam]
    """The items in the list."""