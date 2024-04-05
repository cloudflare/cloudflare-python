# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .lan import LAN
from ...._models import BaseModel

__all__ = ["LANGetResponse"]


class LANGetResponse(BaseModel):
    lan: Optional[LAN] = None
