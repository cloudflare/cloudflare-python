# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["KeyListParams"]


class KeyListParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    cursor: str
    """Cursor for pagination."""
