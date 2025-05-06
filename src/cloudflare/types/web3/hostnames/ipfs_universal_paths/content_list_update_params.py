# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

__all__ = ["ContentListUpdateParams", "Entry"]


class ContentListUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Specify the identifier of the hostname."""

    action: Required[Literal["block"]]
    """Behavior of the content list."""

    entries: Required[Iterable[Entry]]
    """Provides content list entries."""


class Entry(TypedDict, total=False):
    content: str
    """Specify the CID or content path of content to block."""

    description: str
    """Specify an optional description of the content list entry."""

    type: Literal["cid", "content_path"]
    """Specify the type of content list entry to block."""
