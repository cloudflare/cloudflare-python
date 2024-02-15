# File generated from our OpenAPI spec by Stainless.

from typing import Optional, List

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..._models import BaseModel
from ...types import shared

__all__ = ["IndexDeleteByIDsResponse"]


class IndexDeleteByIDsResponse(BaseModel):
    count: Optional[int] = None
    """The count of the vectors successfully deleted."""

    ids: Optional[List[str]] = None
    """
    Array of vector identifiers of the vectors that were successfully processed for
    deletion.
    """
