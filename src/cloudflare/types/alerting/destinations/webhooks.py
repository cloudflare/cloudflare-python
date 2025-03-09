# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["Webhooks"]


class Webhooks(BaseModel):
    id: Optional[str] = None
    """The unique identifier of a webhook"""

    created_at: Optional[datetime] = None
    """Timestamp of when the webhook destination was created."""

    last_failure: Optional[datetime] = None
    """
    Timestamp of the last time an attempt to dispatch a notification to this webhook
    failed.
    """

    last_success: Optional[datetime] = None
    """
    Timestamp of the last time Cloudflare was able to successfully dispatch a
    notification using this webhook.
    """

    name: Optional[str] = None
    """The name of the webhook destination.

    This will be included in the request body when you receive a webhook
    notification.
    """

    type: Optional[Literal["slack", "generic", "gchat"]] = None
    """Type of webhook endpoint."""

    url: Optional[str] = None
    """The POST endpoint to call when dispatching a notification."""
