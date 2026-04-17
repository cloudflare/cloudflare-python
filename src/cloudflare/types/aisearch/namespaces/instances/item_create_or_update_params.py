# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemCreateOrUpdateParams"]


class ItemCreateOrUpdateParams(TypedDict, total=False):
    account_id: str

    name: Required[str]

    key: Required[str]
    """Item key / filename. Must not exceed 128 characters."""

    next_action: Required[Literal["INDEX"]]
