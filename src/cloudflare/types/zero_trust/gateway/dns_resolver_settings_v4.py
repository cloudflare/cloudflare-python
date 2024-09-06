# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DNSResolverSettingsV4"]


class DNSResolverSettingsV4(BaseModel):
    ip: str
    """IPv4 address of upstream resolver."""

    port: Optional[int] = None
    """A port number to use for upstream resolver. Defaults to 53 if unspecified."""

    route_through_private_network: Optional[bool] = None
    """Whether to connect to this resolver over a private network.

    Must be set when vnet_id is set.
    """

    vnet_id: Optional[str] = None
    """Optionally specify a virtual network for this resolver.

    Uses default virtual network id if omitted.
    """
