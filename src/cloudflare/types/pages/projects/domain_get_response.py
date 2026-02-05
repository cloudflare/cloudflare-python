# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainGetResponse", "ValidationData", "VerificationData"]


class ValidationData(BaseModel):
    method: Literal["http", "txt"]

    status: Literal["initializing", "pending", "active", "deactivated", "error"]

    error_message: Optional[str] = None

    txt_name: Optional[str] = None

    txt_value: Optional[str] = None


class VerificationData(BaseModel):
    status: Literal["pending", "active", "deactivated", "blocked", "error"]

    error_message: Optional[str] = None


class DomainGetResponse(BaseModel):
    id: str

    certificate_authority: Literal["google", "lets_encrypt"]

    created_on: str

    domain_id: str

    name: str
    """The domain name."""

    status: Literal["initializing", "pending", "active", "deactivated", "blocked", "error"]

    validation_data: ValidationData

    verification_data: VerificationData

    zone_tag: str
