# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from ..custom_certificates.status import Status

__all__ = ["ClientCertificate", "CertificateAuthority"]


class CertificateAuthority(BaseModel):
    id: Optional[str] = None

    name: Optional[str] = None


class ClientCertificate(BaseModel):
    id: Optional[str] = None
    """Identifier"""

    certificate: Optional[str] = None
    """The Client Certificate PEM"""

    certificate_authority: Optional[CertificateAuthority] = None
    """Certificate Authority used to issue the Client Certificate"""

    common_name: Optional[str] = None
    """Common Name of the Client Certificate"""

    country: Optional[str] = None
    """Country, provided by the CSR"""

    csr: Optional[str] = None
    """The Certificate Signing Request (CSR). Must be newline-encoded."""

    expires_on: Optional[str] = None
    """Date that the Client Certificate expires"""

    fingerprint_sha256: Optional[str] = None
    """Unique identifier of the Client Certificate"""

    issued_on: Optional[str] = None
    """Date that the Client Certificate was issued by the Certificate Authority"""

    location: Optional[str] = None
    """Location, provided by the CSR"""

    organization: Optional[str] = None
    """Organization, provided by the CSR"""

    organizational_unit: Optional[str] = None
    """Organizational Unit, provided by the CSR"""

    serial_number: Optional[str] = None
    """The serial number on the created Client Certificate."""

    signature: Optional[str] = None
    """The type of hash used for the Client Certificate.."""

    ski: Optional[str] = None
    """Subject Key Identifier"""

    state: Optional[str] = None
    """State, provided by the CSR"""

    status: Optional[Status] = None
    """
    Client Certificates may be active or revoked, and the pending_reactivation or
    pending_revocation represent in-progress asynchronous transitions
    """

    validity_days: Optional[int] = None
    """
    The number of days the Client Certificate will be valid after the issued_on date
    """
