# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InvestigateListResponse", "ActionLog", "ActionLogProperties", "Properties", "Finding", "Validation"]


class ActionLogProperties(BaseModel):
    """Additional properties for the action"""

    folder: Optional[str] = None
    """Target folder for move operations"""

    requested_by: Optional[str] = None
    """User who requested the action"""


class ActionLog(BaseModel):
    completed_at: datetime
    """Timestamp when action completed"""

    operation: Literal["MOVE", "RELEASE", "RECLASSIFY", "SUBMISSION", "QUARANTINE_RELEASE", "PREVIEW"]
    """Type of action performed"""

    completed_timestamp: Optional[str] = None
    """Deprecated, use `completed_at` instead. End of life: November 1, 2026."""

    properties: Optional[ActionLogProperties] = None
    """Additional properties for the action"""

    status: Optional[str] = None
    """Status of the action"""


class Properties(BaseModel):
    """Message processing properties"""

    allowlisted_pattern: Optional[str] = None
    """Pattern that allowlisted this message"""

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
    """Type of allowlist pattern"""

    blocklisted_message: Optional[bool] = None
    """Whether message was blocklisted"""

    blocklisted_pattern: Optional[str] = None
    """Pattern that blocklisted this message"""

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
    """Legacy field for allowlist pattern type"""


class Finding(BaseModel):
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


class Validation(BaseModel):
    comment: Optional[str] = None

    dkim: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    dmarc: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    spf: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None


class InvestigateListResponse(BaseModel):
    id: str
    """Unique identifier for a message retrieved from investigation"""

    action_log: List[ActionLog]
    """Deprecated, use `GET /investigate/{investigate_id}/action_log` instead.

    End of life: November 1, 2026.
    """

    client_recipients: List[str]

    detection_reasons: List[str]

    is_phish_submission: bool

    is_quarantined: bool

    postfix_id: str
    """The identifier of the message"""

    properties: Properties
    """Message processing properties"""

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
        List[Literal["delivered", "moved", "quarantined", "rejected", "deferred", "bounced", "queued"]]
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

    findings: Optional[List[Finding]] = None
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
    """Post-delivery operations performed on this message"""

    postfix_id_outbound: Optional[str] = None

    replyto: Optional[str] = None

    scanned_at: Optional[datetime] = None
    """When the message was scanned (UTC)"""

    sent_at: Optional[datetime] = None
    """When the message was sent (UTC)"""

    sent_date: Optional[str] = None

    subject: Optional[str] = None

    threat_categories: Optional[List[str]] = None

    to: Optional[List[str]] = None

    to_name: Optional[List[str]] = None

    validation: Optional[Validation] = None
