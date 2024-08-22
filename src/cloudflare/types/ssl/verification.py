# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .validation_method import ValidationMethod

__all__ = ["Verification", "VerificationInfo"]


class VerificationInfo(BaseModel):
    record_name: Optional[Literal["record_name", "http_url", "cname", "txt_name"]] = None
    """Name of CNAME record."""

    record_target: Optional[Literal["record_value", "http_body", "cname_target", "txt_value"]] = None
    """Target of CNAME record."""


class Verification(BaseModel):
    certificate_status: Literal[
        "initializing", "authorizing", "active", "expired", "issuing", "timing_out", "pending_deployment"
    ]
    """Current status of certificate."""

    brand_check: Optional[bool] = None
    """Certificate Authority is manually reviewing the order."""

    cert_pack_uuid: Optional[str] = None
    """Certificate Pack UUID."""

    signature: Optional[Literal["ECDSAWithSHA256", "SHA1WithRSA", "SHA256WithRSA"]] = None
    """Certificate's signature algorithm."""

    validation_method: Optional[ValidationMethod] = None
    """Validation method in use for a certificate pack order."""

    verification_info: Optional[VerificationInfo] = None
    """Certificate's required verification information."""

    verification_status: Optional[bool] = None
    """
    Status of the required verification information, omitted if verification status
    is unknown.
    """

    verification_type: Optional[Literal["cname", "meta tag"]] = None
    """Method of verification."""
