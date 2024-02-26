# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["VideoStorageUsageParams"]


class VideoStorageUsageParams(TypedDict, total=False):
    creator: str
    """A user-defined identifier for the media creator."""
