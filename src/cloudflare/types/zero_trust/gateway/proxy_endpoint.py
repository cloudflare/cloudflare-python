# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from ...._utils import PropertyInfo
from ...._models import BaseModel
from .gateway_ips import GatewayIPs

__all__ = ["ProxyEndpoint", "ZeroTrustGatewayProxyEndpointIP", "ZeroTrustGatewayProxyEndpointIdentity"]


class ZeroTrustGatewayProxyEndpointIP(BaseModel):
    ips: List[GatewayIPs]
    """Specify the list of CIDRs to restrict ingress connections."""

    name: str
    """Specify the name of the proxy endpoint."""

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    kind: Optional[Literal["ip"]] = None
    """The proxy endpoint kind"""

    subdomain: Optional[str] = None
    """Specify the subdomain to use as the destination in the proxy client."""

    updated_at: Optional[datetime] = None


class ZeroTrustGatewayProxyEndpointIdentity(BaseModel):
    kind: Literal["identity"]
    """The proxy endpoint kind"""

    name: str
    """Specify the name of the proxy endpoint."""

    id: Optional[str] = None

    created_at: Optional[datetime] = None

    subdomain: Optional[str] = None
    """Specify the subdomain to use as the destination in the proxy client."""

    updated_at: Optional[datetime] = None


ProxyEndpoint: TypeAlias = Annotated[
    Union[ZeroTrustGatewayProxyEndpointIP, ZeroTrustGatewayProxyEndpointIdentity], PropertyInfo(discriminator="kind")
]
