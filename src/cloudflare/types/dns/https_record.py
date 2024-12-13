# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["HTTPSRecord", "Data"]


class Data(BaseModel):
    priority: Optional[float] = None
    """priority."""

    target: Optional[str] = None
    """target."""

    value: Optional[str] = None
    """value."""


class HTTPSRecord(BaseModel):
    content: Optional[str] = None
    """Formatted HTTPS content. See 'data' to set HTTPS properties."""

    data: Optional[Data] = None
    """Components of a HTTPS record."""

    type: Optional[Literal["HTTPS"]] = None
    """Record type."""
