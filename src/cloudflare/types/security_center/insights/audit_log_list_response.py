# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["AuditLogListResponse"]


class AuditLogListResponse(BaseModel):
    id: Optional[str] = None
    """UUIDv7 identifier for the audit log entry, time-ordered."""

    changed_at: Optional[datetime] = None
    """The timestamp when the change occurred."""

    changed_by: Optional[str] = None
    """The actor that made the change.

    'system' for automated changes, or a user identifier.
    """

    current_value: Optional[str] = None
    """The value of the field after the change. Null if the field was cleared."""

    field_changed: Optional[Literal["status", "user_classification"]] = None
    """The field that was changed."""

    issue_id: Optional[str] = None
    """The ID of the insight this audit log entry relates to."""

    previous_value: Optional[str] = None
    """The value of the field before the change.

    Null if the field was not previously set.
    """

    rationale: Optional[str] = None
    """Optional rationale provided for the change."""

    zone_id: Optional[int] = None
    """The zone ID associated with the insight. Only present for zone-level insights."""
