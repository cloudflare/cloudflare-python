# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["IdentityProviderSCIMConfig"]


class IdentityProviderSCIMConfig(BaseModel):
    enabled: Optional[bool] = None
    """A flag to enable or disable SCIM for the identity provider."""

    group_member_deprovision: Optional[bool] = None
    """
    A flag to revoke a user's session in Access and force a reauthentication on the
    user's Gateway session when they have been added or removed from a group in the
    Identity Provider.
    """

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
    refresh it token at /access/identity_providers/:idpID/refresh_scim_secret.
    """

    user_deprovision: Optional[bool] = None
    """
    A flag to enable revoking a user's session in Access and Gateway when they have
    been deprovisioned in the Identity Provider.
    """
