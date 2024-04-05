# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .wan import WAN
from ...._models import BaseModel

__all__ = ["WANCreateResponse"]


class WANCreateResponse(BaseModel):
    wans: Optional[List[WAN]] = None
