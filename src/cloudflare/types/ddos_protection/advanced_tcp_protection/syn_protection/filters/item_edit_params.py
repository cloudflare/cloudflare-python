# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ItemEditParams"]


class ItemEditParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    expression: str
    """The new filter expression. Optional."""

    mode: str
    """The new mode for the filter.

    Optional. Must be one of 'enabled', 'disabled', 'monitoring'.
    """
