# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ...._models import BaseModel

__all__ = ["PatternValidateResponse"]


class PatternValidateResponse(BaseModel):
    valid: Optional[bool] = None
