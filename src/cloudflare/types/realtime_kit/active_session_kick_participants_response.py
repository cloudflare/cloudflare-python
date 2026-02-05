# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ActiveSessionKickParticipantsResponse", "Data", "DataParticipant"]


class DataParticipant(BaseModel):
    id: str
    """ID of the session participant"""

    created_at: str

    updated_at: str

    email: Optional[str] = None
    """Email of the session participant."""

    name: Optional[str] = None
    """Name of the session participant."""

    picture: Optional[str] = None
    """A URL pointing to a picture of the participant."""


class Data(BaseModel):
    action: Optional[str] = None

    participants: Optional[List[DataParticipant]] = None


class ActiveSessionKickParticipantsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
