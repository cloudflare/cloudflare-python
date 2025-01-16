# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ValidateDestinationResponse"]


class ValidateDestinationResponse(BaseModel):
    message: Optional[str] = None

    valid: Optional[bool] = None
