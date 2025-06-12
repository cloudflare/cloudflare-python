# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from ..._models import BaseModel

__all__ = ["IPs", "IPItem"]


class IPItem(BaseModel):
    created_at: Optional[datetime] = None

    ip: Optional[str] = None
    """An IPv4 or IPv6 address."""


IPs: TypeAlias = List[IPItem]
