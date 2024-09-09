# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ListUpdateParams"]


class ListUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """The name of the list."""

    description: str
    """The description of the list."""
