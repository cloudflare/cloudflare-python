# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["JobGetResponse"]


class JobGetResponse(BaseModel):
    id: str

    source: Literal["user", "schedule"]

    end_reason: Optional[str] = None

    ended_at: Optional[str] = None

    last_seen_at: Optional[str] = None

    started_at: Optional[str] = None
