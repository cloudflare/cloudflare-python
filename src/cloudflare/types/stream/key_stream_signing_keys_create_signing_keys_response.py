# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["KeyStreamSigningKeysCreateSigningKeysResponse"]


class KeyStreamSigningKeysCreateSigningKeysResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""

    jwk: Optional[str] = None
    """The signing key in JWK format."""

    pem: Optional[str] = None
    """The signing key in PEM format."""
