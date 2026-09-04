# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = [
    "PortalReadResponse",
    "Server",
    "ServerAuthConfigSummary",
    "ServerAuthConfigSummaryConfig",
    "ServerAuthConfigSummaryRegistrationInfo",
    "ServerErrorDetails",
    "ServerUpdatedPrompt",
    "ServerUpdatedTool",
]


class ServerAuthConfigSummaryConfig(BaseModel):
    authorization_endpoint: Optional[str] = None

    issuer: Optional[str] = None

    resource: Optional[str] = None

    revocation_endpoint: Optional[str] = None

    token_endpoint: Optional[str] = None


class ServerAuthConfigSummaryRegistrationInfo(BaseModel):
    client_id: Optional[str] = None

    redirect_uris: Optional[List[str]] = None

    scope: Optional[str] = None

    token_endpoint_auth_method: Optional[str] = None


class ServerAuthConfigSummary(BaseModel):
    """Safe subset of auth_credentials surfaced to the dashboard.

    Includes auth_mode (dcr|manual), has_client_secret, client_secret_version, and the OAuth endpoints + client_id for manual servers. Never includes the secret value.
    """

    auth_mode: Optional[Literal["dcr", "manual"]] = None

    client_secret_version: Optional[float] = None

    config: Optional[ServerAuthConfigSummaryConfig] = None

    has_client_secret: Optional[bool] = None

    registration_info: Optional[ServerAuthConfigSummaryRegistrationInfo] = None


class ServerErrorDetails(BaseModel):
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


class ServerUpdatedPrompt(BaseModel):
    name: str

    enabled: Optional[bool] = None

    portal_alias: Optional[str] = None

    portal_description: Optional[str] = None

    server_alias: Optional[str] = None

    server_description: Optional[str] = None


class ServerUpdatedTool(BaseModel):
    name: str

    enabled: Optional[bool] = None

    portal_alias: Optional[str] = None

    portal_description: Optional[str] = None

    server_alias: Optional[str] = None

    server_description: Optional[str] = None


class Server(BaseModel):
    id: str
    """Unique identifier for the MCP server."""

    auth_type: Literal["oauth", "bearer", "unauthenticated"]
    """Authentication method used to connect to the upstream MCP server."""

    hostname: str
    """URL of the upstream MCP endpoint."""

    name: str
    """Display name for the MCP server."""

    prompts: List[Dict[str, object]]

    server_id: str
    """Unique identifier for the MCP server."""

    tools: List[Dict[str, object]]

    auth_config_summary: Optional[ServerAuthConfigSummary] = None
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

    default_disabled: Optional[bool] = None

    description: Optional[str] = None
    """Optional description of the MCP server."""

    error: Optional[str] = None

    error_details: Optional[ServerErrorDetails] = None

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

    on_behalf: Optional[bool] = None

    secure_web_gateway: Optional[bool] = None
    """
    Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway.
    """

    status: Optional[Literal["waiting", "ready", "stale", "error"]] = None
    """Current sync state of the server"""

    updated_prompts: Optional[List[ServerUpdatedPrompt]] = None

    updated_tools: Optional[List[ServerUpdatedTool]] = None


class PortalReadResponse(BaseModel):
    id: str
    """Unique identifier for the MCP portal."""

    hostname: str
    """Hostname where the MCP portal is available."""

    name: str
    """Display name for the MCP portal."""

    servers: List[Server]

    allow_code_mode: Optional[bool] = None
    """Deprecated: use `code_mode` for new integrations.

    `true` maps to any non-off Code Mode policy; `false` maps to `code_mode: off`.
    If both fields are sent, they must be consistent or the request returns a 400.
    """

    code_mode: Optional[Literal["off", "opt_in", "default_on", "enforced"]] = None
    """Code Mode policy for this portal.

    `off`: Code Mode is unavailable; query parameters are ignored. `opt_in`: Code
    Mode is off by default; clients turn it on with `?codemode=search_and_execute`.
    `default_on`: Code Mode is on by default; clients can opt out with
    `?codemode=off`. `enforced`: Code Mode is always on; query parameters are
    ignored. Defaults to `opt_in` when omitted on create. If both `code_mode` and
    `allow_code_mode` are sent, they must be consistent or the request returns
    a 400.
    """

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None
    """Optional description of the MCP portal."""

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound MCP traffic through Zero Trust Secure Web Gateway."""
