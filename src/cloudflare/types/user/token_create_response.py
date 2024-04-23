# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .tokens.value import Value

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    value: Optional[Value] = None
    """The token value."""
