# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Stat", "Count"]

class Count(BaseModel):
    allowed: Optional[float] = None
    """Cloudflare Images allowed usage."""

    current: Optional[float] = None
    """Cloudflare Images current usage."""

class Stat(BaseModel):
    count: Optional[Count] = None