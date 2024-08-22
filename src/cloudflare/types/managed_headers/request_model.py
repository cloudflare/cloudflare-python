# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RequestModel"]

class RequestModel(BaseModel):
    id: Optional[str] = None
    """Human-readable identifier of the Managed Transform."""

    enabled: Optional[bool] = None
    """When true, the Managed Transform is enabled."""