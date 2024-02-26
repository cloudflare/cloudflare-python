# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

__all__ = ["CustomHostnameCreateParams", "SSL", "SSLSettings", "CustomMetadata"]


class CustomHostnameCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hostname: Required[str]
    """The custom hostname that will point to your hostname via CNAME."""

    ssl: Required[SSL]
    """SSL properties used when creating the custom hostname."""

    custom_metadata: CustomMetadata
    """These are per-hostname (customer) settings."""


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
    bundle_method: Literal["ubiquitous", "optimal", "force"]
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    certificate_authority: Literal["digicert", "google", "lets_encrypt"]
    """The Certificate Authority that will issue the certificate"""

    custom_certificate: str
    """If a custom uploaded certificate is used."""

    custom_key: str
    """The key for a custom uploaded certificate."""

    method: Literal["http", "txt", "email"]
    """Domain control validation (DCV) method used for this hostname."""

    settings: SSLSettings
    """SSL specific settings."""

    type: Literal["dv"]
    """Level of validation to be used for this hostname.

    Domain validation (dv) must be used.
    """

    wildcard: bool
    """Indicates whether the certificate covers a wildcard."""


class CustomMetadata(TypedDict, total=False):
    key: str
    """Unique metadata for this hostname."""
