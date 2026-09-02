# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Domain", "RegistrantContact", "TransferIn"]


class RegistrantContact(BaseModel):
    """Shows contact information for domain registrant."""

    address: str
    """Address."""

    city: str
    """City."""

    country: Optional[str] = None
    """The country in which the user lives."""

    first_name: Optional[str] = None
    """User's first name."""

    last_name: Optional[str] = None
    """User's last name."""

    organization: str
    """Name of organization."""

    phone: Optional[str] = None
    """User's telephone number."""

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
    """Statuses for domain transfers into Cloudflare Registrar."""

    accept_foa: Optional[Literal["needed", "ok"]] = None
    """Status of the registrant authorization step."""

    approve_transfer: Optional[Literal["needed", "ok", "pending", "trying", "rejected", "unknown"]] = None
    """Status of the registry transfer-approval step."""

    can_cancel_transfer: Optional[bool] = None
    """Indicates if cancellation is still possible."""

    disable_privacy: Optional[Literal["needed", "ok", "unknown"]] = None
    """Status of the privacy-guard disabling step at the foreign registrar."""

    enter_auth_code: Optional[Literal["needed", "ok", "pending", "trying", "rejected"]] = None
    """Status of the auth-code entry and verification step."""

    unlock_domain: Optional[Literal["needed", "ok", "pending", "trying", "unknown"]] = None
    """Status of the domain-unlock step at the foreign registrar."""


class Domain(BaseModel):
    id: Optional[str] = None
    """Domain identifier."""

    available: Optional[bool] = None
    """Shows if a domain is available for transferring into Cloudflare Registrar."""

    can_register: Optional[bool] = None
    """Indicates eligibility to register the domain as a new domain."""

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

    Refer to
    [EPP Status Codes](https://www.icann.org/resources/pages/epp-status-codes-2014-06-16-en)
    for the full list.
    """

    supported_tld: Optional[bool] = None
    """Indicates whether Cloudflare Registrar currently supports a particular TLD.

    Refer to [TLD Policies](https://www.cloudflare.com/tld-policies/) for a list of
    supported TLDs.
    """

    transfer_in: Optional[TransferIn] = None
    """Statuses for domain transfers into Cloudflare Registrar."""

    updated_at: Optional[datetime] = None
    """Last updated."""
