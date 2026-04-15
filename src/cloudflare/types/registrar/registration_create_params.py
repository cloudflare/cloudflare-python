# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RegistrationCreateParams",
    "Contacts",
    "ContactsRegistrant",
    "ContactsRegistrantPostalInfo",
    "ContactsRegistrantPostalInfoAddress",
]


class RegistrationCreateParams(TypedDict, total=False):
    account_id: str
    """Identifier"""

    domain_name: Required[str]
    """
    Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
    `mybrand.app`). The domain name uniquely identifies a registration — the same
    domain cannot be registered twice, making it a natural idempotency key for
    registration requests.
    """

    auto_renew: bool
    """Enable or disable automatic renewal.

    Defaults to `false` if omitted. Setting this field to `true` is an explicit
    opt-in authorizing Cloudflare to charge the account's default payment method up
    to 30 days before domain expiry to renew the domain automatically. Renewal
    pricing may change over time based on registry pricing.
    """

    contacts: Contacts
    """Contact data for the registration request.

    If the `contacts` object is omitted entirely from the request, or if
    `contacts.registrant` is not provided, the system will use the account's default
    address book entry as the registrant contact. This default must be
    pre-configured by the account owner at
    `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
    create or update the address book entry and accept the required agreement. No
    API exists for managing address book entries at this time.

    If no default address book entry exists and no registrant contact is provided,
    the registration request will fail with a validation error.
    """

    privacy_mode: Literal["redaction"]
    """WHOIS privacy mode for the registration. Defaults to `redaction`.

    - `off`: Do not request WHOIS privacy.
    - `redaction`: Request WHOIS redaction where supported by the extension. Some
      extensions do not support privacy/redaction.
    """

    years: int
    """Number of years to register (1–10).

    If omitted, defaults to the minimum registration period required by the registry
    for this extension. For most extensions this is 1 year, but some extensions
    require longer minimum terms (e.g., `.ai` requires a minimum of 2 years).

    The registry for each extension may also enforce its own maximum registration
    term. If the requested value exceeds the registry's maximum, the registration
    will be rejected. When in doubt, use the default by omitting this field.
    """

    prefer: Annotated[str, PropertyInfo(alias="Prefer")]


class ContactsRegistrantPostalInfoAddress(TypedDict, total=False):
    """Physical mailing address for the registrant contact."""

    city: Required[str]
    """City or locality name."""

    country_code: Required[str]
    """Two-letter country code per ISO 3166-1 alpha-2 (e.g., `US`, `GB`, `CA`, `DE`)."""

    postal_code: Required[str]
    """Postal or ZIP code."""

    state: Required[str]
    """State, province, or region.

    Use the standard abbreviation where applicable (e.g., `TX` for Texas, `ON` for
    Ontario).
    """

    street: Required[str]
    """Street address including building/suite number."""


class ContactsRegistrantPostalInfo(TypedDict, total=False):
    """Postal/mailing information for the registrant contact."""

    address: Required[ContactsRegistrantPostalInfoAddress]
    """Physical mailing address for the registrant contact."""

    name: Required[str]
    """Full legal name of the registrant (individual or authorized representative)."""

    organization: str
    """Organization or company name. Optional for individual registrants."""


class ContactsRegistrant(TypedDict, total=False):
    """Registrant contact data for the domain registration.

    This information
    is submitted to the domain registry and, depending on extension and
    privacy settings, may appear in public WHOIS records.
    """

    email: Required[str]
    """Email address for the registrant.

    Used for domain-related communications from the registry, including ownership
    verification and renewal notices.
    """

    phone: Required[str]
    """
    Phone number in E.164 format: `+{country_code}.{number}` with no spaces or
    dashes. Examples: `+1.5555555555` (US), `+44.2071234567` (UK), `+81.312345678`
    (Japan).
    """

    postal_info: Required[ContactsRegistrantPostalInfo]
    """Postal/mailing information for the registrant contact."""

    fax: str
    """Fax number in E.164 format (e.g., `+1.5555555555`).

    Optional. Most registrations do not require a fax number.
    """


class Contacts(TypedDict, total=False):
    """Contact data for the registration request.

    If the `contacts` object is omitted entirely from the request, or if
    `contacts.registrant` is not provided, the system will use the account's
    default address book entry as the registrant contact. This default must be
    pre-configured by the account owner at
    `https://dash.cloudflare.com/{account_id}/domains/registrations`, where
    they can create or update the address book entry and accept the required
    agreement. No API exists for managing address book entries at this time.

    If no default address book entry exists and no registrant contact is
    provided, the registration request will fail with a validation error.
    """

    registrant: ContactsRegistrant
    """Registrant contact data for the domain registration.

    This information is submitted to the domain registry and, depending on extension
    and privacy settings, may appear in public WHOIS records.
    """
