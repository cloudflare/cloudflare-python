# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .nameserver import Nameserver

__all__ = ["DNSSetting"]


class DNSSetting(BaseModel):
    foundation_dns: Optional[bool] = None
    """Whether to enable Foundation DNS Advanced Nameservers on the zone."""

    multi_provider: Optional[bool] = None
    """
    Whether to enable multi-provider DNS, which causes Cloudflare to activate the
    zone even when non-Cloudflare NS records exist, and to respect NS records at the
    zone apex during outbound zone transfers.
    """

    nameservers: Optional[Nameserver] = None
    """
    Settings determining the nameservers through which the zone should be available.
    """

    secondary_overrides: Optional[bool] = None
    """
    Allows a Secondary DNS zone to use (proxied) override records and CNAME
    flattening at the zone apex.
    """
