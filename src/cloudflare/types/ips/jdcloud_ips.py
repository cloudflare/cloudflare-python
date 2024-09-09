# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["JDCloudIPs"]


class JDCloudIPs(BaseModel):
    etag: Optional[str] = None
    """A digest of the IP data. Useful for determining if the data has changed."""

    ipv4_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv4 CIDR addresses."""

    ipv6_cidrs: Optional[List[str]] = None
    """List of Cloudflare IPv6 CIDR addresses."""

    jdcloud_cidrs: Optional[List[str]] = None
    """List IPv4 and IPv6 CIDRs, only populated if `?networks=jdcloud` is used."""
