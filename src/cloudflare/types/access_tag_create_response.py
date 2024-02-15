# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from .._models import BaseModel
from ..types import shared

__all__ = ["AccessTagCreateResponse"]


class AccessTagCreateResponse(BaseModel):
    name: str
    """The name of the tag"""

    app_count: Optional[int] = None
    """The number of applications that have this tag"""

    created_at: Optional[datetime] = None

    updated_at: Optional[datetime] = None
