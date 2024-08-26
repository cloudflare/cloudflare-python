# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ...._models import BaseModel
from .ip_network import IPNetwork

__all__ = ["DOHEndpoint"]


class DOHEndpoint(BaseModel):
    enabled: Optional[bool] = None
    """True if the endpoint is enabled for this location."""

    networks: Optional[List[IPNetwork]] = None
    """A list of allowed source IP network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """

    require_token: Optional[bool] = None
    """
    True if the endpoint requires
    [user identity](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/agentless/dns/dns-over-https/#filter-doh-requests-by-user)
    authentication.
    """
