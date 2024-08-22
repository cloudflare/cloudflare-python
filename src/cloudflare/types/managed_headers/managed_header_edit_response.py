# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ManagedHeaderEditResponse", "ManagedRequestHeader", "ManagedResponseHeader"]

class ManagedRequestHeader(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    available: Optional[bool] = None
    """When true, the Managed Transform is available in the current Cloudflare plan."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""

class ManagedResponseHeader(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    available: Optional[bool] = None
    """When true, the Managed Transform is available in the current Cloudflare plan."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""

class ManagedHeaderEditResponse(BaseModel):
    managed_request_headers: Optional[List[ManagedRequestHeader]] = None

    managed_response_headers: Optional[List[ManagedResponseHeader]] = None