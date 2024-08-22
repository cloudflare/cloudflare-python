# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from .permission import Permission

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Role"]

class Role(BaseModel):
    id: str
    """Role identifier tag."""

    description: str
    """Description of role's permissions."""

    name: str
    """Role Name."""

    permissions: List[Permission]
    """Access permissions for this User."""