# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["JitRequestGetResponse", "Event"]


class Event(BaseModel):
    actor_email: Optional[str] = None

    actor_idp: Optional[str] = None

    actor_uuid: Optional[str] = None

    decision_outcome: Optional[str] = None

    rayid: Optional[str] = FieldInfo(alias="ray_id", default=None)

    session_duration_seconds: Optional[int] = None

    success: Optional[bool] = None

    timestamp: Optional[datetime] = None

    type: Optional[
        Literal["CREATED", "APPROVER_DECISION", "COMMITTED", "CANCELED", "LOGIN_SUCCESS", "REDIRECT_TO_ACTIVE"]
    ] = None


class JitRequestGetResponse(BaseModel):
    app_aud: Optional[str] = None
    """Audience of the Access application."""

    app_hostname: Optional[str] = None

    approvals_received: Optional[int] = None
    """Number of unique actors who approved the request."""

    approver_emails: Optional[List[str]] = None
    """Unique actors who approved the request."""

    created_at: Optional[datetime] = None

    events: Optional[List[Event]] = None

    expires_at: Optional[datetime] = None

    knock_request_id: Optional[str] = None
    """Unique identifier for the JIT request."""

    purpose_justification: Optional[str] = None

    requester_email: Optional[str] = None

    status: Optional[Literal["PENDING", "APPROVED", "DENIED", "CANCELED", "SPENT"]] = None
    """JIT request status. `SPENT` is deprecated and interpreted as `APPROVED`."""
