# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .lan import LAN
from ...._models import BaseModel

__all__ = ["LANUpdateResponse"]


class LANUpdateResponse(BaseModel):
    lan: Optional[LAN] = None
