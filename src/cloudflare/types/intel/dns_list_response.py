# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing import List, Optional

from ..shared.response_info import ResponseInfo

from typing_extensions import Literal

from .dns import DNS

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["DNSListResponse"]

class DNSListResponse(BaseModel):
    errors: List[ResponseInfo]

    messages: List[ResponseInfo]

    success: Literal[True]
    """Whether the API call was successful"""

    result: Optional[DNS] = None