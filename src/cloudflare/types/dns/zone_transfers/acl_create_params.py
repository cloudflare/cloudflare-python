# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ACLCreateParams"]


class ACLCreateParams(TypedDict, total=False):
    account_id: Required[str]

    ip_range: Required[str]
    """Allowed IPv4/IPv6 address range of primary or secondary nameservers.

    This will be applied for the entire account. The IP range is used to allow
    additional NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR
    requests from for primary zones. CIDRs are limited to a maximum of /24 for IPv4
    and /64 for IPv6 respectively.
    """

    name: Required[str]
    """The name of the acl."""
