# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional, List

from .hostname_association import HostnameAssociation

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["HostnameAssociationGetResponse"]


class HostnameAssociationGetResponse(BaseModel):
    hostnames: Optional[List[HostnameAssociation]] = None
