# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from .identity_provider_type import IdentityProviderType
from .identity_provider_scim_config_param import IdentityProviderSCIMConfigParam

__all__ = ["AzureADParam", "Config"]


class Config(TypedDict, total=False):
    claims: List[str]
    """Custom claims"""

    client_id: str
    """Your OAuth Client ID"""

    client_secret: str
    """Your OAuth Client Secret"""

    conditional_access_enabled: bool
    """Should Cloudflare try to load authentication contexts from your account"""

    directory_id: str
    """Your Azure directory uuid"""

    email_claim_name: str
    """The claim name for email in the id_token response."""

    prompt: Literal["login", "select_account", "none"]
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

    support_groups: bool
    """Should Cloudflare try to load groups from your account"""


class AzureADParam(TypedDict, total=False):
    config: Required[Config]
    """The configuration parameters for the identity provider.

    To view the required parameters for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    name: Required[str]
    """The name of the identity provider, shown to users on the login page."""

    type: Required[IdentityProviderType]
    """The type of identity provider.

    To determine the value for a specific provider, refer to our
    [developer documentation](https://developers.cloudflare.com/cloudflare-one/identity/idp-integration/).
    """

    scim_config: IdentityProviderSCIMConfigParam
    """
    The configuration settings for enabling a System for Cross-Domain Identity
    Management (SCIM) with the identity provider.
    """
