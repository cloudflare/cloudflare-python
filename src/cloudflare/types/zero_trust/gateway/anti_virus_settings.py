# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel
from .notification_settings import NotificationSettings

__all__ = ["AntiVirusSettings"]


class AntiVirusSettings(BaseModel):
    """Specify anti-virus settings."""

    enabled_download_phase: Optional[bool] = None
    """Specify whether to enable anti-virus scanning on downloads."""

    enabled_upload_phase: Optional[bool] = None
    """Specify whether to enable anti-virus scanning on uploads."""

    fail_closed: Optional[bool] = None
    """Specify whether to block requests for unscannable files."""

    notification_settings: Optional[NotificationSettings] = None
    """Configure the message the user's device shows during an antivirus scan."""
