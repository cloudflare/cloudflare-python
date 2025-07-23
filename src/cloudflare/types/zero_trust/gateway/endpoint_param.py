# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .doh_endpoint_param import DOHEndpointParam
from .dot_endpoint_param import DOTEndpointParam
from .ipv4_endpoint_param import IPV4EndpointParam
from .ipv6_endpoint_param import IPV6EndpointParam

__all__ = ["EndpointParam"]


class EndpointParam(TypedDict, total=False):
    doh: Required[DOHEndpointParam]

    dot: Required[DOTEndpointParam]

    ipv4: Required[IPV4EndpointParam]

    ipv6: Required[IPV6EndpointParam]
