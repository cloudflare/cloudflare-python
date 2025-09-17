# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["DNSResolverSettingsV4"]


class DNSResolverSettingsV4(BaseModel):
    ip: str
    """Specify the IPv4 address of the upstream resolver."""

    port: Optional[int] = None
    """Specify a port number to use for the upstream resolver.

    Defaults to 53 if unspecified.
    """

    route_through_private_network: Optional[bool] = None
    """Indicate whether to connect to this resolver over a private network.

    Must set when vnet_id set.
    """

    vnet_id: Optional[str] = None
    """Specify an optional virtual network for this resolver.

    Uses default virtual network id if omitted.
    """
