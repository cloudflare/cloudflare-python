# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .key import Key
from ...._models import BaseModel

__all__ = ["KeyUpdateResponse"]


class KeyUpdateResponse(BaseModel):
    keys: Optional[List[Key]] = None
