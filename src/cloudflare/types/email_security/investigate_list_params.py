# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["InvestigateListParams"]


class InvestigateListParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    alert_id: str
    """Filter by alert ID."""

    cursor: str
    """Pagination cursor from the previous response's `result_info`."""

    delivery_status: Literal[
        "delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued", "move_failed"
    ]
    """Delivery status to filter by."""

    detections_only: bool
    """Whether to include only detections in search results."""

    domain: str
    """
    Filter by a domain found in the email — sender domain, recipient domain, or a
    domain in a link.
    """

    end: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The end of the search date range. Defaults to `now`."""

    final_disposition: Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]
    """Dispositions to filter by."""

    message_action: Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]
    """Message actions to filter by."""

    message_id: str
    """Filter by the RFC 5322 Message-ID header."""

    metric: str
    """Metric to aggregate the results by."""

    page: Optional[int]
    """Deprecated: Use cursor pagination instead. End of life: November 1, 2026."""

    per_page: int
    """The number of results per page. Maximum value is 1000."""

    query: str
    """
    Space-delimited term matched case-insensitively against message metadata —
    sender, recipient, subject, attachment names and hashes, and message ID.
    """

    recipient: str
    """Filter by recipient. Matches an email address or a domain."""

    sender: str
    """Filter by sender. Matches an email address or a domain."""

    smtp_helo_ip: str
    """Matches messages whose SMTP HELO server IP address equals this value."""

    start: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The beginning of the search date range.

    Defaults to `now - 30 days`. Must not be in the future.
    """

    subject: str
    """
    Search for messages containing individual keywords in any order within the
    subject.
    """
