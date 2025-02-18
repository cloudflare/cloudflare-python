# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ....._models import BaseModel

__all__ = ["IPRule", "IP"]


class IP(BaseModel):
    ip: str
    """An IPv4 or IPv6 CIDR block."""


class IPRule(BaseModel):
    ip: IP
