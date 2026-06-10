# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["DataClassGetResponse", "SensitivityLevel"]


class SensitivityLevel(BaseModel):
    """
    A reference pairing a sensitivity group with a specific level within that group.
    """

    group_id: str

    level_id: str


class DataClassGetResponse(BaseModel):
    id: str

    created_at: datetime

    data_tags: List[str]

    expression: str

    name: str

    sensitivity_levels: List[SensitivityLevel]

    updated_at: datetime

    description: Optional[str] = None
