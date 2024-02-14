# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import TypedDict, Required

from typing import List

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from ..._types import FileTypes
from ..._utils import PropertyInfo
from ...types import shared_params

__all__ = ["ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointParams"]


class ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointParams(TypedDict, total=False):
    ips: Required[List[str]]
    """A list of CIDRs to restrict ingress connections."""

    name: Required[str]
    """The name of the proxy endpoint."""

    subdomain: str
    """The subdomain to be used as the destination in the proxy client."""
