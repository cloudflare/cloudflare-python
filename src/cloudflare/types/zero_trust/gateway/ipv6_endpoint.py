# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .ipv6_network import IPV6Network

__all__ = ["IPV6Endpoint"]


class IPV6Endpoint(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""

    networks: Optional[List[IPV6Network]] = None
    """A list of allowed source IPv6 network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """
