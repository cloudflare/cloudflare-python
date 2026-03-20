# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubmissionListResponse"]


class SubmissionListResponse(BaseModel):
    requested_ts: datetime
    """deprecated as of 2026-04-01, use `requested_at` instead."""

    submission_id: str

    customer_status: Optional[Literal["escalated", "reviewed", "unreviewed"]] = None

    escalated_as: Optional[
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

    escalated_at: Optional[datetime] = None

    escalated_by: Optional[str] = None

    escalated_submission_id: Optional[str] = None

    original_disposition: Optional[
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

    original_edf_hash: Optional[str] = None

    original_postfix_id: Optional[str] = None

    outcome: Optional[str] = None

    outcome_disposition: Optional[
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

    requested_at: Optional[datetime] = None

    requested_by: Optional[str] = None

    requested_disposition: Optional[
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

    status: Optional[str] = None

    subject: Optional[str] = None

    type: Optional[str] = None
