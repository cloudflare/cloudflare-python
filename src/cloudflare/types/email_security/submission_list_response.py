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

    escalated_at: Optional[datetime] = None

    escalated_by: Optional[str] = None

    escalated_submission_id: Optional[str] = None

    original_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None

    original_edf_hash: Optional[str] = None

    original_postfix_id: Optional[str] = None
    """The postfix ID of the original message that was submitted"""

    outcome: Optional[str] = None

    outcome_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None

    requested_by: Optional[str] = None

    requested_disposition: Optional[Literal["MALICIOUS", "SUSPICIOUS", "SPOOF", "SPAM", "BULK", "NONE"]] = None

    requested_ts: Optional[str] = None
    """Deprecated, use `requested_at` instead"""

    status: Optional[str] = None

    subject: Optional[str] = None

    type: Optional[Literal["Team", "User"]] = None
    """Whether the submission was created by a team member or an end user."""
