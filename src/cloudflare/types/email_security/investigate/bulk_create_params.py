# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["BulkCreateParams", "SearchParams"]


class BulkCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    action: Required[Literal["MOVE", "RELEASE"]]

    search_params: Required[SearchParams]

    comment: Optional[str]

    destination: Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]

    expected_disposition: Literal[
        "MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"
    ]


class SearchParams(TypedDict, total=False):
    action_log: bool
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    alert_id: Optional[str]

    delivery_status: Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued"]
    """Delivery status of the message."""

    detections_only: bool

    domain: Optional[str]

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of search date range"""

    exact_subject: Optional[str]

    final_disposition: Literal[
        "MALICIOUS", "MALICIOUS-BEC", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "ENCRYPTED", "EXTERNAL", "UNKNOWN", "NONE"
    ]

    message_action: Optional[Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]]

    message_id: Optional[str]

    metric: Optional[str]

    query: Optional[str]

    recipient: Optional[str]

    sender: Optional[str]

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Beginning of search date range"""

    subject: Optional[str]

    submissions: bool
