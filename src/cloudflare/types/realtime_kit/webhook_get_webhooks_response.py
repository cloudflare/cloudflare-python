# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["WebhookGetWebhooksResponse", "Data"]


class Data(BaseModel):
    id: str
    """ID of the webhook"""

    created_at: datetime
    """Timestamp when this webhook was created"""

    enabled: bool
    """Set to true if the webhook is active"""

    events: List[
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
    """Events this webhook will send updates for"""

    name: str
    """Name of the webhook"""

    updated_at: datetime
    """Timestamp when this webhook was updated"""

    url: str
    """URL the webhook will send events to"""


class WebhookGetWebhooksResponse(BaseModel):
    data: List[Data]

    success: bool
