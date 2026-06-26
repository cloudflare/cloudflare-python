# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SessionGetSessionParticipantDetailsResponse", "Data", "DataParticipant", "DataParticipantPeerEvent"]


class DataParticipantPeerEvent(BaseModel):
    """A connection lifecycle event recorded for a participant's peer."""

    id: Optional[str] = None
    """ID of the peer event."""

    created_at: Optional[str] = None
    """Timestamp when this peer event was created."""

    event_name: Optional[Literal["PEER_CREATED", "PEER_JOINING", "PEER_LEAVING"]] = None
    """Name of the peer event."""

    minutes_consumed: Optional[float] = None
    """Minutes consumed attributed to this event."""

    participant_id: Optional[str] = None
    """ID of the participant this event belongs to."""

    peer_id: Optional[str] = None
    """Peer ID this event belongs to."""

    preset_view_type: Optional[Literal["GROUP_CALL", "WEBINAR", "AUDIO_ROOM", "LIVESTREAM", "CHAT"]] = None
    """View type of the preset associated with the peer."""

    session_id: Optional[str] = None
    """ID of the session this event belongs to."""

    socket_session_id: Optional[str] = None
    """ID of the socket session associated with this event."""

    updated_at: Optional[str] = None
    """Timestamp when this peer event was last updated."""


class DataParticipant(BaseModel):
    id: Optional[str] = None
    """Participant ID. This maps to the corresponding peerId."""

    created_at: Optional[str] = None
    """timestamp when this participant was created."""

    custom_participant_id: Optional[str] = None
    """ID passed by client to create this participant."""

    display_name: Optional[str] = None
    """Display name of participant when joining the session."""

    duration: Optional[float] = None
    """number of minutes for which the participant was in the session."""

    joined_at: Optional[str] = None
    """timestamp at which participant joined the session."""

    left_at: Optional[str] = None
    """timestamp at which participant left the session."""

    peer_events: Optional[List[DataParticipantPeerEvent]] = None
    """Connection lifecycle events for the participant's peer.

    Only included when `include_peer_events` is true.
    """

    preset_name: Optional[str] = None
    """Name of the preset associated with the participant."""

    updated_at: Optional[str] = None
    """timestamp when this participant's data was last updated."""

    user_id: Optional[str] = None
    """User id for this participant."""


class Data(BaseModel):
    participant: Optional[DataParticipant] = None


class SessionGetSessionParticipantDetailsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
