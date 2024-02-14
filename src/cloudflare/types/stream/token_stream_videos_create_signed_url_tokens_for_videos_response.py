# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["TokenStreamVideosCreateSignedURLTokensForVideosResponse"]


class TokenStreamVideosCreateSignedURLTokensForVideosResponse(BaseModel):
    token: Optional[str] = None
    """The signed token used with the signed URLs feature."""
