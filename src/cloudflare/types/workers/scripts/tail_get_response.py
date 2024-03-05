# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["TailGetResponse"]


class TailGetResponse(BaseModel):
    id: Optional[object] = None

    expires_at: Optional[object] = None

    url: Optional[object] = None
