# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RegistrarCheckResponse", "Domain", "DomainPricing"]


class DomainPricing(BaseModel):
    """Annual pricing information for a registrable domain.

    This object is only
    present when `registrable` is `true`. All prices are per year and returned
    as strings to preserve decimal precision.

    `registration_cost` and `renewal_cost` are frequently the same value, but
    may differ — especially for premium domains where registries set different
    rates for initial registration vs. renewal. For a multi-year registration
    (e.g., 4 years), the first year is charged at `registration_cost` and each
    subsequent year at `renewal_cost`. Registry pricing may change over time;
    the values returned here reflect the current registry rate. Premium pricing
    may be surfaced by Search and Check, but premium registration is not currently
    supported by this API.
    """

    currency: str
    """ISO-4217 currency code for the prices (e.g., "USD", "EUR", "GBP")."""

    registration_cost: str
    """The first-year cost to register this domain.

    For premium domains (`tier: premium`), this price is set by the registry and may
    be significantly higher than standard pricing. For multi-year registrations,
    this cost applies to the first year only; subsequent years are charged at
    `renewal_cost`.
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
    Represents a single authoritative domain availability result returned by the Check endpoint. Check results reflect current registry status and should be used immediately before registration.
    """

    name: str
    """
    The fully qualified domain name (FQDN) in punycode format for internationalized
    domain names (IDNs).
    """

    registrable: bool
    """
    Indicates whether this domain can be registered programmatically through this
    API based on a real-time registry check.

    - `true`: Domain is available for registration. The `pricing` object will be
      included.
    - `false`: Domain is not available. See the `reason` field for why. `tier` may
      still be present on some non-registrable results, such as premium domains.
    """

    pricing: Optional[DomainPricing] = None
    """Annual pricing information for a registrable domain.

    This object is only present when `registrable` is `true`. All prices are per
    year and returned as strings to preserve decimal precision.

    `registration_cost` and `renewal_cost` are frequently the same value, but may
    differ — especially for premium domains where registries set different rates for
    initial registration vs. renewal. For a multi-year registration (e.g., 4 years),
    the first year is charged at `registration_cost` and each subsequent year at
    `renewal_cost`. Registry pricing may change over time; the values returned here
    reflect the current registry rate. Premium pricing may be surfaced by Search and
    Check, but premium registration is not currently supported by this API.
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
    """Present only when `registrable` is `false`.

    Explains why the domain cannot be registered via this API.

    - `extension_not_supported_via_api`: Cloudflare Registrar supports this
      extension in the dashboard but it is not yet available for programmatic
      registration via this API. The user can register via
      `https://dash.cloudflare.com/{account_id}/domains/registrations`.
    - `extension_not_supported`: This extension is not supported by Cloudflare
      Registrar at all.
    - `extension_disallows_registration`: The extension's registry has temporarily
      or permanently frozen new registrations. No registrar can register domains on
      this extension at this time.
    - `domain_premium`: The domain is premium priced. Premium registration is not
      currently supported by this API.
    - `domain_unavailable`: The domain is already registered, reserved, or otherwise
      not available on a supported extension.
    """

    tier: Optional[Literal["standard", "premium"]] = None
    """The pricing tier for this domain.

    Always present when `registrable` is `true`; defaults to `standard` for most
    domains. May be absent when `registrable` is `false`.

    - `standard`: Standard registry pricing
    - `premium`: Premium domain with higher pricing set by the registry
    """


class RegistrarCheckResponse(BaseModel):
    """Contains the availability check results."""

    domains: List[Domain]
    """Array of domain availability results.

    Domains on unsupported extensions are included with `registrable: false` and a
    `reason` field. Malformed domain names may be omitted.
    """
