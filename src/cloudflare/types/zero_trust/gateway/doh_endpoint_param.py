# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import TypedDict

from .ip_network_param import IPNetworkParam

__all__ = ["DOHEndpointParam"]


class DOHEndpointParam(TypedDict, total=False):
    enabled: bool
    """True if the endpoint is enabled for this location."""

    networks: Iterable[IPNetworkParam]
    """A list of allowed source IP network ranges for this endpoint.

    When empty, all source IPs are allowed. A non-empty list is only effective if
    the endpoint is enabled for this location.
    """

    require_token: bool
    """
    True if the endpoint requires
    [user identity](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/agentless/dns/dns-over-https/#filter-doh-requests-by-user)
    authentication.
    """
