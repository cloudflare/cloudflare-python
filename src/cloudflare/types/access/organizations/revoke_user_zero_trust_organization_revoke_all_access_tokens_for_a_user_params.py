# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserParams"]


class RevokeUserZeroTrustOrganizationRevokeAllAccessTokensForAUserParams(TypedDict, total=False):
    account_or_zone: Required[str]

    email: Required[str]
    """The email of the user to revoke."""
