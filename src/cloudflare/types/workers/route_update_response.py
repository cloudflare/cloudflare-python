# File generated from our OpenAPI spec by Stainless.

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["RouteUpdateResponse"]


class RouteUpdateResponse(BaseModel):
    id: str
    """Identifier"""

    pattern: str

    script: str
    """Name of the script, used in URLs and route configuration."""
