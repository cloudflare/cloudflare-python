# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from datetime import datetime

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Stage"]

class Stage(BaseModel):
    ended_on: Optional[datetime] = None
    """When the stage ended."""

    name: Optional[str] = None
    """The current build stage."""

    started_on: Optional[datetime] = None
    """When the stage started."""

    status: Optional[str] = None
    """State of the current stage."""