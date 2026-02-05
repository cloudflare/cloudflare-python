# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["MeetingRefreshParticipantTokenResponse", "Data"]


class Data(BaseModel):
    """Data returned by the operation"""

    token: str
    """Regenerated participant's authentication token."""


class MeetingRefreshParticipantTokenResponse(BaseModel):
    data: Data
    """Data returned by the operation"""

    success: bool
    """Success status of the operation"""
