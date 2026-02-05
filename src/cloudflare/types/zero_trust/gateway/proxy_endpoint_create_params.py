# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "ProxyEndpointCreateParams",
    "ZeroTrustGatewayProxyEndpointIPCreate",
    "ZeroTrustGatewayProxyEndpointIdentityCreate",
]


class ZeroTrustGatewayProxyEndpointIPCreate(TypedDict, total=False):
    account_id: Required[str]

    name: Required[str]
    """Specify the name of the proxy endpoint."""

    kind: Literal["ip"]
    """The proxy endpoint kind"""


class ZeroTrustGatewayProxyEndpointIdentityCreate(TypedDict, total=False):
    account_id: Required[str]

    kind: Required[Literal["identity"]]
    """The proxy endpoint kind"""

    name: Required[str]
    """Specify the name of the proxy endpoint."""


ProxyEndpointCreateParams: TypeAlias = Union[
    ZeroTrustGatewayProxyEndpointIPCreate, ZeroTrustGatewayProxyEndpointIdentityCreate
]
