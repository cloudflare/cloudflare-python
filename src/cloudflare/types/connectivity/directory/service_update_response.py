# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = [
    "ServiceUpdateResponse",
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


class InfraHTTPServiceConfigHostInfraIPv4HostNetwork(BaseModel):
    tunnel_id: str


class InfraHTTPServiceConfigHostInfraIPv4Host(BaseModel):
    ipv4: str

    network: InfraHTTPServiceConfigHostInfraIPv4HostNetwork


class InfraHTTPServiceConfigHostInfraIPv6HostNetwork(BaseModel):
    tunnel_id: str


class InfraHTTPServiceConfigHostInfraIPv6Host(BaseModel):
    ipv6: str

    network: InfraHTTPServiceConfigHostInfraIPv6HostNetwork


class InfraHTTPServiceConfigHostInfraDualStackHostNetwork(BaseModel):
    tunnel_id: str


class InfraHTTPServiceConfigHostInfraDualStackHost(BaseModel):
    ipv4: str

    ipv6: str

    network: InfraHTTPServiceConfigHostInfraDualStackHostNetwork


class InfraHTTPServiceConfigHostInfraHostnameHostResolverNetwork(BaseModel):
    tunnel_id: str

    resolver_ips: Optional[List[str]] = None


class InfraHTTPServiceConfigHostInfraHostnameHost(BaseModel):
    hostname: str

    resolver_network: InfraHTTPServiceConfigHostInfraHostnameHostResolverNetwork


InfraHTTPServiceConfigHost: TypeAlias = Union[
    InfraHTTPServiceConfigHostInfraIPv4Host,
    InfraHTTPServiceConfigHostInfraIPv6Host,
    InfraHTTPServiceConfigHostInfraDualStackHost,
    InfraHTTPServiceConfigHostInfraHostnameHost,
]


class InfraHTTPServiceConfigTLSSettings(BaseModel):
    """TLS settings for a connectivity service."""

    cert_verification_mode: str
    """TLS certificate verification mode for the connection to the origin.

    - `"verify_full"` — verify certificate chain and hostname (default)
    - `"verify_ca"` — verify certificate chain only, skip hostname check
    - `"disabled"` — do not verify the server certificate at all

    `disabled` cannot be combined with `certificate_authority`: a custom CA is only
    used to verify the server certificate.
    """

    certificate_authority: Optional[str] = None
    """UUID of the custom CA certificate or chain."""

    client_certificate: Optional[str] = None
    """UUID of the mTLS client certificate and private key."""


class InfraHTTPServiceConfig(BaseModel):
    host: InfraHTTPServiceConfigHost

    name: str

    type: Literal["tcp", "http"]

    created_at: Optional[datetime] = None

    http_port: Optional[int] = None

    https_port: Optional[int] = None

    service_id: Optional[str] = None

    tls_settings: Optional[InfraHTTPServiceConfigTLSSettings] = None
    """TLS settings for a connectivity service."""

    updated_at: Optional[datetime] = None


class InfraTCPServiceConfigHostInfraIPv4HostNetwork(BaseModel):
    tunnel_id: str


class InfraTCPServiceConfigHostInfraIPv4Host(BaseModel):
    ipv4: str

    network: InfraTCPServiceConfigHostInfraIPv4HostNetwork


class InfraTCPServiceConfigHostInfraIPv6HostNetwork(BaseModel):
    tunnel_id: str


class InfraTCPServiceConfigHostInfraIPv6Host(BaseModel):
    ipv6: str

    network: InfraTCPServiceConfigHostInfraIPv6HostNetwork


class InfraTCPServiceConfigHostInfraDualStackHostNetwork(BaseModel):
    tunnel_id: str


class InfraTCPServiceConfigHostInfraDualStackHost(BaseModel):
    ipv4: str

    ipv6: str

    network: InfraTCPServiceConfigHostInfraDualStackHostNetwork


class InfraTCPServiceConfigHostInfraHostnameHostResolverNetwork(BaseModel):
    tunnel_id: str

    resolver_ips: Optional[List[str]] = None


class InfraTCPServiceConfigHostInfraHostnameHost(BaseModel):
    hostname: str

    resolver_network: InfraTCPServiceConfigHostInfraHostnameHostResolverNetwork


InfraTCPServiceConfigHost: TypeAlias = Union[
    InfraTCPServiceConfigHostInfraIPv4Host,
    InfraTCPServiceConfigHostInfraIPv6Host,
    InfraTCPServiceConfigHostInfraDualStackHost,
    InfraTCPServiceConfigHostInfraHostnameHost,
]


class InfraTCPServiceConfigTLSSettings(BaseModel):
    """TLS settings for a connectivity service."""

    cert_verification_mode: str
    """TLS certificate verification mode for the connection to the origin.

    - `"verify_full"` — verify certificate chain and hostname (default)
    - `"verify_ca"` — verify certificate chain only, skip hostname check
    - `"disabled"` — do not verify the server certificate at all

    `disabled` cannot be combined with `certificate_authority`: a custom CA is only
    used to verify the server certificate.
    """

    certificate_authority: Optional[str] = None
    """UUID of the custom CA certificate or chain."""

    client_certificate: Optional[str] = None
    """UUID of the mTLS client certificate and private key."""


class InfraTCPServiceConfig(BaseModel):
    host: InfraTCPServiceConfigHost

    name: str

    type: Literal["tcp", "http"]

    app_protocol: Optional[Literal["postgresql", "mysql"]] = None

    created_at: Optional[datetime] = None

    service_id: Optional[str] = None

    tcp_port: Optional[int] = None

    tls_settings: Optional[InfraTCPServiceConfigTLSSettings] = None
    """TLS settings for a connectivity service."""

    updated_at: Optional[datetime] = None


ServiceUpdateResponse: TypeAlias = Union[InfraHTTPServiceConfig, InfraTCPServiceConfig]
