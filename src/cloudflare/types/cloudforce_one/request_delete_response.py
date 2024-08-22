# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List

from ..shared.response_info import ResponseInfo

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RequestDeleteResponse"]

class RequestDeleteResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""