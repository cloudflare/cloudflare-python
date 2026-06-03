# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OAuthClientListResponse", "ClientURIVerification"]


class ClientURIVerification(BaseModel):
    """Client URI domain control verification state."""

    status: Optional[Literal["pending", "in_progress", "verified", "failed"]] = None
    """Current verification status for the client URI host."""

    text: Optional[str] = None
    """
    Exact TXT record value that must be added to DNS to prove ownership of the
    client URI host.
    """


class OAuthClientListResponse(BaseModel):
    """Fields shared by OAuth client responses and create/update requests."""

    client_id: str
    """The unique identifier for an OAuth client."""

    visibility: Literal["public", "private"]
    """Visibility of the OAuth client."""

    allowed_cors_origins: Optional[List[str]] = None
    """Array of allowed CORS origins."""

    client_name: Optional[str] = None
    """Human-readable name of the OAuth client."""

    client_uri: Optional[str] = None
    """URL of the home page of the client."""

    client_uri_verification: Optional[ClientURIVerification] = None
    """Client URI domain control verification state."""

    created_at: Optional[datetime] = None
    """Timestamp when the OAuth client was created."""

    grant_types: Optional[List[Literal["authorization_code", "refresh_token"]]] = None
    """Array of OAuth grant types the client is allowed to use.

    `authorization_code` is required; `refresh_token` may be included optionally.
    """

    has_rotated_secret: Optional[bool] = None
    """
    Indicates whether the client has a rotated secret that has not yet been deleted.
    """

    logo_uri: Optional[str] = None
    """URL of the client's logo."""

    policy_uri: Optional[str] = None
    """URL that points to a privacy policy document."""

    post_logout_redirect_uris: Optional[List[str]] = None
    """Array of allowed post-logout redirect URIs."""

    promoted_at: Optional[datetime] = None
    """Timestamp when the OAuth client was promoted to public visibility."""

    redirect_uris: Optional[List[str]] = None
    """Array of allowed redirect URIs for the client."""

    response_types: Optional[List[Literal["token", "id_token", "code"]]] = None
    """Array of OAuth response types the client is allowed to use."""

    scopes: Optional[List[str]] = None
    """Array of OAuth scopes the client is allowed to request.

    Colon-delimited scopes are not accepted. Dot-delimited scopes are validated
    against available OAuth API scopes; simple identity scopes are allowed. Protocol
    scopes `offline_access` and `openid` are added or removed automatically based on
    `grant_types` and `response_types`.
    """

    token_endpoint_auth_method: Optional[Literal["none", "client_secret_basic", "client_secret_post"]] = None
    """The authentication method the client uses at the token endpoint."""

    tos_uri: Optional[str] = None
    """URL that points to a terms of service document."""

    updated_at: Optional[datetime] = None
    """Timestamp when the OAuth client was last updated."""
