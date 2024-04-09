# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .tokens import Value
from ..._models import BaseModel

__all__ = ["TokenCreateResponse"]


class TokenCreateResponse(BaseModel):
    value: Optional[Value] = None
    """The token value."""
