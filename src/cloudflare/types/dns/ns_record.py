# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["NSRecord"]


class NSRecord(BaseModel):
    content: Optional[str] = None
    """A valid name server host name."""

    type: Optional[Literal["NS"]] = None
    """Record type."""
