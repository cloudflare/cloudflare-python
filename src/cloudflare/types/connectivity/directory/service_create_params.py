# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ...._types import SequenceNotStr

__all__ = [
    "ServiceCreateParams",
    "InfraHTTPServiceConfig",
    "InfraHTTPServiceConfigHost",
    "InfraHTTPServiceConfigHostInfraIPv4Host",
    "InfraHTTPServiceConfigHostInfraIPv4HostNetwork",
    "InfraHTTPServiceConfigHostInfraIPv6Host",
    "InfraHTTPServiceConfigHostInfraIPv6HostNetwork",
    "InfraHTTPServiceConfigHostInfraDualStackHost",
    "InfraHTTPServiceConfigHostInfraDualStackHostNetwork",
    "InfraHTTPServiceConfigHostInfraHostnameHost",
    "InfraHTTPServiceConfigHostInfraHostnameHostResolverNetwork",
    "InfraHTTPServiceConfigTLSSettings",
    "InfraTCPServiceConfig",
    "InfraTCPServiceConfigHost",
    "InfraTCPServiceConfigHostInfraIPv4Host",
    "InfraTCPServiceConfigHostInfraIPv4HostNetwork",
    "InfraTCPServiceConfigHostInfraIPv6Host",
    "InfraTCPServiceConfigHostInfraIPv6HostNetwork",
    "InfraTCPServiceConfigHostInfraDualStackHost",
    "InfraTCPServiceConfigHostInfraDualStackHostNetwork",
    "InfraTCPServiceConfigHostInfraHostnameHost",
    "InfraTCPServiceConfigHostInfraHostnameHostResolverNetwork",
    "InfraTCPServiceConfigTLSSettings",
]


class InfraHTTPServiceConfig(TypedDict, total=False):
    account_id: str
    """Account identifier"""

    host: Required[InfraHTTPServiceConfigHost]

    name: Required[str]

    type: Required[Literal["tcp", "http"]]

    http_port: Optional[int]

    https_port: Optional[int]

    tls_settings: Optional[InfraHTTPServiceConfigTLSSettings]
    """TLS settings for a connectivity service.

    If omitted, the default mode (`verify_full`) is used.
    """


class InfraHTTPServiceConfigHostInfraIPv4HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraHTTPServiceConfigHostInfraIPv4Host(TypedDict, total=False):
    ipv4: Required[str]

    network: Required[InfraHTTPServiceConfigHostInfraIPv4HostNetwork]


class InfraHTTPServiceConfigHostInfraIPv6HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraHTTPServiceConfigHostInfraIPv6Host(TypedDict, total=False):
    ipv6: Required[str]

    network: Required[InfraHTTPServiceConfigHostInfraIPv6HostNetwork]


class InfraHTTPServiceConfigHostInfraDualStackHostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraHTTPServiceConfigHostInfraDualStackHost(TypedDict, total=False):
    ipv4: Required[str]

    ipv6: Required[str]

    network: Required[InfraHTTPServiceConfigHostInfraDualStackHostNetwork]


class InfraHTTPServiceConfigHostInfraHostnameHostResolverNetwork(TypedDict, total=False):
    tunnel_id: Required[str]

    resolver_ips: Optional[SequenceNotStr[str]]


class InfraHTTPServiceConfigHostInfraHostnameHost(TypedDict, total=False):
    hostname: Required[str]

    resolver_network: Required[InfraHTTPServiceConfigHostInfraHostnameHostResolverNetwork]


InfraHTTPServiceConfigHost: TypeAlias = Union[
    InfraHTTPServiceConfigHostInfraIPv4Host,
    InfraHTTPServiceConfigHostInfraIPv6Host,
    InfraHTTPServiceConfigHostInfraDualStackHost,
    InfraHTTPServiceConfigHostInfraHostnameHost,
]


class InfraHTTPServiceConfigTLSSettings(TypedDict, total=False):
    """TLS settings for a connectivity service.

    If omitted, the default mode (`verify_full`) is used.
    """

    cert_verification_mode: Required[str]
    """TLS certificate verification mode for the connection to the origin.

    - `"verify_full"` — verify certificate chain and hostname (default)
    - `"verify_ca"` — verify certificate chain only, skip hostname check
    - `"disabled"` — do not verify the server certificate at all
    """


class InfraTCPServiceConfig(TypedDict, total=False):
    account_id: str
    """Account identifier"""

    host: Required[InfraTCPServiceConfigHost]

    name: Required[str]

    type: Required[Literal["tcp", "http"]]

    app_protocol: Optional[Literal["postgresql", "mysql"]]

    tcp_port: Optional[int]

    tls_settings: Optional[InfraTCPServiceConfigTLSSettings]
    """TLS settings for a connectivity service.

    If omitted, the default mode (`verify_full`) is used.
    """


class InfraTCPServiceConfigHostInfraIPv4HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraTCPServiceConfigHostInfraIPv4Host(TypedDict, total=False):
    ipv4: Required[str]

    network: Required[InfraTCPServiceConfigHostInfraIPv4HostNetwork]


class InfraTCPServiceConfigHostInfraIPv6HostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraTCPServiceConfigHostInfraIPv6Host(TypedDict, total=False):
    ipv6: Required[str]

    network: Required[InfraTCPServiceConfigHostInfraIPv6HostNetwork]


class InfraTCPServiceConfigHostInfraDualStackHostNetwork(TypedDict, total=False):
    tunnel_id: Required[str]


class InfraTCPServiceConfigHostInfraDualStackHost(TypedDict, total=False):
    ipv4: Required[str]

    ipv6: Required[str]

    network: Required[InfraTCPServiceConfigHostInfraDualStackHostNetwork]


class InfraTCPServiceConfigHostInfraHostnameHostResolverNetwork(TypedDict, total=False):
    tunnel_id: Required[str]

    resolver_ips: Optional[SequenceNotStr[str]]


class InfraTCPServiceConfigHostInfraHostnameHost(TypedDict, total=False):
    hostname: Required[str]

    resolver_network: Required[InfraTCPServiceConfigHostInfraHostnameHostResolverNetwork]


InfraTCPServiceConfigHost: TypeAlias = Union[
    InfraTCPServiceConfigHostInfraIPv4Host,
    InfraTCPServiceConfigHostInfraIPv6Host,
    InfraTCPServiceConfigHostInfraDualStackHost,
    InfraTCPServiceConfigHostInfraHostnameHost,
]


class InfraTCPServiceConfigTLSSettings(TypedDict, total=False):
    """TLS settings for a connectivity service.

    If omitted, the default mode (`verify_full`) is used.
    """

    cert_verification_mode: Required[str]
    """TLS certificate verification mode for the connection to the origin.

    - `"verify_full"` — verify certificate chain and hostname (default)
    - `"verify_ca"` — verify certificate chain only, skip hostname check
    - `"disabled"` — do not verify the server certificate at all
    """


ServiceCreateParams: TypeAlias = Union[InfraHTTPServiceConfig, InfraTCPServiceConfig]
