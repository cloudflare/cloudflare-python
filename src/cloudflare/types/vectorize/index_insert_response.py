# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndexInsertResponse"]


class IndexInsertResponse(BaseModel):
    count: Optional[int] = None
    """Specifies the count of the vectors successfully inserted."""

    ids: Optional[List[str]] = None
    """Array of vector identifiers of the vectors successfully inserted."""
