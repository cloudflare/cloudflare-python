# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import Optional

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["ListDeleteResponse"]

class ListDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique ID of the item in the List."""