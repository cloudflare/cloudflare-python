# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["QuotaGetResponse", "Advanced"]

class Advanced(BaseModel):
    allocated: Optional[int] = None
    """Quantity Allocated."""

    used: Optional[int] = None
    """Quantity Used."""

class QuotaGetResponse(BaseModel):
    advanced: Optional[Advanced] = None