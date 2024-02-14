# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ...._models import BaseModel
from ....types import shared

__all__ = ["OperationUpdateResponse", "OperationUpdateResponseItem"]


class OperationUpdateResponseItem(BaseModel):
    operation_id: Optional[str] = None
    """UUID identifier"""

    state: Optional[Literal["review", "ignored"]] = None
    """Mark state of operation in API Discovery

    - `review` - Mark operation as for review
    - `ignored` - Mark operation as ignored
    """


OperationUpdateResponse = Dict[str, OperationUpdateResponseItem]
