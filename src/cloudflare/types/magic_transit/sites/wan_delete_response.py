# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .wan import WAN
from ...._models import BaseModel

__all__ = ["WANDeleteResponse"]


class WANDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_wan: Optional[WAN] = None
