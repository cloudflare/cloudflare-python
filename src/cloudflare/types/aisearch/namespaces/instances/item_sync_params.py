# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ItemSyncParams"]


class ItemSyncParams(TypedDict, total=False):
    account_id: str

    name: Required[str]

    id: Required[str]
    """AI Search instance ID. Lowercase alphanumeric, hyphens, and underscores."""

    next_action: Required[Literal["INDEX"]]
