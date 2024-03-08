# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["DwebConfigContentListEntryParam"]


class DwebConfigContentListEntryParam(TypedDict, total=False):
    content: str
    """CID or content path of content to block."""

    description: str
    """An optional description of the content list entry."""

    type: Literal["cid", "content_path"]
    """Type of content list entry to block."""
