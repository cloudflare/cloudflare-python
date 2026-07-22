# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "RegistrationCreateParams",
    "Contacts",
    "ContactsAdministrator",
    "ContactsAdministratorPostalInfo",
    "ContactsAdministratorPostalInfoAddress",
    "ContactsBilling",
    "ContactsBillingPostalInfo",
    "ContactsBillingPostalInfoAddress",
    "ContactsRegistrant",
    "ContactsRegistrantPostalInfo",
    "ContactsRegistrantPostalInfoAddress",
    "ContactsTechnical",
    "ContactsTechnicalPostalInfo",
    "ContactsTechnicalPostalInfoAddress",
]


class RegistrationCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    domain_name: Required[str]
    """
    Fully qualified domain name (FQDN) including the extension (e.g., `example.com`,
    `mybrand.app`). The domain name uniquely identifies a registration — the same
    domain cannot be registered twice, making it a natural idempotency key for
    registration requests.
    """

    acknowledgements: Dict[str, object]
    """
    User acknowledgements required by a specific extension or premium registration
    flow. The expected keys are described by the extension registration schema
    returned by the extension discovery endpoint.
    """

    auto_renew: bool
    """Enable or disable automatic renewal.

    Defaults to `false` if omitted. Setting this field to `true` is an explicit
    opt-in authorizing Cloudflare to charge the account's default payment method up
    to 30 days before domain expiry to renew the domain automatically. Renewal
    pricing may change over time based on registry pricing.
    """

    contact_extensions: Dict[str, object]
    """Registry-specific contact extension values for the registrant.

    The required keys and allowed values vary by extension and are described by
    `GET /accounts/{account_id}/registrar/extensions/{extension}` in the
    `registration_schema.properties.contact_extensions` object.

    Examples include `.us` nexus fields, `.uk` registrant type fields, and `.ca`
    legal type fields. Omit this object for extensions whose registration schema
    does not include `contact_extensions`.
    """

    contacts: Contacts
    """Contact data for the registration request.

    The per-extension schema returned by
    `GET /accounts/{account_id}/registrar/extensions/{extension}` is the
    authoritative contract for which contact roles are accepted. Every currently
    supported extension requires only `contacts.registrant` from API callers.
    Additional roles such as `technical`, `administrator`, and `billing` may be
    provided when the extension schema includes them. If a registry requires one of
    those roles and the caller omits it, Cloudflare may derive that contact from
    `contacts.registrant`.

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


class ContactsAdministratorPostalInfoAddress(TypedDict, total=False):
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


class ContactsAdministratorPostalInfo(TypedDict, total=False):
    """Postal/mailing information for the contact.

    The `name` field is the
    complete contact name in one string. Some registries require a complete
    personal name, including a family or last name where applicable, but this
    API does not accept separate first-name and last-name fields for
    registration contacts.
    """

    address: Required[ContactsAdministratorPostalInfoAddress]
    """Physical mailing address for the registrant contact."""

    name: Required[str]
    """
    Full legal name of the contact, including all required name components for an
    individual or authorized representative. Some registries require a complete
    personal name that includes a family or last name where applicable. Provide the
    complete name in this single field, for example `Ada Lovelace`; do not send
    separate first-name or last-name fields.
    """

    organization: str
    """Organization or company name. Optional for individual registrants."""


class ContactsAdministrator(TypedDict, total=False):
    """Contact data for the domain registration.

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

    postal_info: Required[ContactsAdministratorPostalInfo]
    """Postal/mailing information for the contact.

    The `name` field is the complete contact name in one string. Some registries
    require a complete personal name, including a family or last name where
    applicable, but this API does not accept separate first-name and last-name
    fields for registration contacts.
    """

    fax: str
    """Fax number in E.164 format (e.g., `+1.5555555555`).

    Optional. Most registrations do not require a fax number.
    """


class ContactsBillingPostalInfoAddress(TypedDict, total=False):
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


class ContactsBillingPostalInfo(TypedDict, total=False):
    """Postal/mailing information for the contact.

    The `name` field is the
    complete contact name in one string. Some registries require a complete
    personal name, including a family or last name where applicable, but this
    API does not accept separate first-name and last-name fields for
    registration contacts.
    """

    address: Required[ContactsBillingPostalInfoAddress]
    """Physical mailing address for the registrant contact."""

    name: Required[str]
    """
    Full legal name of the contact, including all required name components for an
    individual or authorized representative. Some registries require a complete
    personal name that includes a family or last name where applicable. Provide the
    complete name in this single field, for example `Ada Lovelace`; do not send
    separate first-name or last-name fields.
    """

    organization: str
    """Organization or company name. Optional for individual registrants."""


class ContactsBilling(TypedDict, total=False):
    """Contact data for the domain registration.

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

    postal_info: Required[ContactsBillingPostalInfo]
    """Postal/mailing information for the contact.

    The `name` field is the complete contact name in one string. Some registries
    require a complete personal name, including a family or last name where
    applicable, but this API does not accept separate first-name and last-name
    fields for registration contacts.
    """

    fax: str
    """Fax number in E.164 format (e.g., `+1.5555555555`).

    Optional. Most registrations do not require a fax number.
    """


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
    """Postal/mailing information for the contact.

    The `name` field is the
    complete contact name in one string. Some registries require a complete
    personal name, including a family or last name where applicable, but this
    API does not accept separate first-name and last-name fields for
    registration contacts.
    """

    address: Required[ContactsRegistrantPostalInfoAddress]
    """Physical mailing address for the registrant contact."""

    name: Required[str]
    """
    Full legal name of the contact, including all required name components for an
    individual or authorized representative. Some registries require a complete
    personal name that includes a family or last name where applicable. Provide the
    complete name in this single field, for example `Ada Lovelace`; do not send
    separate first-name or last-name fields.
    """

    organization: str
    """Organization or company name. Optional for individual registrants."""


class ContactsRegistrant(TypedDict, total=False):
    """Contact data for the domain registration.

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
    """Postal/mailing information for the contact.

    The `name` field is the complete contact name in one string. Some registries
    require a complete personal name, including a family or last name where
    applicable, but this API does not accept separate first-name and last-name
    fields for registration contacts.
    """

    fax: str
    """Fax number in E.164 format (e.g., `+1.5555555555`).

    Optional. Most registrations do not require a fax number.
    """


class ContactsTechnicalPostalInfoAddress(TypedDict, total=False):
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


class ContactsTechnicalPostalInfo(TypedDict, total=False):
    """Postal/mailing information for the contact.

    The `name` field is the
    complete contact name in one string. Some registries require a complete
    personal name, including a family or last name where applicable, but this
    API does not accept separate first-name and last-name fields for
    registration contacts.
    """

    address: Required[ContactsTechnicalPostalInfoAddress]
    """Physical mailing address for the registrant contact."""

    name: Required[str]
    """
    Full legal name of the contact, including all required name components for an
    individual or authorized representative. Some registries require a complete
    personal name that includes a family or last name where applicable. Provide the
    complete name in this single field, for example `Ada Lovelace`; do not send
    separate first-name or last-name fields.
    """

    organization: str
    """Organization or company name. Optional for individual registrants."""


class ContactsTechnical(TypedDict, total=False):
    """Contact data for the domain registration.

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

    postal_info: Required[ContactsTechnicalPostalInfo]
    """Postal/mailing information for the contact.

    The `name` field is the complete contact name in one string. Some registries
    require a complete personal name, including a family or last name where
    applicable, but this API does not accept separate first-name and last-name
    fields for registration contacts.
    """

    fax: str
    """Fax number in E.164 format (e.g., `+1.5555555555`).

    Optional. Most registrations do not require a fax number.
    """


class Contacts(TypedDict, total=False):
    """Contact data for the registration request.

    The per-extension schema returned by
    `GET /accounts/{account_id}/registrar/extensions/{extension}` is the
    authoritative contract for which contact roles are accepted. Every
    currently supported extension requires only `contacts.registrant` from
    API callers. Additional roles such as `technical`, `administrator`, and
    `billing` may be provided when the extension schema includes them. If a
    registry requires one of those roles and the caller omits it, Cloudflare
    may derive that contact from `contacts.registrant`.

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

    administrator: ContactsAdministrator
    """Contact data for the domain registration.

    This information is submitted to the domain registry and, depending on extension
    and privacy settings, may appear in public WHOIS records.
    """

    billing: ContactsBilling
    """Contact data for the domain registration.

    This information is submitted to the domain registry and, depending on extension
    and privacy settings, may appear in public WHOIS records.
    """

    registrant: ContactsRegistrant
    """Contact data for the domain registration.

    This information is submitted to the domain registry and, depending on extension
    and privacy settings, may appear in public WHOIS records.
    """

    technical: ContactsTechnical
    """Contact data for the domain registration.

    This information is submitted to the domain registry and, depending on extension
    and privacy settings, may appear in public WHOIS records.
    """
