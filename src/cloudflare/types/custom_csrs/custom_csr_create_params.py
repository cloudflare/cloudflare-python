# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["CustomCsrCreateParams"]


class CustomCsrCreateParams(TypedDict, total=False):
    common_name: Required[str]
    """The common name (domain) for the CSR. Must be at most 64 characters."""

    country: Required[str]
    """Two-letter ISO 3166-1 alpha-2 country code."""

    locality: Required[str]
    """City or locality name."""

    organization: Required[str]
    """Organization name."""

    sans: Required[SequenceNotStr[str]]
    """Subject Alternative Names for the CSR. At least one SAN is required."""

    state: Required[str]
    """State or province name."""

    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    description: str
    """Optional description for the CSR."""

    key_type: Literal["rsa2048", "p256v1"]
    """Key algorithm to use for the CSR. Defaults to rsa2048 if not specified."""

    name: str
    """Human-readable name for the CSR."""

    organizational_unit: str
    """Organizational unit name."""
