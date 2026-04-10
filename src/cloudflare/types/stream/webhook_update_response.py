# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["WebhookUpdateResponse"]


class WebhookUpdateResponse(BaseModel):
    modified: Optional[datetime] = None
    """The date and time the webhook was last modified."""

    notification_url: Optional[str] = None
    """The URL where webhooks will be sent."""

    notification_url: Optional[str] = FieldInfo(alias="notificationUrl", default=None)
    """The URL where webhooks will be sent."""

    secret: Optional[str] = None
    """The secret used to verify webhook signatures."""
