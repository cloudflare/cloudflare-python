# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SubscriptionListResponse", "Lag", "StartAt"]


class Lag(BaseModel):
    records: Optional[str] = None
    """
    Decimal-string distance from the subscription's committed position to the
    observed exclusive stream tail, in records. Includes in-flight records and may
    include expired records or records acknowledged beyond an earlier gap. Null
    unless status is available.
    """

    status: Literal["available", "unsupported", "unavailable"]
    """
    Unsupported means the subscription or stream topology cannot be measured;
    unavailable means a required observation failed or was inconsistent.
    """


class StartAt(BaseModel):
    type: Literal["earliest", "latest"]


class SubscriptionListResponse(BaseModel):
    id: str

    created_at: datetime

    lag: Lag

    modified_at: datetime

    name: str

    start_at: StartAt
