# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["ArticleBulkEditParams"]


class ArticleBulkEditParams(TypedDict, total=False):
    account_id: Required[str]

    article_ids: Required[SequenceNotStr[str]]
    """Array of article UUIDs to mark (1-50)."""

    read: Required[bool]
    """True to mark read, false to mark unread."""
