# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["SummaryGetResponse", "User"]


class User(BaseModel):
    email: str

    event_count: int

    last_event: datetime

    max_risk_level: Optional[Literal["low", "medium", "high"]] = None

    name: str

    user_id: str
    """The ID for a user"""


class SummaryGetResponse(BaseModel):
    users: Optional[List[User]] = None
