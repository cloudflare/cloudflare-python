# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["OAuthClientRotateSecretResponse"]


class OAuthClientRotateSecretResponse(BaseModel):
    client_secret: Optional[str] = None
    """The new client secret."""
