# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HostnameAssociationGetResponse"]


class HostnameAssociationGetResponse(BaseModel):
    hostnames: Optional[List[str]] = None
