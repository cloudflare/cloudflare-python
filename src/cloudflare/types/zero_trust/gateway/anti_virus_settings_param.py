# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .notification_settings_param import NotificationSettingsParam

__all__ = ["AntiVirusSettingsParam"]


class AntiVirusSettingsParam(TypedDict, total=False):
    """Specify anti-virus settings."""

    enabled_download_phase: Optional[bool]
    """Specify whether to enable anti-virus scanning on downloads."""

    enabled_upload_phase: Optional[bool]
    """Specify whether to enable anti-virus scanning on uploads."""

    fail_closed: Optional[bool]
    """Specify whether to block requests for unscannable files."""

    notification_settings: Optional[NotificationSettingsParam]
    """Configure the message the user's device shows during an antivirus scan."""
