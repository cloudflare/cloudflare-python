# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookEditWebhookParams"]


class WebhookEditWebhookParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    app_id: Required[str]
    """The app identifier tag."""

    enabled: bool

    events: List[
        Literal[
            "meeting.started",
            "meeting.ended",
            "meeting.participantJoined",
            "meeting.participantLeft",
            "recording.statusUpdate",
            "livestreaming.statusUpdate",
            "meeting.chatSynced",
            "meeting.transcript",
            "meeting.summary",
        ]
    ]
    """Events that the webhook will get triggered by"""

    name: str
    """Name of the webhook"""

    url: str
    """URL the webhook will send events to"""
