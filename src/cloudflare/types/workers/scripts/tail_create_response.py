# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TailCreateResponse"]


class TailCreateResponse(BaseModel):
    id: Optional[str] = None

    expires_at: Optional[str] = None

    url: Optional[str] = None
