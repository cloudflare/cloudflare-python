# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["IdentityProviderSCIMConfig"]


class IdentityProviderSCIMConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    identity_update_behavior: Optional[Literal["automatic", "reauth", "no_action"]] = None
    """Indicates how a SCIM event updates a user identity used for policy evaluation.

    Use "automatic" to automatically update a user's identity and augment it with
    fields from the SCIM user resource. Use "reauth" to force re-authentication on
    group membership updates, user identity update will only occur after successful
    re-authentication. With "reauth" identities will not contain fields from the
    SCIM user resource. With "no_action" identities will not be changed by SCIM
    updates in any way and users will not be prompted to reauthenticate.
    """

    scim_base_url: Optional[str] = None
    """The base URL of Cloudflare's SCIM V2.0 API endpoint."""

    seat_deprovision: Optional[bool] = None
    """
    A flag to remove a user's seat in Zero Trust when they have been deprovisioned
    in the Identity Provider. This cannot be enabled unless user_deprovision is also
    enabled.
    """

    secret: Optional[str] = None
    """
    A read-only token generated when the SCIM integration is enabled for the first
    time. It is redacted on subsequent requests. If you lose this you will need to
    refresh it at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """
