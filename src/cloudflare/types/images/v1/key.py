# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Key"]

class Key(BaseModel):
    name: Optional[str] = None
    """Key name."""

    value: Optional[str] = None
    """Key value."""