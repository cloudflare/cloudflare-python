# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ListDeleteResponse"]


class ListDeleteResponse(BaseModel):
    id: Optional[str] = None
    """The unique ID of the item in the List."""
