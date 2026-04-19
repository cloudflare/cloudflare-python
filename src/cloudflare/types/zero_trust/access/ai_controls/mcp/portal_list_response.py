# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["PortalListResponse", "Server", "ServerUpdatedPrompt", "ServerUpdatedTool"]


class ServerUpdatedPrompt(BaseModel):
    name: str

    description: Optional[str] = None

    enabled: Optional[bool] = None

    portal_alias: Optional[str] = None

    server_alias: Optional[str] = None


class ServerUpdatedTool(BaseModel):
    name: str

    description: Optional[str] = None

    enabled: Optional[bool] = None

    portal_alias: Optional[str] = None

    server_alias: Optional[str] = None


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

    last_successful_sync: Optional[datetime] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    on_behalf: Optional[bool] = None

    status: Optional[str] = None

    updated_prompts: Optional[List[ServerUpdatedPrompt]] = None

    updated_tools: Optional[List[ServerUpdatedTool]] = None


class PortalListResponse(BaseModel):
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
