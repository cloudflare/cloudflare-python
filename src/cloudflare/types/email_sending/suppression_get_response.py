# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["SuppressionGetResponse"]


class SuppressionGetResponse(BaseModel):
    id: str

    created_at: datetime

    email: str

    expires_at: Optional[datetime] = None

    read_only: bool
    """Whether clients may mutate this suppression.

    This is determined by the server and must not be inferred from `reason`.
    """

    reason: str

    note: Optional[str] = None
