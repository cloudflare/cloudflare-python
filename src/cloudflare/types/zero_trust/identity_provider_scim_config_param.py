# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IdentityProviderSCIMConfigParam"]


class IdentityProviderSCIMConfigParam(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    identity_update_behavior: Literal["automatic", "reauth", "no_action"]
    """Indicates how a SCIM event updates a user identity used for policy evaluation.

    Use "automatic" to automatically update a user's identity and augment it with
    fields from the SCIM user resource. Use "reauth" to force re-authentication on
    group membership updates, user identity update will only occur after successful
    re-authentication. With "reauth" identities will not contain fields from the
    SCIM user resource. With "no_action" identities will not be changed by SCIM
    updates in any way and users will not be prompted to reauthenticate.
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
