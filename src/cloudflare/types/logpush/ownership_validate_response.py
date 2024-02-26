# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OwnershipValidateResponse"]


class OwnershipValidateResponse(BaseModel):
    valid: Optional[bool] = None
