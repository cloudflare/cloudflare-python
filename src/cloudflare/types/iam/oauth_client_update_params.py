# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["OAuthClientUpdateParams"]


class OAuthClientUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Account identifier tag."""

    allowed_cors_origins: SequenceNotStr[str]
    """Array of allowed CORS origins."""

    client_name: str
    """Human-readable name of the OAuth client."""

    client_uri: str
    """URL of the home page of the client."""

    grant_types: List[Literal["authorization_code", "refresh_token"]]
    """Array of OAuth grant types the client is allowed to use.

    `authorization_code` is required; `refresh_token` may be included optionally.
    """

    logo_uri: str
    """URL of the client's logo."""

    policy_uri: str
    """URL that points to a privacy policy document."""

    post_logout_redirect_uris: SequenceNotStr[str]
    """Array of allowed post-logout redirect URIs."""

    redirect_uris: SequenceNotStr[str]
    """Array of allowed redirect URIs for the client."""

    response_types: List[Literal["token", "id_token", "code"]]
    """Array of OAuth response types the client is allowed to use."""

    scopes: SequenceNotStr[str]
    """Array of OAuth scopes the client is allowed to request.

    Colon-delimited scopes are not accepted. Dot-delimited scopes are validated
    against available OAuth API scopes; simple identity scopes are allowed. Protocol
    scopes `offline_access` and `openid` are added or removed automatically based on
    `grant_types` and `response_types`.
    """

    token_endpoint_auth_method: Literal["none", "client_secret_basic", "client_secret_post"]
    """The authentication method the client uses at the token endpoint."""

    tos_uri: str
    """URL that points to a terms of service document."""

    visibility: Literal["public"]
    """Promote the OAuth client from private to public visibility.

    Only `public` is accepted; demotion to `private` is not supported. Promotion
    requires a non-empty client name, logo URI, verified client URI host, and at
    least one non-identity scope.
    """
