# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ActiveSessionKickAllParticipantsResponse", "Data"]


class Data(BaseModel):
    action: Optional[str] = None

    kicked_participants_count: Optional[float] = None


class ActiveSessionKickAllParticipantsResponse(BaseModel):
    data: Optional[Data] = None

    success: Optional[bool] = None
