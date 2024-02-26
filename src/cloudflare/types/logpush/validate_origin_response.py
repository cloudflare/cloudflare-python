# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ValidateOriginResponse"]


class ValidateOriginResponse(BaseModel):
    message: Optional[str] = None

    valid: Optional[bool] = None
