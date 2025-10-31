# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SSOListResponse", "Verification"]


class Verification(BaseModel):
    code: Optional[str] = None
    """DNS verification code.

    Add this entire string to the DNS TXT record of the email domain to validate
    ownership.
    """

    status: Optional[Literal["awaiting", "pending", "failed", "verified"]] = None
    """The status of the verification code from the verification process."""


class SSOListResponse(BaseModel):
    id: Optional[str] = None
    """SSO Connector identifier tag."""

    created_on: Optional[datetime] = None
    """Timestamp for the creation of the SSO connector"""

    email_domain: Optional[str] = None

    enabled: Optional[bool] = None

    updated_on: Optional[datetime] = None
    """Timestamp for the last update of the SSO connector"""

    verification: Optional[Verification] = None
