# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IdentityProviderListParams"]


class IdentityProviderListParams(TypedDict, total=False):
    account_id: str
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: str
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    scim_enabled: str
    """
    Indicates to Access to only retrieve identity providers that have the System for
    Cross-Domain Identity Management (SCIM) enabled.
    """
