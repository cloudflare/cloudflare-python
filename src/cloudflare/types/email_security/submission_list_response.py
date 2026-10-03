# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SubmissionListResponse"]


class SubmissionListResponse(BaseModel):
    requested_at: datetime
    """When the submission was requested (UTC)."""

    submission_id: str

    customer_status: Optional[Literal["escalated", "reviewed", "unreviewed"]] = None

    escalated_as: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None
    """The disposition a message is submitted to have."""

    escalated_at: Optional[datetime] = None
    """When the submission was escalated to the security team."""

    escalated_by: Optional[str] = None
    """Email address of the user who escalated the submission."""

    escalated_submission_id: Optional[str] = None
    """
    Submission ID of the escalated team submission, when this user submission was
    escalated.
    """

    original_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None
    """The disposition a message is submitted to have."""

    original_edf_hash: Optional[str] = None
    """EDF hash of the original message."""

    original_postfix_id: Optional[str] = None
    """The postfix ID of the original message that was submitted."""

    outcome: Optional[str] = None
    """Processing outcome of the submission."""

    outcome_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None
    """The disposition a message is submitted to have."""

    requested_by: Optional[str] = None
    """Email address of the user who requested the submission."""

    requested_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None
    """The disposition a message is submitted to have."""

    requested_ts: Optional[str] = None
    """Deprecated, use `requested_at` instead."""

    status: Optional[str] = None
    """Processing status of the submission."""

    subject: Optional[str] = None
    """Subject line of the submitted message."""

    type: Optional[Literal["Team", "User"]] = None
    """Indicates whether a team member or an end user created the submission."""
