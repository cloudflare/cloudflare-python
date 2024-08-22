# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["IdentityProviderSCIMConfigParam"]

class IdentityProviderSCIMConfigParam(TypedDict, total=False):
    enabled: bool
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: bool
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

    seat_deprovision: bool
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: str
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: bool
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """