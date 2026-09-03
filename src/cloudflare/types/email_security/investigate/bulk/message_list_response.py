# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ....._utils import PropertyInfo
from ....._models import BaseModel

__all__ = [
    "MessageListResponse",
    "ActionParams",
    "ActionParamsMove",
    "ActionParamsRelease",
    "Message",
    "MessageActionLog",
    "MessageActionLogProperties",
    "MessageProperties",
    "MessageFinding",
    "MessageValidation",
]


class ActionParamsMove(BaseModel):
    client_recipient: str

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
    client_recipient: str

    type: Literal["RELEASE"]


ActionParams: TypeAlias = Annotated[Union[ActionParamsMove, ActionParamsRelease], PropertyInfo(discriminator="type")]


class MessageActionLogProperties(BaseModel):
    """Additional properties for the action."""

    folder: Optional[str] = None
    """Target folder for move operations."""

    requested_by: Optional[str] = None
    """User who requested the action."""


class MessageActionLog(BaseModel):
    completed_at: datetime
    """Timestamp when action completed."""

    operation: Literal["MOVE", "RELEASE", "RECLASSIFY", "SUBMISSION", "QUARANTINE_RELEASE", "PREVIEW"]
    """Type of action performed."""

    completed_timestamp: Optional[str] = None
    """Deprecated, use `completed_at` instead. End of life: November 1, 2026."""

    properties: Optional[MessageActionLogProperties] = None
    """Additional properties for the action."""

    status: Optional[str] = None
    """Status of the action."""


class MessageProperties(BaseModel):
    """Message processing properties."""

    allowlisted_pattern: Optional[str] = None
    """Pattern that allowlisted this message."""

    allowlisted_pattern_type: Optional[
        Literal[
            "quarantine_release",
            "acceptable_sender",
            "allowed_sender",
            "allowed_recipient",
            "domain_similarity",
            "domain_recency",
            "managed_acceptable_sender",
            "outbound_ndr",
        ]
    ] = None
    """Type of allowlist pattern."""

    blocklisted_message: Optional[bool] = None
    """Whether message was blocklisted."""

    blocklisted_pattern: Optional[str] = None
    """Pattern that blocklisted this message."""

    whitelisted_pattern_type: Optional[
        Literal[
            "quarantine_release",
            "acceptable_sender",
            "allowed_sender",
            "allowed_recipient",
            "domain_similarity",
            "domain_recency",
            "managed_acceptable_sender",
            "outbound_ndr",
        ]
    ] = None
    """Legacy field for allowlist pattern type."""


class MessageFinding(BaseModel):
    attachment: Optional[str] = None

    detail: Optional[str] = None

    detection: Optional[
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

    field: Optional[str] = None

    name: Optional[str] = None

    portion: Optional[str] = None

    reason: Optional[str] = None

    score: Optional[float] = None

    value: Optional[str] = None


class MessageValidation(BaseModel):
    comment: Optional[str] = None

    dkim: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    dmarc: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    spf: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None


class Message(BaseModel):
    id: str
    """Unique identifier for a message retrieved from investigation."""

    action_log: List[MessageActionLog]
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    client_recipients: List[str]

    detection_reasons: List[str]

    is_phish_submission: bool

    is_quarantined: bool

    postfix_id: str
    """The identifier of the message."""

    properties: MessageProperties
    """Message processing properties."""

    ts: str
    """Deprecated, use `scanned_at` instead. End of life: November 1, 2026."""

    alert_id: Optional[str] = None

    delivery_mode: Optional[
        Literal[
            "DIRECT",
            "BCC",
            "JOURNAL",
            "REVIEW_SUBMISSION",
            "DMARC_UNVERIFIED",
            "DMARC_FAILURE_REPORT",
            "DMARC_AGGREGATE_REPORT",
            "THREAT_INTEL_SUBMISSION",
            "SIMULATION_SUBMISSION",
            "API",
            "RETRO_SCAN",
        ]
    ] = None

    delivery_status: Optional[
        List[Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued", "move_failed"]]
    ] = None

    edf_hash: Optional[str] = None

    envelope_from: Optional[str] = None

    envelope_to: Optional[List[str]] = None

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

    findings: Optional[List[MessageFinding]] = None
    """
    Deprecated, use the `findings` field from
    `GET /investigate/{investigate_id}/detections` instead. End of life: November
    1, 2026. Detection findings for this message.
    """

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_name: Optional[str] = None

    htmltext_structure_hash: Optional[str] = None

    message_id: Optional[str] = None

    post_delivery_operations: Optional[List[Literal["PREVIEW", "QUARANTINE_RELEASE", "SUBMISSION", "MOVE"]]] = None
    """Post-delivery operations performed on this message."""

    postfix_id_outbound: Optional[str] = None

    replyto: Optional[str] = None

    scanned_at: Optional[datetime] = None
    """When the message was scanned (UTC)."""

    sent_at: Optional[datetime] = None
    """When the message was sent (UTC)."""

    sent_date: Optional[str] = None

    smtp_helo_server_ip: Optional[str] = None

    smtp_previous_hop_ip: Optional[str] = None

    subject: Optional[str] = None

    threat_categories: Optional[List[str]] = None

    to: Optional[List[str]] = None

    to_name: Optional[List[str]] = None

    validation: Optional[MessageValidation] = None

    x_originating_ip: Optional[str] = None


class MessageListResponse(BaseModel):
    action_params: ActionParams

    action_type: Literal["MOVE", "RELEASE"]

    created_at: datetime

    message_id: str

    postfix_id: str

    retry_count: int

    status: Literal["PENDING", "DISCOVERING", "PROCESSING", "COMPLETED", "FAILED", "CANCELLED", "SKIPPED"]

    alert_id: Optional[str] = None

    email_message_id: Optional[str] = None

    message: Optional[Message] = None

    processed_at: Optional[datetime] = None

    retry_after: Optional[datetime] = None
    """When to retry the action if it failed."""

    status_message: Optional[str] = None
