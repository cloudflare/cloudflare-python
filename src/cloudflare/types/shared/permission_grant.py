# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PermissionGrant"]


class PermissionGrant(BaseModel):
    read: Optional[bool] = None

    write: Optional[bool] = None
