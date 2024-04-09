# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .custom_metadata_param import CustomMetadataParam
from .unnamed_schema_ref_9a9935a9a770967bb604ae41a81e42e1 import UnnamedSchemaRef9a9935a9a770967bb604ae41a81e42e1
from .unnamed_schema_ref_16aca57bde2963201c7e6e895436c1c1 import UnnamedSchemaRef16aca57bde2963201c7e6e895436c1c1
from .unnamed_schema_ref_78adb375f06c6d462dd92b99e2ecf510 import UnnamedSchemaRef78adb375f06c6d462dd92b99e2ecf510

__all__ = ["CustomHostnameCreateParams", "SSL", "SSLSettings"]


class CustomHostnameCreateParams(TypedDict, total=False):
    zone_id: Required[str]
    """Identifier"""

    hostname: Required[str]
    """The custom hostname that will point to your hostname via CNAME."""

    ssl: Required[SSL]
    """SSL properties used when creating the custom hostname."""

    custom_metadata: CustomMetadataParam
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
    bundle_method: UnnamedSchemaRef16aca57bde2963201c7e6e895436c1c1
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

    method: UnnamedSchemaRef78adb375f06c6d462dd92b99e2ecf510
    """Domain control validation (DCV) method used for this hostname."""

    settings: SSLSettings
    """SSL specific settings."""

    type: UnnamedSchemaRef9a9935a9a770967bb604ae41a81e42e1
    """Level of validation to be used for this hostname.

    Domain validation (dv) must be used.
    """

    wildcard: bool
    """Indicates whether the certificate covers a wildcard."""
