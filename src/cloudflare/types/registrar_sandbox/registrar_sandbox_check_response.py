# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegistrarSandboxCheckResponse", "Domain", "DomainPricing"]


class DomainPricing(BaseModel):
    """Provides annual pricing information for a registrable domain.

    This object
    appears only when `registrable` is `true`. The API returns all per-year
    prices as strings to preserve decimal precision.

    `registration_cost` and `renewal_cost` frequently have the same value, but
    may differ, especially when registries set different premium rates for
    initial registration and renewal. For a multi-year registration (e.g., 4
    years), `registration_cost` applies to the first year and `renewal_cost`
    applies to each subsequent year. The values reflect the current registry
    rate, which may change over time. Search and Check may surface premium
    pricing, but this API currently supports standard registrations only.
    """

    currency: str
    """ISO-4217 currency code for the prices (e.g., "USD", "EUR", "GBP")."""

    registration_cost: str
    """The first-year cost to register this domain.

    For premium domains (`tier: premium`), the registry sets this price, which may
    significantly exceed standard pricing. For multi-year registrations, this cost
    applies to the first year only; `renewal_cost` applies to subsequent years.
    """

    renewal_cost: str
    """Per-year renewal cost for this domain.

    Applied to each year beyond the first year of a multi-year registration, and to
    each annual auto-renewal thereafter. May differ from `registration_cost`,
    especially for premium domains where initial registration often costs more than
    renewals.
    """


class Domain(BaseModel):
    """
    Describes a single authoritative domain availability result from the Check endpoint. Check results reflect current registry status; use them immediately before registration.
    """

    name: str
    """
    The fully qualified domain name (FQDN) in punycode format for internationalized
    domain names (IDNs).
    """

    registrable: bool
    """
    Indicates programmatic registration eligibility according to a real-time
    registry check.

    - `true`: The domain is available for registration. The response includes the
      `pricing` object.
    - `false`: A restriction prevents registration. See the `reason` field for
      details. Some results, such as premium domains, may still include `tier`.
    """

    pricing: Optional[DomainPricing] = None
    """Provides annual pricing information for a registrable domain.

    This object appears only when `registrable` is `true`. The API returns all
    per-year prices as strings to preserve decimal precision.

    `registration_cost` and `renewal_cost` frequently have the same value, but may
    differ, especially when registries set different premium rates for initial
    registration and renewal. For a multi-year registration (e.g., 4 years),
    `registration_cost` applies to the first year and `renewal_cost` applies to each
    subsequent year. The values reflect the current registry rate, which may change
    over time. Search and Check may surface premium pricing, but this API currently
    supports standard registrations only.
    """

    reason: Optional[
        Literal[
            "extension_not_supported_via_api",
            "extension_not_supported",
            "extension_disallows_registration",
            "domain_premium",
            "domain_unavailable",
        ]
    ] = None
    """Appears only when `registrable` is `false` and explains the result.

    - `extension_not_supported_via_api`: Cloudflare Registrar supports this
      extension in the dashboard but currently excludes it from programmatic
      registration through this API. The user can register via
      `https://dash.cloudflare.com/{account_id}/domains/registrations`.
    - `extension_not_supported`: Cloudflare Registrar excludes this extension
      entirely.
    - `extension_disallows_registration`: The extension's registry temporarily or
      permanently freezes new registrations. Registrars currently cannot register
      domains on this extension.
    - `domain_premium`: The domain carries premium pricing. This API currently
      supports standard registrations only.
    - `domain_unavailable`: An existing registration, reservation, or other registry
      restriction makes the domain unavailable on a supported extension.
    """

    tier: Optional[Literal["standard", "premium"]] = None
    """The pricing tier for this domain.

    A `registrable` value of `true` always includes this field, which defaults to
    `standard` for most domains. A `registrable` value of `false` may omit it.

    - `standard`: Standard registry pricing.
    - `premium`: Premium domain with higher pricing from the registry.
    """


class RegistrarSandboxCheckResponse(BaseModel):
    """Contains the availability check results."""

    domains: List[Domain]
    """Array of domain availability results.

    Results for unsupported extensions contain `registrable: false` and a `reason`
    field. The response may omit malformed domain names.
    """
