# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["OperationEditResponse"]


class OperationEditResponse(BaseModel):
    state: Optional[Literal["review", "saved", "ignored"]] = None
    """State of operation in API Discovery

    - `review` - Operation is not saved into API Shield Endpoint Management
    - `saved` - Operation is saved into API Shield Endpoint Management
    - `ignored` - Operation is marked as ignored
    """
