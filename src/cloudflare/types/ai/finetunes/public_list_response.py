# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ...._models import BaseModel

__all__ = ["PublicListResponse"]


class PublicListResponse(BaseModel):
    id: str

    created_at: datetime

    model: str

    modified_at: datetime

    name: str

    public: bool

    description: Optional[str] = None
