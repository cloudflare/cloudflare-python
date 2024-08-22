# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VideoStorageUsageParams"]


class VideoStorageUsageParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    creator: str
    """A user-defined identifier for the media creator."""
