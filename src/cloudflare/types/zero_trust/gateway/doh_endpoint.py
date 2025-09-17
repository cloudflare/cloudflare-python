# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .ip_network import IPNetwork

__all__ = ["DOHEndpoint"]


class DOHEndpoint(BaseModel):
    enabled: Optional[bool] = None
    """Indicate whether the DOH endpoint is enabled for this location."""

    networks: Optional[List[IPNetwork]] = None
    """Specify the list of allowed source IP network ranges for this endpoint.

    When the list is empty, the endpoint allows all source IPs. The list takes
    effect only if the endpoint is enabled for this location.
    """

    require_token: Optional[bool] = None
    """Specify whether the DOH endpoint requires user identity authentication."""
