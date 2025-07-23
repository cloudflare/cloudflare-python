# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel
from .doh_endpoint import DOHEndpoint
from .dot_endpoint import DOTEndpoint
from .ipv4_endpoint import IPV4Endpoint
from .ipv6_endpoint import IPV6Endpoint

__all__ = ["Endpoint"]


class Endpoint(BaseModel):
    doh: DOHEndpoint

    dot: DOTEndpoint

    ipv4: IPV4Endpoint

    ipv6: IPV6Endpoint
