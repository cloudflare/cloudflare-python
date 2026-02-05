# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .ip_network import IPNetwork

__all__ = ["DOTEndpoint"]


class DOTEndpoint(BaseModel):
    enabled: Optional[bool] = None
    """Indicate whether the DOT endpoint is enabled for this location."""

    networks: Optional[List[IPNetwork]] = None
    """Specify the list of allowed source IP network ranges for this endpoint.

    When the list is empty, the endpoint allows all source IPs. The list takes
    effect only if the endpoint is enabled for this location.
    """
