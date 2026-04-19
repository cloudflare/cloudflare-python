# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SessionGetSessionsResponse", "Data", "DataSession"]


class DataSession(BaseModel):
    id: str
    """ID of the session"""

    associated_id: str
    """ID of the meeting this session is associated with.

    In the case of V2 meetings, it is always a UUID. In V1 meetings, it is a room
    name of the form `abcdef-ghijkl`
    """

    created_at: str
    """timestamp when session created"""

    live_participants: float
    """number of participants currently in the session"""

    max_concurrent_participants: float
    """number of maximum participants that were in the session"""

    meeting_display_name: str
    """Title of the meeting this session belongs to"""

    minutes_consumed: float
    """number of minutes consumed since the session started"""

    organization_id: str
    """App id that hosted this session"""

    started_at: str
    """timestamp when session started"""

    status: Literal["LIVE", "ENDED"]
    """current status of session"""

    type: Literal["meeting", "livestream", "participant"]
    """type of session"""

    updated_at: str
    """timestamp when session was last updated"""

    breakout_rooms: Optional[List[object]] = None

    ended_at: Optional[str] = None
    """timestamp when session ended"""

    meta: Optional[object] = None
    """Any meta data about session."""


class Data(BaseModel):
    sessions: Optional[List[DataSession]] = None


class SessionGetSessionsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
