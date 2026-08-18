# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = [
    "ServerDeleteResponse",
    "AuthConfigSummary",
    "AuthConfigSummaryConfig",
    "AuthConfigSummaryRegistrationInfo",
    "ErrorDetails",
    "UpdatedPrompt",
    "UpdatedTool",
]


class AuthConfigSummaryConfig(BaseModel):
    authorization_endpoint: Optional[str] = None

    issuer: Optional[str] = None

    resource: Optional[str] = None

    revocation_endpoint: Optional[str] = None

    token_endpoint: Optional[str] = None


class AuthConfigSummaryRegistrationInfo(BaseModel):
    client_id: Optional[str] = None

    redirect_uris: Optional[List[str]] = None

    scope: Optional[str] = None

    token_endpoint_auth_method: Optional[str] = None


class AuthConfigSummary(BaseModel):
    """Safe subset of auth_credentials surfaced to the dashboard.

    Includes auth_mode (dcr|manual), has_client_secret, client_secret_version, and the OAuth endpoints + client_id for manual servers. Never includes the secret value.
    """

    auth_mode: Optional[Literal["dcr", "manual"]] = None

    client_secret_version: Optional[float] = None

    config: Optional[AuthConfigSummaryConfig] = None

    has_client_secret: Optional[bool] = None

    registration_info: Optional[AuthConfigSummaryRegistrationInfo] = None


class ErrorDetails(BaseModel):
    cause: Optional[str] = None
    """Underlying error message"""

    is_upstream: Optional[bool] = None
    """True = MCP server returned an error. False = couldn't reach the server"""

    mcp_code: Optional[float] = None
    """MCP protocol error code"""

    retryable: Optional[bool] = None
    """Whether the error is transient and worth retrying"""

    status_code: Optional[float] = None
    """HTTP status code from the server"""


class UpdatedPrompt(BaseModel):
    name: str
    """Name of the tool or prompt capability to override."""

    alias: Optional[str] = None
    """Custom name exposed for the capability."""

    description: Optional[str] = None
    """Custom description exposed for the capability."""

    enabled: Optional[bool] = None
    """Whether the capability is available through the MCP server."""


class UpdatedTool(BaseModel):
    name: str
    """Name of the tool or prompt capability to override."""

    alias: Optional[str] = None
    """Custom name exposed for the capability."""

    description: Optional[str] = None
    """Custom description exposed for the capability."""

    enabled: Optional[bool] = None
    """Whether the capability is available through the MCP server."""


class ServerDeleteResponse(BaseModel):
    id: str
    """Unique identifier for the MCP server."""

    auth_type: Literal["oauth", "bearer", "unauthenticated"]
    """Authentication method used to connect to the upstream MCP server."""

    hostname: str
    """URL of the upstream MCP endpoint."""

    name: str
    """Display name for the MCP server."""

    prompts: List[Dict[str, object]]

    tools: List[Dict[str, object]]

    auth_config_summary: Optional[AuthConfigSummary] = None
    """Safe subset of auth_credentials surfaced to the dashboard.

    Includes auth_mode (dcr|manual), has_client_secret, client_secret_version, and
    the OAuth endpoints + client_id for manual servers. Never includes the secret
    value.
    """

    authentication_status: Optional[Literal["not_required", "required", "connected", "stale", "manual"]] = None
    """
    Whether administrative authentication is required before capabilities can be
    synced. Manual OAuth is user-managed and has no administrative authentication
    flow.
    """

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None
    """Optional description of the MCP server."""

    error: Optional[str] = None

    error_details: Optional[ErrorDetails] = None

    is_shared_oauth_callback_enabled: Optional[bool] = None
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. Defaults to false (off); opt in per server by setting
    true.
    """

    last_successful_sync: Optional[datetime] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """
    Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.
    """

    status: Optional[Literal["waiting", "ready", "stale", "error"]] = None
    """Current sync state of the server"""

    updated_prompts: Optional[List[UpdatedPrompt]] = None
    """Server-wide prompt capability overrides."""

    updated_tools: Optional[List[UpdatedTool]] = None
    """Server-wide tool capability overrides."""
