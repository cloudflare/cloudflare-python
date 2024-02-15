# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TokenUserAPITokensCreateTokenResponse"]


class TokenUserAPITokensCreateTokenResponse(BaseModel):
    value: Optional[str] = None
    """The token value."""
