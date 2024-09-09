# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .hostname_association import HostnameAssociation

__all__ = ["HostnameAssociationUpdateResponse"]


class HostnameAssociationUpdateResponse(BaseModel):
    hostnames: Optional[List[HostnameAssociation]] = None
