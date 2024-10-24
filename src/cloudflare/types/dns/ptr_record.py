# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["PTRRecord"]


class PTRRecord(BaseModel):
    content: Optional[str] = None
    """Domain name pointing to the address."""

    type: Optional[Literal["PTR"]] = None
    """Record type."""
