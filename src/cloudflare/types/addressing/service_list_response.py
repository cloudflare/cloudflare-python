# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["ServiceListResponse", "ServiceListResponseItem"]


class ServiceListResponseItem(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Name of a service running on the Cloudflare network"""


ServiceListResponse = List[ServiceListResponseItem]
