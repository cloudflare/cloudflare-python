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

    modified_at: Optional[datetime] = None

    modified_by: Optional[str] = None

    secure_web_gateway: Optional[bool] = None
    """Route outbound MCP traffic through Zero Trust Secure Web Gateway"""
