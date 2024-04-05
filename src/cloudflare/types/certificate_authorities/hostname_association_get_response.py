# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .hostname_association_item import HostnameAssociationItem

__all__ = ["HostnameAssociationGetResponse"]


class HostnameAssociationGetResponse(BaseModel):
    hostnames: Optional[List[HostnameAssociationItem]] = None
