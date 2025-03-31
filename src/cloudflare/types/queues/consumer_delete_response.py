# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ConsumerDeleteResponse"]


class ConsumerDeleteResponse(BaseModel):
    errors: Optional[List[object]] = None

    messages: Optional[List[str]] = None

    success: Optional[Literal[True]] = None
    """Indicates if the API call was successful or not."""
