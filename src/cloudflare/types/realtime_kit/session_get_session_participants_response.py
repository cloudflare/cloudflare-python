# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["SessionGetSessionParticipantsResponse", "Data", "DataParticipant"]


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

    preset_name: Optional[str] = None
    """Name of the preset associated with the participant."""

    updated_at: Optional[str] = None
    """timestamp when this participant's data was last updated."""

    user_id: Optional[str] = None
    """User id for this participant."""


class Data(BaseModel):
    participants: Optional[List[DataParticipant]] = None


class SessionGetSessionParticipantsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
