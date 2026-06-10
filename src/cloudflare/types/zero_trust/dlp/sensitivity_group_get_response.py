# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["SensitivityGroupGetResponse", "Level"]


class Level(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    description: Optional[str] = None


class SensitivityGroupGetResponse(BaseModel):
    id: str

    created_at: datetime

    levels: List[Level]

    name: str

    updated_at: datetime

    description: Optional[str] = None

    template_id: Optional[str] = None
