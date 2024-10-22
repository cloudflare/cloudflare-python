# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AAAARecord"]


class AAAARecord(BaseModel):
    content: Optional[str] = None
    """A valid IPv6 address."""

    type: Optional[Literal["AAAA"]] = None
    """Record type."""
