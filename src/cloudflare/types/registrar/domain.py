# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Domain", "RegistrantContact", "TransferIn"]


class RegistrantContact(BaseModel):
    address: str
    """Address."""

    city: str
    """City."""

    country: Optional[str] = None
    """The country in which the user lives."""

    first_name: Optional[str] = None
    """User's first name"""

    last_name: Optional[str] = None
    """User's last name"""

    organization: str
    """Name of organization."""

    phone: Optional[str] = None
    """User's telephone number"""

    state: str
    """State."""

    zip: Optional[str] = None
    """The zipcode or postal code where the user lives."""

    id: Optional[str] = None
    """Contact Identifier."""

    address2: Optional[str] = None
    """Optional address line for unit, floor, suite, etc."""

    email: Optional[str] = None
    """The contact email address of the user."""

    fax: Optional[str] = None
    """Contact fax number."""


class TransferIn(BaseModel):
    accept_foa: Optional[Literal["needed", "ok"]] = None
    """Form of authorization has been accepted by the registrant."""

    approve_transfer: Optional[Literal["needed", "ok", "pending", "trying", "rejected", "unknown"]] = None
    """Shows transfer status with the registry."""

    can_cancel_transfer: Optional[bool] = None
    """Indicates if cancellation is still possible."""

    disable_privacy: Optional[Literal["needed", "ok", "unknown"]] = None
    """Privacy guards are disabled at the foreign registrar."""

    enter_auth_code: Optional[Literal["needed", "ok", "pending", "trying", "rejected"]] = None
    """Auth code has been entered and verified."""

    unlock_domain: Optional[Literal["needed", "ok", "pending", "trying", "unknown"]] = None
    """Domain is unlocked at the foreign registrar."""


class Domain(BaseModel):
    id: Optional[str] = None
    """Domain identifier."""

    available: Optional[bool] = None
    """Shows if a domain is available for transferring into Cloudflare Registrar."""

    can_register: Optional[bool] = None
    """Indicates if the domain can be registered as a new domain."""

    created_at: Optional[datetime] = None
    """Shows time of creation."""

    current_registrar: Optional[str] = None
    """Shows name of current registrar."""

    expires_at: Optional[datetime] = None
    """Shows when domain name registration expires."""

    locked: Optional[bool] = None
    """Shows whether a registrar lock is in place for a domain."""

    registrant_contact: Optional[RegistrantContact] = None
    """Shows contact information for domain registrant."""

    registry_statuses: Optional[str] = None
    """A comma-separated list of registry status codes.

    A full list of status codes can be found at
    [EPP Status Codes](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en).
    """

    supported_tld: Optional[bool] = None
    """Whether a particular TLD is currently supported by Cloudflare Registrar.

    Refer to [TLD Policies](https://www.cloudflare.com/tld-policies/) for a list of
    supported TLDs.
    """

    transfer_in: Optional[TransferIn] = None
    """Statuses for domain transfers into Cloudflare Registrar."""

    updated_at: Optional[datetime] = None
    """Last updated."""
