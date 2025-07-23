# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["InvestigateGetResponse", "Properties", "Finding", "Validation"]


class Properties(BaseModel):
    allowlisted_pattern: Optional[str] = None

    allowlisted_pattern_type: Optional[
        Literal[
            "quarantine_release",
            "acceptable_sender",
            "allowed_sender",
            "allowed_recipient",
            "domain_similarity",
            "domain_recency",
            "managed_acceptable_sender",
        ]
    ] = None

    blocklisted_message: Optional[bool] = None

    blocklisted_pattern: Optional[str] = None

    whitelisted_pattern_type: Optional[
        Literal[
            "quarantine_release",
            "acceptable_sender",
            "allowed_sender",
            "allowed_recipient",
            "domain_similarity",
            "domain_recency",
            "managed_acceptable_sender",
        ]
    ] = None


class Finding(BaseModel):
    detail: Optional[str] = None

    name: Optional[str] = None

    value: Optional[str] = None


class Validation(BaseModel):
    comment: Optional[str] = None

    dkim: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    dmarc: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None

    spf: Optional[Literal["pass", "neutral", "fail", "error", "none"]] = None


class InvestigateGetResponse(BaseModel):
    id: str

    action_log: object

    client_recipients: List[str]

    detection_reasons: List[str]

    is_phish_submission: bool

    is_quarantined: bool

    postfix_id: str
    """The identifier of the message."""

    properties: Properties

    ts: str

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

    edf_hash: Optional[str] = None

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

    from_: Optional[str] = FieldInfo(alias="from", default=None)

    from_name: Optional[str] = None

    message_id: Optional[str] = None

    sent_date: Optional[str] = None

    subject: Optional[str] = None

    threat_categories: Optional[List[str]] = None

    to: Optional[List[str]] = None

    to_name: Optional[List[str]] = None

    validation: Optional[Validation] = None
