# File generated from our OpenAPI spec by Stainless.

from typing import Optional

from ..._models import BaseModel

__all__ = ["UUIDGetResponse"]


class UUIDGetResponse(BaseModel):
    uuid: Optional[str] = None
    """The DCV Delegation unique identifier."""
