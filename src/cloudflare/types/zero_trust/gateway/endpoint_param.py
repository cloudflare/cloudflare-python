# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .doh_endpoint_param import DOHEndpointParam
from .dot_endpoint_param import DOTEndpointParam
from .ipv4_endpoint_param import IPV4EndpointParam
from .ipv6_endpoint_param import IPV6EndpointParam

__all__ = ["EndpointParam"]


class EndpointParam(TypedDict, total=False):
    doh: DOHEndpointParam

    dot: DOTEndpointParam

    ipv4: IPV4EndpointParam

    ipv6: IPV6EndpointParam
