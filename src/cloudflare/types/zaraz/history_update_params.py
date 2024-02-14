# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HistoryUpdateParams"]


class HistoryUpdateParams(TypedDict, total=False):
    body: Required[int]
    """ID of the Zaraz configuration to restore."""
