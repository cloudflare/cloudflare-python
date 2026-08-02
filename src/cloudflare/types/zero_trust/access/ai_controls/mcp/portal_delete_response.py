# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ......_models import BaseModel

__all__ = ["PortalDeleteResponse"]


class PortalDeleteResponse(BaseModel):
    id: str
    """portal id"""

    hostname: str

    name: str

    allow_code_mode: Optional[bool] = None
    """Deprecated: use `code_mode` instead.

    Legacy on/off toggle for Dynamic Workers (codemode). `true` maps to any non-off
    `code_mode`; `false` maps to `code_mode: off`.
    """

    code_mode: Optional[Literal["off", "opt_in", "default_on", "enforced"]] = None
    """Controls Dynamic Workers (codemode) availability for this portal.

    `off` disables codemode. `opt_in` makes it available but clients must opt in per
    session. `default_on` enables it by default with a client override. `enforced`
    requires codemode for every session with no override.
    """

    created_at: Optional[datetime] = None

    created_by: Optional[str] = None

    description: Optional[str] = None

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound MCP traffic through Zero Trust Secure Web Gateway"""
