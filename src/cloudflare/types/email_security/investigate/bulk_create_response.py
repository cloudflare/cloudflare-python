# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = ["BulkCreateResponse", "ActionParams", "ActionParamsMove", "ActionParamsRelease", "SearchParams"]


class ActionParamsMove(BaseModel):
    destination: Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]
    """The mailbox folder to move messages to."""

    type: Literal["MOVE"]

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
    ] = None
    """Nonfunctional field. End of life: December 1, 2026."""


class ActionParamsRelease(BaseModel):
    type: Literal["RELEASE"]


ActionParams: TypeAlias = Annotated[Union[ActionParamsMove, ActionParamsRelease], PropertyInfo(discriminator="type")]


class SearchParams(BaseModel):
    action_log: Optional[bool] = None
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    alert_id: Optional[str] = None
    """Alert ID of the detection to filter by."""

    delivery_status: Optional[
        Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued", "move_failed"]
    ] = None
    """Delivery status to filter by."""

    detections_only: Optional[bool] = None
    """Whether to include only detections in search results."""

    domain: Optional[str] = None
    """
    Match messages that mention this domain — sender domain, recipient domain, or a
    domain in a link.
    """

    end: Optional[datetime] = None
    """End of search date range."""

    exact_subject: Optional[str] = None
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
    ] = None
    """Dispositions to filter by."""

    message_action: Optional[Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]] = None
    """Message actions to filter by."""

    message_id: Optional[str] = None
    """Message-ID header value to filter by."""

    metric: Optional[str] = None
    """Metric name to filter the search by."""

    query: Optional[str] = None
    """Space-delimited search term. Case-insensitive."""

    recipient: Optional[str] = None
    """Match messages whose recipient is this email address or domain."""

    sender: Optional[str] = None
    """Match messages whose sender is this email address or domain."""

    smtp_helo_ip: Optional[str] = None
    """Matches messages whose SMTP HELO server IP address equals this value."""

    start: Optional[datetime] = None
    """Beginning of search date range."""

    subject: Optional[str] = None
    """Match messages whose subject contains these keywords, in any order."""

    submissions: Optional[bool] = None
    """Whether to search reclassification submissions instead of original messages."""


class BulkCreateResponse(BaseModel):
    action_params: ActionParams

    action_type: Literal["MOVE", "RELEASE"]

    created_at: datetime

    job_id: str

    messages_cancelled: int
    """
    Messages that were cancelled: rows cancelled via the API before being claimed,
    and rows whose in-flight attempt ended when the job reached a terminal state.
    Together the counters satisfy total_messages_discovered = messages_pending +
    messages_successful + messages_failed + messages_skipped + messages_cancelled.
    """

    messages_failed: int

    messages_pending: int

    messages_skipped: int
    """
    Messages that discovery skipped (for example, phish submissions, which the job
    cannot action).
    """

    messages_successful: int

    search_params: SearchParams

    status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED"]
    """Status of a bulk action job."""

    total_messages_discovered: int

    comment: Optional[str] = None

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    status_message: Optional[str] = None
