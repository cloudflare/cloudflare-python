# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["MoveBulkParams"]


class MoveBulkParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    destination: Required[
        Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    ]

    ids: SequenceNotStr[str]
    """List of message IDs to move"""

    postfix_ids: SequenceNotStr[str]
    """Deprecated, use `ids` instead.

    End of life: November 1, 2026. List of message IDs to move.
    """
