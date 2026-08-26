# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["PayloadCreateResponse"]


class PayloadCreateResponse(BaseModel):
    """Defines a Content Scanning custom expression."""

    id: Optional[str] = None
    """Defines the unique ID for this Content Scanning custom expression."""

    payload: Optional[str] = None
    """
    Defines the custom content extraction expression used to reach content objects
    in the request.
    """
