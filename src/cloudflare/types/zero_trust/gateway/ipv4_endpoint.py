# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["IPV4Endpoint"]


class IPV4Endpoint(BaseModel):
    enabled: Optional[bool] = None
    """Indicate whether the IPv4 endpoint is enabled for this location."""
