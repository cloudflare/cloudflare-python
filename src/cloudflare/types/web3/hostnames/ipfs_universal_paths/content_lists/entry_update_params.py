# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["EntryUpdateParams"]


class EntryUpdateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    identifier: Required[str]
    """Identifier"""

    content: Required[str]
    """CID or content path of content to block."""

    type: Required[Literal["cid", "content_path"]]
    """Type of content list entry to block."""

    description: str
    """An optional description of the content list entry."""
