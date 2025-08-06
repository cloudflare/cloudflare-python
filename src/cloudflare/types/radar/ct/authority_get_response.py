# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuthorityGetResponse", "CertificateAuthority", "CertificateAuthorityRelated"]


class CertificateAuthorityRelated(BaseModel):
    certificate_record_type: Literal["ROOT_CERTIFICATE", "INTERMEDIATE_CERTIFICATE"] = FieldInfo(
        alias="certificateRecordType"
    )
    """Specifies the type of certificate in the trust chain."""

    name: str
    """The full name of the certificate authority (CA)."""

    revocation_status: Literal["NOT_REVOKED", "REVOKED", "PARENT_CERT_REVOKED"] = FieldInfo(alias="revocationStatus")
    """The current revocation status of a Certificate Authority (CA) certificate."""

    sha256_fingerprint: str = FieldInfo(alias="sha256Fingerprint")
    """The SHA-256 fingerprint of the intermediate certificate."""


class CertificateAuthority(BaseModel):
    apple_status: Literal[
        "INCLUDED", "NOT_YET_INCLUDED", "NOT_INCLUDED", "NOT_BEFORE", "REMOVED", "DISABLED", "BLOCKED"
    ] = FieldInfo(alias="appleStatus")
    """The inclusion status of a Certificate Authority (CA) in the trust store."""

    authority_key_identifier: str = FieldInfo(alias="authorityKeyIdentifier")
    """The authorityKeyIdentifier value extracted from the certificate PEM."""

    certificate_record_type: Literal["ROOT_CERTIFICATE", "INTERMEDIATE_CERTIFICATE"] = FieldInfo(
        alias="certificateRecordType"
    )
    """Specifies the type of certificate in the trust chain."""

    chrome_status: Literal[
        "INCLUDED", "NOT_YET_INCLUDED", "NOT_INCLUDED", "NOT_BEFORE", "REMOVED", "DISABLED", "BLOCKED"
    ] = FieldInfo(alias="chromeStatus")
    """The inclusion status of a Certificate Authority (CA) in the trust store."""

    country: str
    """The two-letter ISO country code where the CA organization is based."""

    country_name: str = FieldInfo(alias="countryName")
    """The full country name corresponding to the country code."""

    microsoft_status: Literal[
        "INCLUDED", "NOT_YET_INCLUDED", "NOT_INCLUDED", "NOT_BEFORE", "REMOVED", "DISABLED", "BLOCKED"
    ] = FieldInfo(alias="microsoftStatus")
    """The inclusion status of a Certificate Authority (CA) in the trust store."""

    mozilla_status: Literal[
        "INCLUDED", "NOT_YET_INCLUDED", "NOT_INCLUDED", "NOT_BEFORE", "REMOVED", "DISABLED", "BLOCKED"
    ] = FieldInfo(alias="mozillaStatus")
    """The inclusion status of a Certificate Authority (CA) in the trust store."""

    name: str
    """The full name of the certificate authority (CA)."""

    owner: str
    """The organization that owns and operates the CA."""

    parent_name: str = FieldInfo(alias="parentName")
    """
    The name of the parent/root certificate authority that issued this intermediate
    certificate.
    """

    parent_sha256_fingerprint: str = FieldInfo(alias="parentSha256Fingerprint")
    """The SHA-256 fingerprint of the parent certificate."""

    related: List[CertificateAuthorityRelated]
    """CAs from the same owner."""

    revocation_status: Literal["NOT_REVOKED", "REVOKED", "PARENT_CERT_REVOKED"] = FieldInfo(alias="revocationStatus")
    """The current revocation status of a Certificate Authority (CA) certificate."""

    sha256_fingerprint: str = FieldInfo(alias="sha256Fingerprint")
    """The SHA-256 fingerprint of the intermediate certificate."""

    subject_key_identifier: str = FieldInfo(alias="subjectKeyIdentifier")
    """The subjectKeyIdentifier value extracted from the certificate PEM."""

    valid_from: str = FieldInfo(alias="validFrom")
    """The start date of the certificate’s validity period (ISO format)."""

    valid_to: str = FieldInfo(alias="validTo")
    """The end date of the certificate’s validity period (ISO format)."""


class AuthorityGetResponse(BaseModel):
    certificate_authority: CertificateAuthority = FieldInfo(alias="certificateAuthority")
