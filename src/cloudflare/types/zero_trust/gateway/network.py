# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["Network"]


class Network(BaseModel):
    network: str
    """The IPv4 address or IPv4 CIDR. IPv4 CIDRs are limited to a maximum of /24."""
