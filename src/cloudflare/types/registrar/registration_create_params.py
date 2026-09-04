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
    """Identifier."""

    domain_name: Required[str]
    """
    Provides a fully qualified domain name (FQDN), including the extension (e.g.,
    `example.com`, `mybrand.app`). The domain name uniquely identifies a
    registration. Cloudflare permits only one registration per domain, making the
    domain name a natural idempotency key for registration requests.
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
    """
    Provides registry-specific contact extension values for the registrant.
    `GET /accounts/{account_id}/registrar/extensions/{extension}` identifies the
    required keys and allowed values for each extension in the
    `registration_schema.properties.contact_extensions` object.

    Examples include `.us` nexus fields, `.uk` registrant type fields, and `.ca`
    legal type fields. Omit this object when the extension's registration schema
    excludes `contact_extensions`.
    """

    contacts: Contacts
    """Provides contact data for the registration request.

    The per-extension schema from
    `GET /accounts/{account_id}/registrar/extensions/{extension}` defines the
    accepted contact roles. Every currently supported extension requires only
    `contacts.registrant` from API callers. Callers may provide additional roles
    such as `technical`, `administrator`, and `billing` when the extension schema
    includes them. When a registry requires an omitted role, Cloudflare may derive
    that contact from `contacts.registrant`.

    When the request omits either the entire `contacts` object or
    `contacts.registrant`, the system uses the account's default address book entry
    as the registrant contact. The account owner must configure this default at
    `https://dash.cloudflare.com/{account_id}/domains/registrations`, where they can
    create or update the address book entry and accept the required agreement.
    Dashboard settings currently provide the only way to manage address book
    entries.

    Without either a default address book entry or a registrant contact, the
    registration request fails validation.
    """

    privacy_mode: Literal["off", "redaction"]
    """Sets the WHOIS privacy mode for the registration. Defaults to `redaction`.

    - `off`: Disables WHOIS privacy.
    - `redaction`: Requests WHOIS redaction where the extension supports it. Some
      extensions exclude privacy and redaction.
    """

    years: int
    """Sets the registration term from 1 to 10 years.

    When omitted, this field defaults to the registry's minimum registration period
    for the extension. Most extensions require 1 year, while some require longer
    minimum terms (e.g., `.ai` requires 2 years).

    Each registry may also enforce its own maximum registration term. A request
    above that maximum fails. When uncertain, omit this field to use the default.
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
    """Optional administrator contact.

    Accepted only when the extension
    schema includes this role. When the registry requires an omitted
    contact, Cloudflare may derive it from `contacts.registrant`.
    """

    email: Required[str]
    """Email address for the registrant.

    Used for domain-related communications from the registry, including ownership
    verification and renewal notices.
    """

    phone: Required[str]
    """
    Phone number in E.164 format: `+{country_code}.{number}` without spaces or
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
    """Optional billing contact.

    Accepted only when the extension schema
    includes this role. When the registry requires an omitted contact,
    Cloudflare may derive it from `contacts.registrant`.
    """

    email: Required[str]
    """Email address for the registrant.

    Used for domain-related communications from the registry, including ownership
    verification and renewal notices.
    """

    phone: Required[str]
    """
    Phone number in E.164 format: `+{country_code}.{number}` without spaces or
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
    """Optional registrant contact.

    If omitted, the account's default
    address book entry is used instead.
    """

    email: Required[str]
    """Email address for the registrant.

    Used for domain-related communications from the registry, including ownership
    verification and renewal notices.
    """

    phone: Required[str]
    """
    Phone number in E.164 format: `+{country_code}.{number}` without spaces or
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
    """Optional technical contact.

    Accepted only when the extension schema
    includes this role. When the registry requires an omitted contact,
    Cloudflare may derive it from `contacts.registrant`.
    """

    email: Required[str]
    """Email address for the registrant.

    Used for domain-related communications from the registry, including ownership
    verification and renewal notices.
    """

    phone: Required[str]
    """
    Phone number in E.164 format: `+{country_code}.{number}` without spaces or
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
    """Provides contact data for the registration request.

    The per-extension schema from
    `GET /accounts/{account_id}/registrar/extensions/{extension}` defines the
    accepted contact roles. Every currently supported extension requires only
    `contacts.registrant` from API callers. Callers may provide additional roles
    such as `technical`, `administrator`, and `billing` when the extension
    schema includes them. When a registry requires an omitted role, Cloudflare
    may derive that contact from `contacts.registrant`.

    When the request omits either the entire `contacts` object or
    `contacts.registrant`, the system uses the account's default address book
    entry as the registrant contact. The account owner must configure this
    default at `https://dash.cloudflare.com/{account_id}/domains/registrations`,
    where they can create or update the address book entry and accept the
    required agreement. Dashboard settings currently provide the only way to
    manage address book entries.

    Without either a default address book entry or a registrant contact, the
    registration request fails validation.
    """

    administrator: ContactsAdministrator
    """Optional administrator contact.

    Accepted only when the extension schema includes this role. When the registry
    requires an omitted contact, Cloudflare may derive it from
    `contacts.registrant`.
    """

    billing: ContactsBilling
    """Optional billing contact.

    Accepted only when the extension schema includes this role. When the registry
    requires an omitted contact, Cloudflare may derive it from
    `contacts.registrant`.
    """

    registrant: ContactsRegistrant
    """Optional registrant contact.

    If omitted, the account's default address book entry is used instead.
    """

    technical: ContactsTechnical
    """Optional technical contact.

    Accepted only when the extension schema includes this role. When the registry
    requires an omitted contact, Cloudflare may derive it from
    `contacts.registrant`.
    """
