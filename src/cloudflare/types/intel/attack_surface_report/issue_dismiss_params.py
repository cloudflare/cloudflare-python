# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IssueDismissParams"]


class IssueDismissParams(TypedDict, total=False):
    account_id: str
    """Identifier."""

    dismiss: bool
