# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["DataTagCategoryCreateResponse", "Tag"]


class Tag(BaseModel):
    id: str

    created_at: datetime

    name: str

    updated_at: datetime

    description: Optional[str] = None


class DataTagCategoryCreateResponse(BaseModel):
    id: str

    created_at: datetime

    name: str

    tags: List[Tag]

    updated_at: datetime

    description: Optional[str] = None

    template_id: Optional[str] = None
