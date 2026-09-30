# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "RegistrarTransferCheckResponse",
    "Domains",
    "DomainsTransferableResult",
    "DomainsTransferableResultPricing",
    "DomainsTransferableResultReason",
    "DomainsNonTransferableResult",
    "DomainsNonTransferableResultPricing",
    "DomainsNonTransferableResultReason",
]


class DomainsTransferableResultPricing(BaseModel):
    """
    Provides annual pricing information for a given domain.
    The API returns all per-year prices as strings to preserve decimal precision.

    `renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value,
    but may differ due to premium rates for certain domains.

    For a multi-year operations, the operation's cost applies to the first year
    and `renewal_cost` applies to each subsequent year. The values reflect the current
    registry rate, which can change over time.
    """

    currency: str
    """ISO-4217 currency code for the prices (e.g., "USD", "EUR", "GBP")."""

    renewal_cost: str
    """Per-year renewal cost for this domain.

    Applied to each year beyond the first year of a multi-year registration, and to
    each annual auto-renewal thereafter. May differ from `registration_cost`,
    especially for premium domains where initial registration often costs more than
    renewals.
    """

    transfer_cost: str
    """The first-year cost to transfer this domain."""


class DomainsTransferableResultReason(BaseModel):
    code: Literal[
        "extension_not_supported_via_api",
        "extension_not_supported",
        "domain_premium",
        "extension_disallows_transfer",
        "domain_not_exists",
        "domain_on_cloudflare",
        "domain_locked",
        "registry_status",
        "domain_outside_transfer_window",
        "domain_max_term",
        "invalid_auth_code",
        "invalid_auth_code_format",
        "dnssec_enabled",
        "zone_not_found",
        "zone_status_invalid",
        "invalid_zone_plan",
        "domain_unsupported",
    ]
    """Transfer eligibility reason code.

    - `extension_not_supported_via_api`: This API excludes the extension; dashboard
      flows support it.
    - `extension_not_supported`: Cloudflare Registrar excludes the extension.
    - `domain_premium`: This API currently excludes premium transfers.
    - `extension_disallows_transfer`: Extension currently blocks transfer
      operations.
    - `domain_not_exists`: No registration record exists for the domain.
    - `domain_on_cloudflare`: Cloudflare already serves as the domain's registrar.
    - `domain_locked`: Losing registrar reports transfer-prohibited lock status.
    - `registry_status`: Registry status currently blocks transfer (for example,
      pending transfer or deletion state).
    - `domain_outside_transfer_window`: Domain is within a transfer wait window (for
      example, recently registered).
    - `domain_max_term`: Completing transfer would exceed the registry maximum term.
    - `invalid_auth_code`: The provided auth code is incorrect.
    - `invalid_auth_code_format`: Auth code fails Base64 validation.
    - `dnssec_enabled`: DNSSEC is enabled. It must be disabled before transfer.
    - `zone_not_found`: The target account lacks a Cloudflare zone for the domain.
    - `zone_status_invalid`: The Cloudflare zone cannot transfer in its current
      state.
    - `invalid_zone_plan`: The zone plan fails transfer requirements.
    - `domain_unsupported`: This endpoint rejects the domain name format.
    """


class DomainsTransferableResult(BaseModel):
    pricing: DomainsTransferableResultPricing
    """
    Provides annual pricing information for a given domain. The API returns all
    per-year prices as strings to preserve decimal precision.

    `renewal_cost` and `registration_cost` or `transfer_cost` are frequently the
    same value, but may differ due to premium rates for certain domains.

    For a multi-year operations, the operation's cost applies to the first year and
    `renewal_cost` applies to each subsequent year. The values reflect the current
    registry rate, which can change over time.
    """

    transferable: Literal[True]

    name: Optional[str] = None
    """The check evaluates this domain name."""

    reasons: Optional[List[DomainsTransferableResultReason]] = None


class DomainsNonTransferableResultPricing(BaseModel):
    """
    Provides annual pricing information for a given domain.
    The API returns all per-year prices as strings to preserve decimal precision.

    `renewal_cost` and `registration_cost` or `transfer_cost` are frequently the same value,
    but may differ due to premium rates for certain domains.

    For a multi-year operations, the operation's cost applies to the first year
    and `renewal_cost` applies to each subsequent year. The values reflect the current
    registry rate, which can change over time.
    """

    currency: str
    """ISO-4217 currency code for the prices (e.g., "USD", "EUR", "GBP")."""

    renewal_cost: str
    """Per-year renewal cost for this domain.

    Applied to each year beyond the first year of a multi-year registration, and to
    each annual auto-renewal thereafter. May differ from `registration_cost`,
    especially for premium domains where initial registration often costs more than
    renewals.
    """

    transfer_cost: str
    """The first-year cost to transfer this domain."""


class DomainsNonTransferableResultReason(BaseModel):
    code: Literal[
        "extension_not_supported_via_api",
        "extension_not_supported",
        "domain_premium",
        "extension_disallows_transfer",
        "domain_not_exists",
        "domain_on_cloudflare",
        "domain_locked",
        "registry_status",
        "domain_outside_transfer_window",
        "domain_max_term",
        "invalid_auth_code",
        "invalid_auth_code_format",
        "dnssec_enabled",
        "zone_not_found",
        "zone_status_invalid",
        "invalid_zone_plan",
        "domain_unsupported",
    ]
    """Transfer eligibility reason code.

    - `extension_not_supported_via_api`: This API excludes the extension; dashboard
      flows support it.
    - `extension_not_supported`: Cloudflare Registrar excludes the extension.
    - `domain_premium`: This API currently excludes premium transfers.
    - `extension_disallows_transfer`: Extension currently blocks transfer
      operations.
    - `domain_not_exists`: No registration record exists for the domain.
    - `domain_on_cloudflare`: Cloudflare already serves as the domain's registrar.
    - `domain_locked`: Losing registrar reports transfer-prohibited lock status.
    - `registry_status`: Registry status currently blocks transfer (for example,
      pending transfer or deletion state).
    - `domain_outside_transfer_window`: Domain is within a transfer wait window (for
      example, recently registered).
    - `domain_max_term`: Completing transfer would exceed the registry maximum term.
    - `invalid_auth_code`: The provided auth code is incorrect.
    - `invalid_auth_code_format`: Auth code fails Base64 validation.
    - `dnssec_enabled`: DNSSEC is enabled. It must be disabled before transfer.
    - `zone_not_found`: The target account lacks a Cloudflare zone for the domain.
    - `zone_status_invalid`: The Cloudflare zone cannot transfer in its current
      state.
    - `invalid_zone_plan`: The zone plan fails transfer requirements.
    - `domain_unsupported`: This endpoint rejects the domain name format.
    """


class DomainsNonTransferableResult(BaseModel):
    transferable: Literal[False]

    name: Optional[str] = None
    """The check evaluates this domain name."""

    pricing: Optional[DomainsNonTransferableResultPricing] = None
    """
    Provides annual pricing information for a given domain. The API returns all
    per-year prices as strings to preserve decimal precision.

    `renewal_cost` and `registration_cost` or `transfer_cost` are frequently the
    same value, but may differ due to premium rates for certain domains.

    For a multi-year operations, the operation's cost applies to the first year and
    `renewal_cost` applies to each subsequent year. The values reflect the current
    registry rate, which can change over time.
    """

    reasons: Optional[List[DomainsNonTransferableResultReason]] = None


Domains: TypeAlias = Union[DomainsTransferableResult, DomainsNonTransferableResult]


class RegistrarTransferCheckResponse(BaseModel):
    """Contains the transfer eligibility results."""

    domains: Dict[str, Domains]
    """
    Maps domain names to transfer eligibility results. Each value contains `name`,
    `transferable`, and `reasons`.
    """
