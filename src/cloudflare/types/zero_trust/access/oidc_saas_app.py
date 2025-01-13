# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OIDCSaaSApp", "CustomClaim", "CustomClaimSource", "HybridAndImplicitOptions", "RefreshTokenOptions"]


class CustomClaimSource(BaseModel):
    name: Optional[str] = None
    """The name of the IdP claim."""

    name_by_idp: Optional[Dict[str, str]] = None
    """A mapping from IdP ID to claim name."""


class CustomClaim(BaseModel):
    name: Optional[str] = None
    """The name of the claim."""

    required: Optional[bool] = None
    """If the claim is required when building an OIDC token."""

    scope: Optional[Literal["groups", "profile", "email", "openid"]] = None
    """The scope of the claim."""

    source: Optional[CustomClaimSource] = None


class HybridAndImplicitOptions(BaseModel):
    return_access_token_from_authorization_endpoint: Optional[bool] = None
    """If an Access Token should be returned from the OIDC Authorization endpoint"""

    return_id_token_from_authorization_endpoint: Optional[bool] = None
    """If an ID Token should be returned from the OIDC Authorization endpoint"""


class RefreshTokenOptions(BaseModel):
    lifetime: Optional[str] = None
    """How long a refresh token will be valid for after creation.

    Valid units are m,h,d. Must be longer than 1m.
    """


class OIDCSaaSApp(BaseModel):
    access_token_lifetime: Optional[str] = None
    """The lifetime of the OIDC Access Token after creation.

    Valid units are m,h. Must be greater than or equal to 1m and less than or equal
    to 24h.
    """

    allow_pkce_without_client_secret: Optional[bool] = None
    """
    If client secret should be required on the token endpoint when
    authorization_code_with_pkce grant is used.
    """

    app_launcher_url: Optional[str] = None
    """The URL where this applications tile redirects users"""

    auth_type: Optional[Literal["saml", "oidc"]] = None
    """Identifier of the authentication protocol used for the saas app.

    Required for OIDC.
    """

    client_id: Optional[str] = None
    """The application client id"""

    client_secret: Optional[str] = None
    """The application client secret, only returned on POST request."""

    created_at: Optional[datetime] = None

    custom_claims: Optional[List[CustomClaim]] = None

    grant_types: Optional[
        List[Literal["authorization_code", "authorization_code_with_pkce", "refresh_tokens", "hybrid", "implicit"]]
    ] = None
    """The OIDC flows supported by this application"""

    group_filter_regex: Optional[str] = None
    """A regex to filter Cloudflare groups returned in ID token and userinfo endpoint"""

    hybrid_and_implicit_options: Optional[HybridAndImplicitOptions] = None

    public_key: Optional[str] = None
    """The Access public certificate that will be used to verify your identity."""

    redirect_uris: Optional[List[str]] = None
    """
    The permitted URL's for Cloudflare to return Authorization codes and Access/ID
    tokens
    """

    refresh_token_options: Optional[RefreshTokenOptions] = None

    scopes: Optional[List[Literal["openid", "groups", "email", "profile"]]] = None
    """
    Define the user information shared with access, "offline_access" scope will be
    automatically enabled if refresh tokens are enabled
    """

    updated_at: Optional[datetime] = None
