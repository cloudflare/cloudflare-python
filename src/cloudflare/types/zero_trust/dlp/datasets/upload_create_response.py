# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ....._models import BaseModel

__all__ = ["UploadCreateResponse"]


class UploadCreateResponse(BaseModel):
    max_cells: int

    version: int

    secret: Optional[str] = None
