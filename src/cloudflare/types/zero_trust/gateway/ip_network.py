# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

__all__ = ["IPNetwork"]


class IPNetwork(BaseModel):
    network: str
    """Specify the IP address or IP CIDR."""
