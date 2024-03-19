# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TailCreateResponse"]


class TailCreateResponse(BaseModel):
    id: Optional[object] = None

    expires_at: Optional[object] = None

    url: Optional[object] = None
