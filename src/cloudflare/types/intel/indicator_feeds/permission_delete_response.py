# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["PermissionDeleteResponse"]

class PermissionDeleteResponse(BaseModel):
    success: Optional[bool] = None
    """Whether the update succeeded or not"""