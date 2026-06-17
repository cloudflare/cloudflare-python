# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TokenRotateResponse"]


class TokenRotateResponse(BaseModel):
    token: str
    """New token value (shown once). Treat as sensitive."""

    type: Literal["publish_subscribe", "subscribe"]
