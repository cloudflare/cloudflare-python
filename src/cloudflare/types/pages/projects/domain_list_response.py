# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DomainListResponse", "ValidationData", "VerificationData"]


class ValidationData(BaseModel):
    error_message: Optional[str] = None

    method: Optional[Literal["http", "txt"]] = None

    status: Optional[Literal["initializing", "pending", "active", "deactivated", "error"]] = None

    txt_name: Optional[str] = None

    txt_value: Optional[str] = None


class VerificationData(BaseModel):
    error_message: Optional[str] = None

    status: Optional[Literal["pending", "active", "deactivated", "blocked", "error"]] = None


class DomainListResponse(BaseModel):
    id: Optional[str] = None

    certificate_authority: Optional[Literal["google", "lets_encrypt"]] = None

    created_on: Optional[str] = None

    domain_id: Optional[str] = None

    name: Optional[str] = None

    status: Optional[Literal["initializing", "pending", "active", "deactivated", "blocked", "error"]] = None

    validation_data: Optional[ValidationData] = None

    verification_data: Optional[VerificationData] = None

    zone_tag: Optional[str] = None
