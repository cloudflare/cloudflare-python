# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["GatewayItemParam"]


class GatewayItemParam(TypedDict, total=False):
    description: str
    """The description of the list item, if present"""

    value: str
    """The value of the item in a list."""
