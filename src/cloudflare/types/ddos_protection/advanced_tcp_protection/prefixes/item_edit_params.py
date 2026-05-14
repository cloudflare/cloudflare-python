# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemEditParams"]


class ItemEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    comment: str
    """A new comment for the prefix. Optional."""

    excluded: bool
    """Whether to exclude the prefix from protection. Optional."""
