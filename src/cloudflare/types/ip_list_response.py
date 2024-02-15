# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["IPListResponse", "AddressingIPs", "AddressingIPsJdcloud"]


class AddressingIPs(BaseModel):
    etag: Optional[str] = None
    """A digest of the IP data. Useful for determining if the data has changed."""

    ipv4_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv4 CIDR addresses."""

    ipv6_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv6 CIDR addresses."""


class AddressingIPsJdcloud(BaseModel):
    etag: Optional[str] = None
    """A digest of the IP data. Useful for determining if the data has changed."""

    ipv4_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv4 CIDR addresses."""

    ipv6_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv6 CIDR addresses."""

    jdcloud_cidrs: Optional[List[str]] = None
    """List IPv4 and IPv6 CIDRs, only populated if `?networks=jdcloud` is used."""


IPListResponse = Union[AddressingIPs, AddressingIPsJdcloud]
