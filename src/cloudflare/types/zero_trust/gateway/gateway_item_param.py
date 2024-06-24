# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GatewayItemParam"]


class GatewayItemParam(TypedDict, total=False):
    created_at: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    description: str
    """The description of the list item, if present"""

    value: str
    """The value of the item in a list."""
