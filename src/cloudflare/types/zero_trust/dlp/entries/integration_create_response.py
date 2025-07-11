# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["IntegrationCreateResponse"]


class IntegrationCreateResponse(BaseModel):
    id: str

    created_at: datetime

    enabled: bool

    name: str

    updated_at: datetime

    profile_id: Optional[str] = None
