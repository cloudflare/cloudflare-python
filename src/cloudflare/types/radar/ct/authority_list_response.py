# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AuthorityListResponse", "CertificateAuthority"]


class CertificateAuthority(BaseModel):
    certificate_record_type: Literal["ROOT_CERTIFICATE", "INTERMEDIATE_CERTIFICATE"] = FieldInfo(
        alias="certificateRecordType"
    )
    """Specifies the type of certificate in the trust chain."""

    country: str
    """The two-letter ISO country code where the CA organization is based."""

    country_name: str = FieldInfo(alias="countryName")
    """The full country name corresponding to the country code."""

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

    revocation_status: Literal["NOT_REVOKED", "REVOKED", "PARENT_CERT_REVOKED"] = FieldInfo(alias="revocationStatus")
    """The current revocation status of a Certificate Authority (CA) certificate."""

    sha256_fingerprint: str = FieldInfo(alias="sha256Fingerprint")
    """The SHA-256 fingerprint of the intermediate certificate."""


class AuthorityListResponse(BaseModel):
    certificate_authorities: List[CertificateAuthority] = FieldInfo(alias="certificateAuthorities")
