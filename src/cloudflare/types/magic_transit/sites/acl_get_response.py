# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .acl import ACL
from ...._models import BaseModel

__all__ = ["ACLGetResponse"]


class ACLGetResponse(BaseModel):
    acl: Optional[ACL] = None
    """Bidirectional ACL policy for network traffic within a site."""
