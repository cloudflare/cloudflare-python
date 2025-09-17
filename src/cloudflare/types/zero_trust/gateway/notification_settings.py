# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["NotificationSettings"]


class NotificationSettings(BaseModel):
    enabled: Optional[bool] = None
    """Specify whether to enable notifications."""

    include_context: Optional[bool] = None
    """Specify whether to include context information as query parameters."""

    msg: Optional[str] = None
    """Specify the message to show in the notification."""

    support_url: Optional[str] = None
    """Specify a URL that directs users to more information.

    If unset, the notification opens a block page.
    """
