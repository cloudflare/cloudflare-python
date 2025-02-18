# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, Required, TypedDict

from .dcv_method import DCVMethod
from .bundle_method import BundleMethod
from ..shared.certificate_ca import CertificateCA
from .domain_validation_type import DomainValidationType

__all__ = ["CustomHostnameEditParams", "SSL", "SSLCustomCERTBundle", "SSLSettings"]


class CustomHostnameEditParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    custom_metadata: Dict[str, str]
    """Unique key/value metadata for this hostname.

    These are per-hostname (customer) settings.
    """

    custom_origin_server: str
    """
    a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME
    record.
    """

    custom_origin_sni: str
    """
    A hostname that will be sent to your custom origin server as SNI for TLS
    handshake. This can be a valid subdomain of the zone or custom origin server
    name or the string ':request_host_header:' which will cause the host header in
    the request to be used as SNI. Not configurable with default/fallback origin
    server.
    """

    ssl: SSL
    """SSL properties used when creating the custom hostname."""


class SSLCustomCERTBundle(TypedDict, total=False):
    custom_certificate: Required[str]
    """If a custom uploaded certificate is used."""

    custom_key: Required[str]
    """The key for a custom uploaded certificate."""


class SSLSettings(TypedDict, total=False):
    ciphers: List[str]
    """An allowlist of ciphers for TLS termination.

    These ciphers must be in the BoringSSL format.
    """

    early_hints: Literal["on", "off"]
    """Whether or not Early Hints is enabled."""

    http2: Literal["on", "off"]
    """Whether or not HTTP2 is enabled."""

    min_tls_version: Literal["1.0", "1.1", "1.2", "1.3"]
    """The minimum TLS version supported."""

    tls_1_3: Literal["on", "off"]
    """Whether or not TLS 1.3 is enabled."""


class SSL(TypedDict, total=False):
    bundle_method: BundleMethod
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    certificate_authority: CertificateCA
    """The Certificate Authority that will issue the certificate"""

    cloudflare_branding: bool
    """Whether or not to add Cloudflare Branding for the order.

    This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to
    true
    """

    custom_cert_bundle: Iterable[SSLCustomCERTBundle]
    """Array of custom certificate and key pairs (1 or 2 pairs allowed)"""

    custom_certificate: str
    """If a custom uploaded certificate is used."""

    custom_key: str
    """The key for a custom uploaded certificate."""

    method: DCVMethod
    """Domain control validation (DCV) method used for this hostname."""

    settings: SSLSettings
    """SSL specific settings."""

    type: DomainValidationType
    """Level of validation to be used for this hostname.

    Domain validation (dv) must be used.
    """

    wildcard: bool
    """Indicates whether the certificate covers a wildcard."""
