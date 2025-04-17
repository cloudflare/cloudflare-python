# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationSettingsParam"]


class NotificationSettingsParam(TypedDict, total=False):
    enabled: bool
    """Set notification on"""

    include_context: bool
    """If true, context information will be passed as query parameters"""

    msg: str
    """Customize the message shown in the notification."""

    support_url: str
    """Optional URL to direct users to additional information.

    If not set, the notification will open a block page.
    """
