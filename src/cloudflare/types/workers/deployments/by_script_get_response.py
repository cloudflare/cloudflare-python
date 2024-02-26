# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["ByScriptGetResponse"]


class ByScriptGetResponse(BaseModel):
    id: Optional[str] = None

    metadata: Optional[object] = None

    number: Optional[float] = None

    resources: Optional[object] = None
