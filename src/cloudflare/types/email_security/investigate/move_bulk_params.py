# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from ...._types import SequenceNotStr

__all__ = ["MoveBulkParams"]


class MoveBulkParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    destination: Required[
        Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    ]
    """The mailbox folder to move messages to."""

    ids: Required[SequenceNotStr[str]]
    """List of message IDs to move."""

    expected_disposition: Optional[
        Literal[
            "MALICIOUS",
            "MALICIOUS-BEC",
            "SUSPICIOUS",
            "SPOOF",
            "SPAM",
            "BULK",
            "ENCRYPTED",
            "EXTERNAL",
            "UNKNOWN",
            "NONE",
        ]
    ]
    """Nonfunctional field. End of life: December 1, 2026."""

    postfix_ids: SequenceNotStr[str]
    """Deprecated, use `ids` instead. End of life: November 1, 2026."""
