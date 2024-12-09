# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CommandListResponse", "Command"]


class Command(BaseModel):
    id: Optional[str] = None

    completed_date: Optional[datetime] = None

    created_date: Optional[datetime] = None

    device_id: Optional[str] = None

    filename: Optional[str] = None

    status: Optional[str] = None

    type: Optional[str] = None

    user_email: Optional[str] = None


class CommandListResponse(BaseModel):
    commands: Optional[List[Command]] = None
