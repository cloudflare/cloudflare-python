# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from datetime import datetime

from .gateway_ips import GatewayIPs

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ProxyEndpoint"]

class ProxyEndpoint(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = None

    ips: Optional[List[GatewayIPs]] = None
    """A list of CIDRs to restrict ingress connections."""

    name: Optional[str] = None
    """The name of the proxy endpoint."""

    subdomain: Optional[str] = None
    """The subdomain to be used as the destination in the proxy client."""

    updated_at: Optional[datetime] = None