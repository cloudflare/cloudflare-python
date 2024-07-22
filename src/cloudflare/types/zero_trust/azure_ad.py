# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .identity_provider_type import IdentityProviderType
from .identity_provider_scim_config import IdentityProviderSCIMConfig

__all__ = ["AzureAD", "Config"]


class Config(BaseModel):
    claims: Optional[List[str]] = None
    """Custom claims"""

    client_id: Optional[str] = None
    """Your OAuth Client ID"""

    client_secret: Optional[str] = None
    """Your OAuth Client Secret"""

    conditional_access_enabled: Optional[bool] = None
    """Should Cloudflare try to load authentication contexts from your account"""

    directory_id: Optional[str] = None
    """Your Azure directory uuid"""

    email_claim_name: Optional[str] = None
    """The claim name for email in the id_token response."""

    prompt: Optional[Literal["login", "select_account", "none"]] = None
    """Indicates the type of user interaction that is required.

    prompt=login forces the user to enter their credentials on that request,
    negating single-sign on. prompt=none is the opposite. It ensures that the user
    isn't presented with any interactive prompt. If the request can't be completed
    silently by using single-sign on, the Microsoft identity platform returns an
    interaction_required error. prompt=select_account interrupts single sign-on
    providing account selection experience listing all the accounts either in
    session or any remembered account or an option to choose to use a different
    account altogether.
    """

    support_groups: Optional[bool] = None
    """Should Cloudflare try to load groups from your account"""


class AzureAD(BaseModel):
    config: Config
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: str
    """The name of the identity provider, shown to users on the login page."""

    type: IdentityProviderType
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    id: Optional[str] = None
    """UUID"""

    scim_config: Optional[IdentityProviderSCIMConfig] = None
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """
