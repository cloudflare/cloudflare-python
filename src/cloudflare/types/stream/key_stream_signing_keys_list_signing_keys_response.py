# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["KeyStreamSigningKeysListSigningKeysResponse", "KeyStreamSigningKeysListSigningKeysResponseItem"]


class KeyStreamSigningKeysListSigningKeysResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""


KeyStreamSigningKeysListSigningKeysResponse = List[KeyStreamSigningKeysListSigningKeysResponseItem]
