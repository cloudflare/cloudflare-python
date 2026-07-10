# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel

__all__ = ["BulkListResponse", "ActionParams", "ActionParamsMove", "ActionParamsRelease", "SearchParams"]


class ActionParamsMove(BaseModel):
    destination: Literal["Inbox", "JunkEmail", "DeletedItems", "RecoverableItemsDeletions", "RecoverableItemsPurges"]

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


class ActionParamsRelease(BaseModel):
    type: Literal["RELEASE"]


ActionParams: TypeAlias = Annotated[Union[ActionParamsMove, ActionParamsRelease], PropertyInfo(discriminator="type")]


class SearchParams(BaseModel):
    action_log: Optional[bool] = None
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    alert_id: Optional[str] = None

    delivery_status: Optional[
        Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued"]
    ] = None
    """Delivery status of the message."""

    detections_only: Optional[bool] = None

    domain: Optional[str] = None

    end: Optional[datetime] = None
    """End of search date range"""

    exact_subject: Optional[str] = None

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

    message_action: Optional[Literal["PREVIEW", "QUARANTINE_RELEASED", "MOVED"]] = None

    message_id: Optional[str] = None

    metric: Optional[str] = None

    query: Optional[str] = None

    recipient: Optional[str] = None

    sender: Optional[str] = None

    start: Optional[datetime] = None
    """Beginning of search date range"""

    subject: Optional[str] = None

    submissions: Optional[bool] = None


class BulkListResponse(BaseModel):
    action_params: ActionParams

    action_type: Literal["MOVE", "RELEASE"]

    created_at: datetime

    job_id: str

    messages_failed: int

    messages_pending: int

    messages_successful: int

    search_params: SearchParams

    status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]

    total_messages_discovered: int

    comment: Optional[str] = None

    completed_at: Optional[datetime] = None

    started_at: Optional[datetime] = None

    status_message: Optional[str] = None
