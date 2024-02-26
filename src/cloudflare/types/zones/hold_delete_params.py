# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["HoldDeleteParams"]


class HoldDeleteParams(TypedDict, total=False):
    hold_after: str
    """
    If `hold_after` is provided, the hold will be temporarily disabled, then
    automatically re-enabled by the system at the time specified in this
    RFC3339-formatted timestamp. Otherwise, the hold will be disabled indefinitely.
    """
