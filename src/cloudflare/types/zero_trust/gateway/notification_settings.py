# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["NotificationSettings"]


class NotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Set notification on"""

    msg: Optional[str] = None
    """Customize the message shown in the notification."""

    support_url: Optional[str] = None
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """
