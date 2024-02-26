# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["OrganizationRevokeUsersParams"]


class OrganizationRevokeUsersParams(TypedDict, total=False):
    account_id: Required[str]
    """The Account ID to use for this endpoint. Mutually exclusive with the Zone ID."""

    zone_id: Required[str]
    """The Zone ID to use for this endpoint. Mutually exclusive with the Account ID."""

    email: Required[str]
    """The email of the user to revoke."""
