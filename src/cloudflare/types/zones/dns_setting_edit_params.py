# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .nameserver_param import NameserverParam

__all__ = ["DNSSettingEditParams"]


class DNSSettingEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    foundation_dns: bool
    """Whether to enable Foundation DNS Advanced Nameservers on the zone."""

    multi_provider: bool
    """
    Whether to enable multi-provider DNS, which causes Cloudflare to activate the
    zone even when non-Cloudflare NS records exist, and to respect NS records at the
    zone apex during outbound zone transfers.
    """

    nameservers: NameserverParam
    """
    Settings determining the nameservers through which the zone should be available.
    """

    secondary_overrides: bool
    """
    Allows a Secondary DNS zone to use (proxied) override records and CNAME
    flattening at the zone apex.
    """
