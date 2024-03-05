# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["StreamKeys"]


class StreamKeys(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""

    jwk: Optional[str] = None
    """The signing key in JWK format."""

    pem: Optional[str] = None
    """The signing key in PEM format."""
