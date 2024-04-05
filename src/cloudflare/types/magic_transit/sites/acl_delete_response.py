# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .acl import ACL
from ...._models import BaseModel

__all__ = ["ACLDeleteResponse"]


class ACLDeleteResponse(BaseModel):
    deleted: Optional[bool] = None

    deleted_acl: Optional[ACL] = None
    """Bidirectional ACL policy for network traffic within a site."""
