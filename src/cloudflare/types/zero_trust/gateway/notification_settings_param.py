# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationSettingsParam"]


class NotificationSettingsParam(TypedDict, total=False):
    """Configure the message the user's device shows during an antivirus scan."""

    enabled: bool
    """Specify whether to enable notifications."""

    include_context: bool
    """Specify whether to include context information as query parameters."""

    msg: str
    """Specify the message to show in the notification."""

    support_url: str
    """Specify a URL that directs users to more information.

    If unset, the notification opens a block page.
    """
