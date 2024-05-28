# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["DiscoveryGetResponse"]


class DiscoveryGetResponse(BaseModel):
    schemas: Optional[List[object]] = None

    timestamp: Optional[datetime] = None
