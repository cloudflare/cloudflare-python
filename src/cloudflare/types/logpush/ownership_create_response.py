# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OwnershipCreateResponse"]


class OwnershipCreateResponse(BaseModel):
    filename: Optional[str] = None

    message: Optional[str] = None

    valid: Optional[bool] = None
