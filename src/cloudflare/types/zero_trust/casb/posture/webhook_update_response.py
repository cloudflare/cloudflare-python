# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["WebhookUpdateResponse", "Header"]


class Header(BaseModel):
    key: Optional[str] = None
    """Header key name (lowercase)."""


class WebhookUpdateResponse(BaseModel):
    """Webhook configuration for sending finding notifications."""

    id: str
    """Unique identifier for the specific webhook configuration."""

    authentication_type: Literal["Basic Auth", "None", "Bearer Auth", "Static Headers", "HMAC-Signing"]
    """Type of authentication used for the webhook."""

    created_at: datetime
    """Timestamp when the webhook configuration was created."""

    destination_url: str
    """Target URL for the webhook configuration. Where resulting data will be sent."""

    label: str
    """Account-specified display label for the webhook configuration."""

    status: Literal["enabled", "disabled"]
    """Current status of the webhook configuration.

    If disabled, data cannot be sent through this configuration.
    """

    updated_at: datetime
    """Timestamp when the webhook configuration was last updated."""

    version: int
    """Version number of the configuration."""

    headers: Optional[List[Header]] = None
    """List of header keys configured for this webhook.

    Values are not included for security reasons.
    """
