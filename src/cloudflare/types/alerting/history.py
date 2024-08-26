# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["History"]


class History(BaseModel):
    id: Optional[str] = None
    """UUID"""

    alert_body: Optional[str] = None
    """Message body included in the notification sent."""

    alert_type: Optional[str] = None
    """Type of notification that has been dispatched."""

    description: Optional[str] = None
    """Description of the notification policy (if present)."""

    mechanism: Optional[str] = None
    """The mechanism to which the notification has been dispatched."""

    mechanism_type: Optional[Literal["email", "pagerduty", "webhook"]] = None
    """The type of mechanism to which the notification has been dispatched.

    This can be email/pagerduty/webhook based on the mechanism configured.
    """

    name: Optional[str] = None
    """Name of the policy."""

    policy_id: Optional[str] = None
    """The unique identifier of a notification policy"""

    sent: Optional[datetime] = None
    """Timestamp of when the notification was dispatched in ISO 8601 format."""
