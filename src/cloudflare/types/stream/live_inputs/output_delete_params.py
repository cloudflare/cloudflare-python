# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OutputDeleteParams"]


class OutputDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    live_input_identifier: Required[str]
    """A unique identifier for a live input."""

    body: Required[object]
