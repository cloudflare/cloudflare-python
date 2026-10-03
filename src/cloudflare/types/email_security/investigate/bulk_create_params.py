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
    """The action the job performs on every message matching the search parameters."""

    search_params: Required[SearchParams]

    comment: Optional[str]
    """Optional note describing the job."""

    destination: Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    """Required when action is 'MOVE'."""

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


class SearchParams(TypedDict, total=False):
    action_log: bool
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    alert_id: Optional[str]
    """Alert ID of the detection to filter by."""

    delivery_status: Optional[
        Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued", "move_failed"]
    ]
    """Delivery status to filter by."""

    detections_only: bool
    """Whether to include only detections in search results."""

    domain: Optional[str]
    """
    Match messages that mention this domain — sender domain, recipient domain, or a
    domain in a link.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End of search date range."""

    exact_subject: Optional[str]
    """Match messages whose subject line equals this value exactly."""

    final_disposition: Optional[
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
    """Dispositions to filter by."""

    message_action: Optional[Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]]
    """Message actions to filter by."""

    message_id: Optional[str]
    """Message-ID header value to filter by."""

    metric: Optional[str]
    """Metric name to filter the search by."""

    query: Optional[str]
    """Space-delimited search term. Case-insensitive."""

    recipient: Optional[str]
    """Match messages whose recipient is this email address or domain."""

    sender: Optional[str]
    """Match messages whose sender is this email address or domain."""

    smtp_helo_ip: Optional[str]
    """Matches messages whose SMTP HELO server IP address equals this value."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Beginning of search date range."""

    subject: Optional[str]
    """Match messages whose subject contains these keywords, in any order."""

    submissions: bool
    """Whether to search reclassification submissions instead of original messages."""
