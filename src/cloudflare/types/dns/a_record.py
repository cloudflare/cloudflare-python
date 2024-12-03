# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["ARecord"]


class ARecord(BaseModel):
    content: Optional[str] = None
    """A valid IPv4 address."""

    type: Optional[Literal["A"]] = None
    """Record type."""
