# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["CustomHostnameCreateResponse", "SSL", "SSLSettings", "SSLValidationError", "SSLValidationRecord"]


class SSLSettings(BaseModel):
    ciphers: Optional[List[str]] = None
    """An allowlist of ciphers for TLS termination.

    These ciphers must be in the BoringSSL format.
    """

    early_hints: Optional[Literal["on", "off"]] = None
    """Whether or not Early Hints is enabled."""

    http2: Optional[Literal["on", "off"]] = None
    """Whether or not HTTP2 is enabled."""

    min_tls_version: Optional[Literal["1.0", "1.1", "1.2", "1.3"]] = None
    """The minimum TLS version supported."""

    tls_1_3: Optional[Literal["on", "off"]] = None
    """Whether or not TLS 1.3 is enabled."""


class SSLValidationError(BaseModel):
    message: Optional[str] = None
    """A domain validation error."""


class SSLValidationRecord(BaseModel):
    emails: Optional[List[object]] = None
    """
    The set of email addresses that the certificate authority (CA) will use to
    complete domain validation.
    """

    http_body: Optional[str] = None
    """
    The content that the certificate authority (CA) will expect to find at the
    http_url during the domain validation.
    """

    http_url: Optional[str] = None
    """The url that will be checked during domain validation."""

    txt_name: Optional[str] = None
    """
    The hostname that the certificate authority (CA) will check for a TXT record
    during domain validation .
    """

    txt_value: Optional[str] = None
    """
    The TXT record that the certificate authority (CA) will check during domain
    validation.
    """


class SSL(BaseModel):
    id: Optional[str] = None
    """Custom hostname SSL identifier tag."""

    bundle_method: Optional[Literal["ubiquitous", "optimal", "force"]] = None
    """
    A ubiquitous bundle has the highest probability of being verified everywhere,
    even by clients using outdated or unusual trust stores. An optimal bundle uses
    the shortest chain and newest intermediates. And the force bundle verifies the
    chain, but does not otherwise modify it.
    """

    certificate_authority: Optional[Literal["digicert", "google", "lets_encrypt"]] = None
    """The Certificate Authority that will issue the certificate"""

    custom_certificate: Optional[str] = None
    """If a custom uploaded certificate is used."""

    custom_csr_id: Optional[str] = None
    """The identifier for the Custom CSR that was used."""

    custom_key: Optional[str] = None
    """The key for a custom uploaded certificate."""

    expires_on: Optional[datetime] = None
    """The time the custom certificate expires on."""

    hosts: Optional[List[object]] = None
    """A list of Hostnames on a custom uploaded certificate."""

    issuer: Optional[str] = None
    """The issuer on a custom uploaded certificate."""

    method: Optional[Literal["http", "txt", "email"]] = None
    """Domain control validation (DCV) method used for this hostname."""

    serial_number: Optional[str] = None
    """The serial number on a custom uploaded certificate."""

    settings: Optional[SSLSettings] = None
    """SSL specific settings."""

    signature: Optional[str] = None
    """The signature on a custom uploaded certificate."""

    status: Optional[
        Literal[
            "initializing",
            "pending_validation",
            "deleted",
            "pending_issuance",
            "pending_deployment",
            "pending_deletion",
            "pending_expiration",
            "expired",
            "active",
            "initializing_timed_out",
            "validation_timed_out",
            "issuance_timed_out",
            "deployment_timed_out",
            "deletion_timed_out",
            "pending_cleanup",
            "staging_deployment",
            "staging_active",
            "deactivating",
            "inactive",
            "backup_issued",
            "holding_deployment",
        ]
    ] = None
    """Status of the hostname's SSL certificates."""

    type: Optional[Literal["dv"]] = None
    """Level of validation to be used for this hostname.

    Domain validation (dv) must be used.
    """

    uploaded_on: Optional[datetime] = None
    """The time the custom certificate was uploaded."""

    validation_errors: Optional[List[SSLValidationError]] = None
    """
    Domain validation errors that have been received by the certificate authority
    (CA).
    """

    validation_records: Optional[List[SSLValidationRecord]] = None

    wildcard: Optional[bool] = None
    """Indicates whether the certificate covers a wildcard."""


class CustomHostnameCreateResponse(BaseModel):
    id: str
    """Identifier"""

    hostname: str
    """The custom hostname that will point to your hostname via CNAME."""

    ssl: SSL
    """SSL properties for the custom hostname."""
