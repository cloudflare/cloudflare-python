# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ServerListResponse", "ErrorDetails", "UpdatedPrompt", "UpdatedTool"]


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

    alias: Optional[str] = None

    description: Optional[str] = None

    enabled: Optional[bool] = None


class UpdatedTool(BaseModel):
    name: str

    alias: Optional[str] = None

    description: Optional[str] = None

    enabled: Optional[bool] = None


class ServerListResponse(BaseModel):
    id: str
    """server id"""

    auth_type: Literal["oauth", "bearer", "unauthenticated"]

    hostname: str

    name: str

    prompts: List[Dict[str, object]]

    tools: List[Dict[str, object]]

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    error: Optional[str] = None

    error_details: Optional[ErrorDetails] = None

    is_shared_oauth_callback_enabled: Optional[bool] = None
    """
    When true, the gateway worker uses the shared Cloudflare-owned OAuth callback
    endpoint as the redirect_uri for upstream on-behalf OAuth, instead of the
    customer portal hostname. Operators manage this internal rollout flag through
    admin endpoints. Effective behavior is gated by the gateway worker's per-env
    rollout mode KV key.
    """

    last_successful_sync: Optional[datetime] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    status: Optional[str] = None

    updated_prompts: Optional[List[UpdatedPrompt]] = None

    updated_tools: Optional[List[UpdatedTool]] = None
