# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams"]


class DelegationIPAddressManagementPrefixDelegationCreatePrefixDelegationParams(TypedDict, total=False):
    account_identifier: Required[str]
    """Identifier"""

    cidr: Required[str]
    """IP Prefix in Classless Inter-Domain Routing format."""

    delegated_account_id: Required[str]
    """Account identifier for the account to which prefix is being delegated."""
