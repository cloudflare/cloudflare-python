# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ......_models import BaseModel

__all__ = ["PortalUpdateResponse"]


class PortalUpdateResponse(BaseModel):
    id: str
    """portal id"""

    hostname: str

    name: str

    allow_code_mode: Optional[bool] = None
    """Allow remote code execution in Dynamic Workers (beta)"""

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound MCP traffic through Zero Trust Secure Web Gateway"""
