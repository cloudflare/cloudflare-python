# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OAuthClientCreateParams"]


class OAuthClientCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    client_name: Required[str]
    """Human-readable name of the OAuth client."""

    grant_types: Required[List[Literal["authorization_code", "refresh_token"]]]
    """Array of OAuth grant types the client is allowed to use.

    `authorization_code` is required; `refresh_token` may be included optionally.
    """

    redirect_uris: Required[SequenceNotStr[str]]
    """Array of allowed redirect URIs for the client."""

    response_types: Required[List[Literal["token", "id_token", "code"]]]
    """Array of OAuth response types the client is allowed to use."""

    scopes: Required[SequenceNotStr[str]]
    """Array of OAuth scopes the client is allowed to request.

    Colon-delimited scopes are not accepted. Dot-delimited scopes are validated
    against available OAuth API scopes; simple identity scopes are allowed. Protocol
    scopes `offline_access` and `openid` are added or removed automatically based on
    `grant_types` and `response_types`.
    """

    token_endpoint_auth_method: Required[Literal["none", "client_secret_basic", "client_secret_post"]]
    """The authentication method the client uses at the token endpoint."""

    allowed_cors_origins: SequenceNotStr[str]
    """Array of allowed CORS origins."""

    client_uri: str
    """URL of the home page of the client."""

    logo_uri: str
    """URL of the client's logo."""

    policy_uri: str
    """URL that points to a privacy policy document."""

    post_logout_redirect_uris: SequenceNotStr[str]
    """Array of allowed post-logout redirect URIs."""

    tos_uri: str
    """URL that points to a terms of service document."""
