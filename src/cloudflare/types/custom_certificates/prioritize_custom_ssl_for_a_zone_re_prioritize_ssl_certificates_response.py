# File generated from our OpenAPI spec by Stainless.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse",
    "PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItem",
    "PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemGeoRestrictions",
    "PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServer",
    "PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServerTunnel",
]


class PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemGeoRestrictions(BaseModel):
    label: Optional[Literal["us", "eu", "highest_security"]] = None


class PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServerTunnel(BaseModel):
    private_ip: str
    """Private IP of the Key Server Host"""

    vnet_id: str
    """Cloudflare Tunnel Virtual Network ID"""


class PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServer(BaseModel):
    id: str
    """Keyless certificate identifier tag."""

    created_on: datetime
    """When the Keyless SSL was created."""

    enabled: bool
    """Whether or not the Keyless SSL is on or off."""

    host: str
    """The keyless SSL name."""

    modified_on: datetime
    """When the Keyless SSL was last modified."""

    name: str
    """The keyless SSL name."""

    permissions: List[object]
    """
    Available permissions for the Keyless SSL for the current user requesting the
    item.
    """

    port: float
    """
    The keyless SSL port used to communicate between Cloudflare and the client's
    Keyless SSL server.
    """

    status: Literal["active", "deleted"]
    """Status of the Keyless SSL."""

    tunnel: Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServerTunnel] = None
    """Configuration for using Keyless SSL through a Cloudflare Tunnel"""


class PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItem(BaseModel):
    id: str
    """Identifier"""

    bundle_method: Literal["ubiquitous", "optimal", "force"]
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    expires_on: datetime
    """When the certificate from the authority expires."""

    hosts: List[str]

    issuer: str
    """The certificate authority that issued the certificate."""

    modified_on: datetime
    """When the certificate was last modified."""

    priority: float
    """The order/priority in which the certificate will be used in a request.

    The higher priority will break ties across overlapping 'legacy_custom'
    certificates, but 'legacy_custom' certificates will always supercede
    'sni_custom' certificates.
    """

    signature: str
    """The type of hash used for the certificate."""

    status: Literal["active", "expired", "deleted", "pending", "initializing"]
    """Status of the zone's custom SSL."""

    uploaded_on: datetime
    """When the certificate was uploaded to Cloudflare."""

    zone_id: str
    """Identifier"""

    geo_restrictions: Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemGeoRestrictions] = None
    """
    Specify the region where your private key can be held locally for optimal TLS
    performance. HTTPS connections to any excluded data center will still be fully
    encrypted, but will incur some latency while Keyless SSL is used to complete the
    handshake with the nearest allowed data center. Options allow distribution to
    only to U.S. data centers, only to E.U. data centers, or only to highest
    security data centers. Default distribution is to all Cloudflare datacenters,
    for optimal performance.
    """

    keyless_server: Optional[PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItemKeylessServer] = None

    policy: Optional[str] = None
    """
    Specify the policy that determines the region where your private key will be
    held locally. HTTPS connections to any excluded data center will still be fully
    encrypted, but will incur some latency while Keyless SSL is used to complete the
    handshake with the nearest allowed data center. Any combination of countries,
    specified by their two letter country code
    (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
    can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
    the EU region. If there are too few data centers satisfying the policy, it will
    be rejected.
    """


PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponse = List[
    PrioritizeCustomSSLForAZoneRePrioritizeSSLCertificatesResponseItem
]
