# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PermissionGroupGetResponse", "Meta"]

class Meta(BaseModel):
    key: Optional[str] = None

    value: Optional[str] = None

class PermissionGroupGetResponse(BaseModel):
    id: str
    """Identifier of the group."""

    meta: Optional[Meta] = None
    """Attributes associated to the permission group."""

    name: Optional[str] = None
    """Name of the group."""