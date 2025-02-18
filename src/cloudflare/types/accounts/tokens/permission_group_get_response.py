# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["PermissionGroupGetResponse"]


class PermissionGroupGetResponse(BaseModel):
    id: Optional[str] = None
    """Public ID."""

    name: Optional[str] = None
    """Permission Group Name"""

    scopes: Optional[
        List[
            Literal[
                "com.cloudflare.api.account",
                "com.cloudflare.api.account.zone",
                "com.cloudflare.api.user",
                "com.cloudflare.edge.r2.bucket",
            ]
        ]
    ] = None
    """Resources to which the Permission Group is scoped"""
