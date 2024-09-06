# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, Dict

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DHCPServer"]


class DHCPServer(BaseModel):
    dhcp_pool_end: Optional[str] = None
    """A valid IPv4 address."""

    dhcp_pool_start: Optional[str] = None
    """A valid IPv4 address."""

    dns_server: Optional[str] = None
    """A valid IPv4 address."""

    reservations: Optional[Dict[str, str]] = None
    """Mapping of MAC addresses to IP addresses"""
