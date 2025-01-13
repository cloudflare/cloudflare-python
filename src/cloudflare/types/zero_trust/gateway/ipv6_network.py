# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from ...._models import BaseModel

__all__ = ["IPV6Network"]


class IPV6Network(BaseModel):
    network: str
    """The IPv6 address or IPv6 CIDR."""
