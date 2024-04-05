# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .lan import LAN
from ...._models import BaseModel

__all__ = ["LANCreateResponse"]


class LANCreateResponse(BaseModel):
    lans: Optional[List[LAN]] = None
