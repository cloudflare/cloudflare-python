# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ....._models import BaseModel

__all__ = [
    "ServiceUpdateResponse",
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


class HostInfraIPv4HostNetwork(BaseModel):
    tunnel_id: str


class HostInfraIPv4Host(BaseModel):
    ipv4: str

    network: HostInfraIPv4HostNetwork


class HostInfraIPv6HostNetwork(BaseModel):
    tunnel_id: str


class HostInfraIPv6Host(BaseModel):
    ipv6: str

    network: HostInfraIPv6HostNetwork


class HostInfraDualStackHostNetwork(BaseModel):
    tunnel_id: str


class HostInfraDualStackHost(BaseModel):
    ipv4: str

    ipv6: str

    network: HostInfraDualStackHostNetwork


class HostInfraHostnameHostResolverNetwork(BaseModel):
    tunnel_id: str

    resolver_ips: Optional[List[str]] = None


class HostInfraHostnameHost(BaseModel):
    hostname: str

    resolver_network: HostInfraHostnameHostResolverNetwork


Host: TypeAlias = Union[HostInfraIPv4Host, HostInfraIPv6Host, HostInfraDualStackHost, HostInfraHostnameHost]


class ServiceUpdateResponse(BaseModel):
    host: Host

    name: str

    type: Literal["http"]

    created_at: Optional[datetime] = None

    http_port: Optional[int] = None

    https_port: Optional[int] = None

    service_id: Optional[str] = None

    updated_at: Optional[datetime] = None
