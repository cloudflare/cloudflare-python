# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["ServerListResponse", "UpdatedPrompt", "UpdatedTool"]


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

    last_successful_sync: Optional[datetime] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    status: Optional[str] = None

    updated_prompts: Optional[List[UpdatedPrompt]] = None

    updated_tools: Optional[List[UpdatedTool]] = None
