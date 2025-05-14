# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .notification_settings_param import NotificationSettingsParam

__all__ = ["AntiVirusSettingsParam"]


class AntiVirusSettingsParam(TypedDict, total=False):
    enabled_download_phase: bool
    """Enable anti-virus scanning on downloads."""

    enabled_upload_phase: bool
    """Enable anti-virus scanning on uploads."""

    fail_closed: bool
    """Block requests for files that cannot be scanned."""

    notification_settings: NotificationSettingsParam
    """
    Configure a message to display on the user's device when an antivirus search is
    performed.
    """
