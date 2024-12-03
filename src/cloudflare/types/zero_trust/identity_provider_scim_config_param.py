# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IdentityProviderSCIMConfigParam"]


class IdentityProviderSCIMConfigParam(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    identity_update_behavior: Literal["automatic", "reauth"]
    """Indicates how a SCIM event updates an Access identity.

    Use "automatic" to automatically update a user's Access identity and augment it
    with fields from the SCIM user resource. Use "reauth" to force re-authentication
    on group membership updates. With "reauth" Access identities will not contain
    fields from the SCIM user resource.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """
