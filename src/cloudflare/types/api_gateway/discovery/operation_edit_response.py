# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["OperationEditResponse"]


class OperationEditResponse(BaseModel):
    state: Optional[Literal["review", "saved", "ignored"]] = None
    """State of operation in API Discovery

    - `review` - Operation is not saved into API Shield Endpoint Management
    - `saved` - Operation is saved into API Shield Endpoint Management
    - `ignored` - Operation is marked as ignored
    """
