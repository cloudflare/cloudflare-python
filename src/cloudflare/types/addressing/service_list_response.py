# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ServiceListResponse"]


class ServiceListResponse(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    name: Optional[str] = None
    """Name of a service running on the Cloudflare network"""
