# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .host import Host
from .status import Status
from ..._models import BaseModel

__all__ = [
    "CertificatePackListResponse",
    "Certificate",
    "CertificateGeoRestrictions",
    "ValidationError",
    "ValidationRecord",
]


class CertificateGeoRestrictions(BaseModel):
    label: Optional[Literal["us", "eu", "highest_security"]] = None


class Certificate(BaseModel):
    id: str
    """Certificate identifier."""

    hosts: List[str]
    """Hostnames covered by this certificate."""

    status: str
    """Certificate status."""

    bundle_method: Optional[str] = None
    """Certificate bundle method."""

    expires_on: Optional[datetime] = None
    """When the certificate from the authority expires."""

    geo_restrictions: Optional[CertificateGeoRestrictions] = None
    """Specify the region where your private key can be held locally."""

    issuer: Optional[str] = None
    """The certificate authority that issued the certificate."""

    modified_on: Optional[datetime] = None
    """When the certificate was last modified."""

    priority: Optional[float] = None
    """The order/priority in which the certificate will be used."""

    signature: Optional[str] = None
    """The type of hash used for the certificate."""

    uploaded_on: Optional[datetime] = None
    """When the certificate was uploaded to Cloudflare."""

    zone_id: Optional[str] = None
    """Identifier."""


class ValidationError(BaseModel):
    message: Optional[str] = None
    """A domain validation error."""


class ValidationRecord(BaseModel):
    emails: Optional[List[str]] = None
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


class CertificatePackListResponse(BaseModel):
    id: str
    """Identifier."""

    certificates: List[Certificate]
    """Array of certificates in this pack."""

    hosts: List[Host]
    """Comma separated list of valid host names for the certificate packs.

    Must contain the zone apex, may not contain more than 50 hosts, and may not be
    empty.
    """

    status: Status
    """Status of certificate pack."""

    type: Literal[
        "mh_custom", "managed_hostname", "sni_custom", "universal", "advanced", "total_tls", "keyless", "legacy_custom"
    ]
    """Type of certificate pack."""

    certificate_authority: Optional[Literal["google", "lets_encrypt", "ssl_com"]] = None
    """Certificate Authority selected for the order.

    For information on any certificate authority specific details or restrictions
    [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)
    """

    cloudflare_branding: Optional[bool] = None
    """Whether or not to add Cloudflare Branding for the order.

    This will add a subdomain of sni.cloudflaressl.com as the Common Name if set to
    true.
    """

    primary_certificate: Optional[str] = None
    """Identifier of the primary certificate in a pack."""

    validation_errors: Optional[List[ValidationError]] = None
    """
    Domain validation errors that have been received by the certificate authority
    (CA).
    """

    validation_method: Optional[Literal["txt", "http", "email"]] = None
    """Validation Method selected for the order."""

    validation_records: Optional[List[ValidationRecord]] = None
    """Certificates' validation records."""

    validity_days: Optional[Literal[14, 30, 90, 365]] = None
    """Validity Days selected for the order."""
