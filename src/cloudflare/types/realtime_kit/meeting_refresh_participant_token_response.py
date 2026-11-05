# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from ..._models import BaseModel

__all__ = ["MeetingRefreshParticipantTokenResponse", "Data"]


class Data(BaseModel):
    """Data returned by the operation"""

    token: str
    """Regenerated participant's authentication token."""

    expires_on: datetime
    """Time at which the token stops being valid, in UTC."""

    not_before: datetime
    """Time from which the token is valid, in UTC."""


class MeetingRefreshParticipantTokenResponse(BaseModel):
    data: Data
    """Data returned by the operation"""

    success: bool
    """Success status of the operation"""
