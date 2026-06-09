# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["PortalUpdateResponse", "Server", "ServerErrorDetails", "ServerUpdatedPrompt", "ServerUpdatedTool"]


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
    """server id"""

    auth_type: Literal["oauth", "bearer", "unauthenticated"]

    hostname: str

    name: str

    prompts: List[Dict[str, object]]

    tools: List[Dict[str, object]]

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    default_disabled: Optional[bool] = None

    description: Optional[str] = None

    error: Optional[str] = None

    error_details: Optional[ServerErrorDetails] = None

    is_shared_oauth_callback_enabled: Optional[bool] = None
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. New public server creates default to true; existing
    servers default to false from migration until explicitly updated. Effective
    behavior is gated by the gateway worker's per-env rollout mode KV key.
    """

    last_successful_sync: Optional[datetime] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    on_behalf: Optional[bool] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound traffic to this MCP server through Zero Trust Secure Web Gateway"""

    status: Optional[str] = None

    updated_prompts: Optional[List[ServerUpdatedPrompt]] = None

    updated_tools: Optional[List[ServerUpdatedTool]] = None


class PortalUpdateResponse(BaseModel):
    id: str
    """portal id"""

    hostname: str

    name: str

    servers: List[Server]

    allow_code_mode: Optional[bool] = None
    """Allow remote code execution in Dynamic Workers (beta)"""

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound MCP traffic through Zero Trust Secure Web Gateway"""
