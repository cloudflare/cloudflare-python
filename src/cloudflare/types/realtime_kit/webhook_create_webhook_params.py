# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["WebhookCreateWebhookParams"]


class WebhookCreateWebhookParams(TypedDict, total=False):
    account_id: Required[str]
    """The account identifier tag."""

    events: Required[
        List[
            Literal[
                "meeting.started",
                "meeting.ended",
                "meeting.participantJoined",
                "meeting.participantLeft",
                "meeting.chatSynced",
                "recording.statusUpdate",
                "livestreaming.statusUpdate",
                "meeting.transcript",
                "meeting.summary",
            ]
        ]
    ]
    """Events that this webhook will get triggered by"""

    name: Required[str]
    """Name of the webhook"""

    url: Required[str]
    """URL this webhook will send events to"""

    enabled: bool
    """Set whether or not the webhook should be active when created"""
