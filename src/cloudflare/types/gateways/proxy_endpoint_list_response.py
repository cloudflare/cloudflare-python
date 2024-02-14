# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["ProxyEndpointListResponse"]


class ProxyEndpointListResponse(BaseModel):
    id: Optional[object] = None

    created_at: Optional[datetime] = None

    ips: Optional[List[str]] = None
    """A list of CIDRs to restrict ingress connections."""

    name: Optional[str] = None
    """The name of the proxy endpoint."""

    subdomain: Optional[str] = None
    """The subdomain to be used as the destination in the proxy client."""

    updated_at: Optional[datetime] = None
