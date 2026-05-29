# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["CustomPromptTopic"]


class CustomPromptTopic(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    topic: str

    updated_at: datetime

    description: Optional[str] = None

    profile_id: Optional[str] = None
