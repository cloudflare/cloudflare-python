# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["JitRequestListResponse"]


class JitRequestListResponse(BaseModel):
    app_aud: Optional[str] = None
    """Audience of the Access application."""

    app_hostname: Optional[str] = None

    approvals_received: Optional[int] = None
    """Number of unique actors who approved the request."""

    approver_emails: Optional[List[str]] = None
    """Unique actors who approved the request."""

    created_at: Optional[datetime] = None

    expires_at: Optional[datetime] = None

    knock_request_id: Optional[str] = None
    """Unique identifier for the JIT request."""

    purpose_justification: Optional[str] = None

    requester_email: Optional[str] = None

    status: Optional[Literal["PENDING", "APPROVED", "DENIED", "CANCELED", "SPENT"]] = None
    """JIT request status. `SPENT` is deprecated and interpreted as `APPROVED`."""
