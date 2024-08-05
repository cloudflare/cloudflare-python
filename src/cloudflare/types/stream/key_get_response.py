# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["KeyGetResponse", "KeyGetResponseItem"]


class KeyGetResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    created: Optional[datetime] = None
    """The date and time a signing key was created."""


KeyGetResponse: TypeAlias = List[KeyGetResponseItem]
