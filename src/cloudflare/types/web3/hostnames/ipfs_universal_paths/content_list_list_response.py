# File generated from our OpenAPI spec by Stainless.

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel

__all__ = ["ContentListListResponse"]


class ContentListListResponse(BaseModel):
    action: Optional[Literal["block"]] = None
    """Behavior of the content list."""
