# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .acl import ACL
from ...._models import BaseModel

__all__ = ["ACLCreateResponse"]


class ACLCreateResponse(BaseModel):
    acls: Optional[List[ACL]] = None
