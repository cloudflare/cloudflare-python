# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["AccessAccessRequests"]


class AccessAccessRequests(BaseModel):
    action: Optional[str] = None
    """The event that occurred, such as a login attempt."""

    allowed: Optional[bool] = None
    """The result of the authentication event."""

    app_domain: Optional[str] = None
    """The URL of the Access application."""

    app_uid: Optional[object] = None
    """The unique identifier for the Access application."""

    connection: Optional[str] = None
    """The IdP used to authenticate."""

    created_at: Optional[datetime] = None

    ip_address: Optional[str] = None
    """The IP address of the authenticating user."""

    ray_id: Optional[str] = None
    """The unique identifier for the request to Cloudflare."""

    user_email: Optional[str] = None
    """The email address of the authenticating user."""
