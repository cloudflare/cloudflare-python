# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["PortalReadResponse", "Server"]


class Server(BaseModel):
    id: str
    """server id"""

    auth_type: Literal["oauth", "bearer", "unauthenticated"]

    hostname: str

    name: str

    prompts: List[Dict[str, object]]

    tools: List[Dict[str, object]]

    updated_prompts: List[Dict[str, Union[float, str]]]

    updated_tools: List[Dict[str, Union[float, str]]]

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    default_disabled: Optional[bool] = None

    description: Optional[str] = None

    error: Optional[str] = None

    last_synced: Optional[datetime] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    on_behalf: Optional[bool] = None

    status: Optional[str] = None


class PortalReadResponse(BaseModel):
    id: str
    """portal id"""

    hostname: str

    name: str

    servers: List[Server]

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None
