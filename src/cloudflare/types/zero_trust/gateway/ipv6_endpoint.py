# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .ipv6_network import IPV6Network

__all__ = ["IPV6Endpoint"]


class IPV6Endpoint(BaseModel):
    enabled: Optional[bool] = None
    """Indicate whether the IPV6 endpoint is enabled for this location."""

    networks: Optional[List[IPV6Network]] = None
    """Specify the list of allowed source IPv6 network ranges for this endpoint.

    When the list is empty, the endpoint allows all source IPs. The list takes
    effect only if the endpoint is enabled for this location.
    """
