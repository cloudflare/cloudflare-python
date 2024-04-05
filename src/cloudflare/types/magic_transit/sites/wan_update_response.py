# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .wan import WAN
from ...._models import BaseModel

__all__ = ["WANUpdateResponse"]


class WANUpdateResponse(BaseModel):
    wan: Optional[WAN] = None
