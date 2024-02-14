# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UuidGetResponse"]


class UuidGetResponse(BaseModel):
    uuid: Optional[str] = None
    """The DCV Delegation unique identifier."""
