# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["ACL"]


class ACL(BaseModel):
    id: str

    ip_range: str
    """Allowed IPv4/IPv6 address range of primary or secondary nameservers.

    This will be applied for the entire account. The IP range is used to allow
    additional NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR
    requests from for primary zones. CIDRs are limited to a maximum of /24 for IPv4
    and /64 for IPv6 respectively.
    """

    name: str
    """The name of the acl."""
