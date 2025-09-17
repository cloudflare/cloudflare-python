# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ...._models import BaseModel
from .gateway_ips import GatewayIPs

__all__ = ["ProxyEndpoint"]


class ProxyEndpoint(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    ips: Optional[List[GatewayIPs]] = None
    """Specify the list of CIDRs to restrict ingress connections."""

    name: Optional[str] = None
    """Specify the name of the proxy endpoint."""

    subdomain: Optional[str] = None
    """Specify the subdomain to use as the destination in the proxy client."""

    updated_at: Optional[datetime] = None
