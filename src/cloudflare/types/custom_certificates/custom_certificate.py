# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel
from .geo_restrictions import GeoRestrictions
from ..custom_hostnames.bundle_method import BundleMethod
from ..keyless_certificates.keyless_certificate import KeylessCertificate

__all__ = ["CustomCertificate"]


class CustomCertificate(BaseModel):
    id: str
    """Identifier."""

    zone_id: str
    """Identifier."""

    bundle_method: Optional[BundleMethod] = None
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    expires_on: Optional[datetime] = None
    """When the certificate from the authority expires."""

    geo_restrictions: Optional[GeoRestrictions] = None
    """
    Specify the region where your private key can be held locally for optimal TLS
    performance. HTTPS connections to any excluded data center will still be fully
    encrypted, but will incur some latency while Keyless SSL is used to complete the
    handshake with the nearest allowed data center. Options allow distribution to
    only to U.S. data centers, only to E.U. data centers, or only to highest
    security data centers. Default distribution is to all Cloudflare datacenters,
    for optimal performance.
    """

    hosts: Optional[List[str]] = None

    issuer: Optional[str] = None
    """The certificate authority that issued the certificate."""

    keyless_server: Optional[KeylessCertificate] = None

    modified_on: Optional[datetime] = None
    """When the certificate was last modified."""

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

    priority: Optional[float] = None
    """The order/priority in which the certificate will be used in a request.

    The higher priority will break ties across overlapping 'legacy_custom'
    certificates, but 'legacy_custom' certificates will always supercede
    'sni_custom' certificates.
    """

    signature: Optional[str] = None
    """The type of hash used for the certificate."""

    status: Optional[Literal["active", "expired", "deleted", "pending", "initializing"]] = None
    """Status of the zone's custom SSL."""

    uploaded_on: Optional[datetime] = None
    """When the certificate was uploaded to Cloudflare."""
