# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ....._types import SequenceNotStr

__all__ = [
    "ServiceUpdateParams",
    "Host",
    "HostInfraIPv4Host",
    "HostInfraIPv4HostNetwork",
    "HostInfraIPv6Host",
    "HostInfraIPv6HostNetwork",
    "HostInfraDualStackHost",
    "HostInfraDualStackHostNetwork",
    "HostInfraHostnameHost",
    "HostInfraHostnameHostResolverNetwork",
]


class ServiceUpdateParams(TypedDict, total=False):
    account_id: Required[str]

    host: Required[Host]

    name: Required[str]

    type: Required[Literal["http"]]

    http_port: Optional[int]

    https_port: Optional[int]


class HostInfraIPv4HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class HostInfraIPv4Host(TypedDict, total=False):
    ipv4: Required[str]

    network: Required[HostInfraIPv4HostNetwork]


class HostInfraIPv6HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class HostInfraIPv6Host(TypedDict, total=False):
    ipv6: Required[str]

    network: Required[HostInfraIPv6HostNetwork]


class HostInfraDualStackHostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class HostInfraDualStackHost(TypedDict, total=False):
    ipv4: Required[str]

    ipv6: Required[str]

    network: Required[HostInfraDualStackHostNetwork]


class HostInfraHostnameHostResolverNetwork(TypedDict, total=False):
    tunnel_id: Required[str]

    resolver_ips: Optional[SequenceNotStr[str]]


class HostInfraHostnameHost(TypedDict, total=False):
    hostname: Required[str]

    resolver_network: Required[HostInfraHostnameHostResolverNetwork]


Host: TypeAlias = Union[HostInfraIPv4Host, HostInfraIPv6Host, HostInfraDualStackHost, HostInfraHostnameHost]
