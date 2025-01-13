# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["OIDCSaaSAppParam", "CustomClaim", "CustomClaimSource", "HybridAndImplicitOptions", "RefreshTokenOptions"]


class CustomClaimSource(TypedDict, total=False):
    name: str
    """The name of the IdP claim."""

    name_by_idp: Dict[str, str]
    """A mapping from IdP ID to claim name."""


class CustomClaim(TypedDict, total=False):
    name: str
    """The name of the claim."""

    required: bool
    """If the claim is required when building an OIDC token."""

    scope: Literal["groups", "profile", "email", "openid"]
    """The scope of the claim."""

    source: CustomClaimSource


class HybridAndImplicitOptions(TypedDict, total=False):
    return_access_token_from_authorization_endpoint: bool
    """If an Access Token should be returned from the OIDC Authorization endpoint"""

    return_id_token_from_authorization_endpoint: bool
    """If an ID Token should be returned from the OIDC Authorization endpoint"""


class RefreshTokenOptions(TypedDict, total=False):
    lifetime: str
    """How long a refresh token will be valid for after creation.

    Valid units are m,h,d. Must be longer than 1m.
    """


class OIDCSaaSAppParam(TypedDict, total=False):
    access_token_lifetime: str
    """The lifetime of the OIDC Access Token after creation.

    Valid units are m,h. Must be greater than or equal to 1m and less than or equal
    to 24h.
    """

    allow_pkce_without_client_secret: bool
    """
    If client secret should be required on the token endpoint when
    authorization_code_with_pkce grant is used.
    """

    app_launcher_url: str
    """The URL where this applications tile redirects users"""

    auth_type: Literal["saml", "oidc"]
    """Identifier of the authentication protocol used for the saas app.

    Required for OIDC.
    """

    client_id: str
    """The application client id"""

    client_secret: str
    """The application client secret, only returned on POST request."""

    custom_claims: Iterable[CustomClaim]

    grant_types: List[
        Literal["authorization_code", "authorization_code_with_pkce", "refresh_tokens", "hybrid", "implicit"]
    ]
    """The OIDC flows supported by this application"""

    group_filter_regex: str
    """A regex to filter Cloudflare groups returned in ID token and userinfo endpoint"""

    hybrid_and_implicit_options: HybridAndImplicitOptions

    public_key: str
    """The Access public certificate that will be used to verify your identity."""

    redirect_uris: List[str]
    """
    The permitted URL's for Cloudflare to return Authorization codes and Access/ID
    tokens
    """

    refresh_token_options: RefreshTokenOptions

    scopes: List[Literal["openid", "groups", "email", "profile"]]
    """
    Define the user information shared with access, "offline_access" scope will be
    automatically enabled if refresh tokens are enabled
    """
