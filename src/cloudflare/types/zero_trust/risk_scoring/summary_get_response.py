# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from datetime import datetime

from typing_extensions import Literal

from typing import List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["SummaryGetResponse", "User"]


class User(BaseModel):
    email: str

    event_count: int

    last_event: datetime

    max_risk_level: Literal["low", "medium", "high"]

    name: str

    user_id: str


class SummaryGetResponse(BaseModel):
    users: List[User]
