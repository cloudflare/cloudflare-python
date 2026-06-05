# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionGetParticipantDataFromPeerIDResponse", "Data", "DataParticipant", "DataParticipantPeerReport"]


class DataParticipantPeerReport(BaseModel):
    """Peer call statistics report."""

    metadata: Optional[Dict[str, object]] = None

    quality: Optional[Dict[str, object]] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class DataParticipant(BaseModel):
    id: Optional[str] = None
    """ID of the participant."""

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

    peer_events: Optional[List[Dict[str, object]]] = None

    peer_report: Optional[DataParticipantPeerReport] = None
    """Peer call statistics report."""

    role: Optional[str] = None
    """Name of the preset associated with the participant."""

    session_id: Optional[str] = None

    updated_at: Optional[str] = None
    """timestamp when this participant's data was last updated."""

    user_id: Optional[str] = None
    """User id for this participant."""


class Data(BaseModel):
    participant: Optional[DataParticipant] = None


class SessionGetParticipantDataFromPeerIDResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
